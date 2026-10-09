# Contributing

Thank you for contributing to Sharpe Nova OS. Contributions should preserve the
system's role as pre-execution governance infrastructure for consequential
machine-prepared capital actions.

## Doctrine Boundaries

Contributions must preserve these boundaries:

- Nova does not authorize execution.
- Nova does not move capital.
- Nova does not provide trading signals.
- Nova does not optimize portfolios.
- Nova structures bounded governed pre-execution review context; local authority
  decides and external systems execute.

Avoid adding examples, field names, docs, or tests that imply Nova grants permission, approves decisions, executes orders, or recommends trades.

## Environment Setup

Create the local environment with Python 3.12 and the same constrained dependency resolution used in CI:

```bash
python3.12 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt -c constraints.txt
.venv/bin/python -m pip check
```

## Required Checks

Before opening a pull request, run the complete repository validation contract:

```bash
make verify
```

Individual controls are available through `make verify-doctrine`,
`make verify-scenarios`, `make verify-tests`, `make verify-chronology`, and
`make verify-whitespace`. `make test` and `make verify-tests` run the full
pytest suite; use `make test-isolated` only for diagnostic file-by-file runs.

Keep changes narrowly scoped and document governance-boundary changes in the relevant docs.
