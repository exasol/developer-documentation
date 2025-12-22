from __future__ import annotations

from pathlib import Path

from exasol.toolbox.config import BaseConfig

PROJECT_CONFIG = BaseConfig(
    root_path=Path(__file__).parent,
    project_name="developer_documentation",
    python_versions=("3.10", "3.11", "3.12", "3.13", "3.14"),
    # The developer-documentation does not run against any Exasol DBs.
    # We put a dummy version here for the purposes of the tests running.
    exasol_versions=("8.29.13",),
)
