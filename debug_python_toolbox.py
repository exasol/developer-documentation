import nox

# imports from PTB
from typing import Optional, Union
import datetime
from pathlib import Path
from exasol.toolbox.metrics import Report
import json
from tempfile import TemporaryDirectory
from nox import Session

# new imports
import subprocess
import sys

def total_coverage(file: Union[str, Path]) -> float:
    with TemporaryDirectory() as tmpdir:
        tmp_dir = Path(tmpdir)
        report = tmp_dir / "coverage.json"
        p = subprocess.run(
            ["coverage", "json", f"--data-file={file}", "-o", f"{report}"],
            capture_output=True,
            check=False,
            encoding="utf-8",
        )
        stdout = p.stdout.strip()
        if (p.returncode == 1) and (stdout == "No data to report."):
            print(
                f'The following command'
                f' returned non-zero exit status {p.returncode}:\n'
                f'  {" ".join(p.args)}\n'
                f'{stdout}\n'
                'Returning total coverage 100 %.',
                file=sys.stderr,
            )
            return 100.0
        with open(report, encoding="utf-8") as r:
            data = json.load(r)
            total: float = data["totals"]["percent_covered"]

        return total


def create_report(
    commit: str,
    date: Optional[datetime.datetime] = None,
    coverage_report: Union[str, Path] = ".coverage",
    pylint_report: Union[str, Path] = ".lint.txt",
    bandit_report: Union[str, Path] = ".security.json",
) -> Report:
    return total_coverage(coverage_report)
    return Report(
        commit=commit,
        date=date if date is not None else datetime.datetime.now(),
        coverage=total_coverage(coverage_report),
        maintainability=maintainability(pylint_report),
        reliability=reliability(),
        security=security(bandit_report),
        technical_debt=technical_debt(),
    )


@nox.session(name="project:report", python=False)
def report(session: Session) -> None:
    sha1 = str(
        session.run("git", "rev-parse", "HEAD", external=True, silent=True)
    ).strip()
    project_report = create_report(commit=sha1)
