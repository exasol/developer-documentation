import os
import sys

import nox

# imports all nox task provided by the toolbox
from exasol.toolbox.nox.tasks import *

# default actions to be run if nothing is explicitly specified with the -s option
nox.options.sessions = ["project:fix"]


@nox.session(python=False, name="doc:serve")
def serve_docs(session):
    session.run(
        sys.executable,
        "-m",
        "http.server",
        "9000",
        "--directory",
        ".html-documentation",
    )
