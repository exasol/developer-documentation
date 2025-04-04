# Unreleased

## Features

* #1: Added initial Project Setup


Findings in `report.yml`, columns: 
* DEVDOC: whether the resp. finding affects the repository developer-documentation, 
* PTB: whether the finding affects the folder `.github/workflows/` in the PTB
* PTB Template:  whether the finding affects the folder `exasol/toolbox/templates/github/workflows/` in the PTB 

| Location | Finding | DEVDOC | PTB | PTB Template |
|----------|---------|--------|-----|---|
| Step "Generate GitHub Summary", `poetry run -- coverage report --format markdown` | must ignore coverage error due to no data | Y | Y | Y |
| Step "Copy Artifacts into Root Folder" | copies 2x `.lint.txt` but must copy `.lint.json`, too | Y | - | Y |
| Step "Generate GitHub Summary" | contains 2x security, but must be 1x lint and 1x security | Y | - | - |
