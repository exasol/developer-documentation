from __future__ import annotations

from pathlib import Path

from exasol.toolbox.config import BaseConfig

PROJECT_CONFIG = BaseConfig(
    root_path=Path(__file__).parent,
    project_name="developer_documentation",
    # The developer-documentation does not run against any Exasol DBs.
    exasol_versions=(),
)
