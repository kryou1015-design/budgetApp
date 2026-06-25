---
name: budget-cli-tdd
description: Build, test, and review this Python CSV-based budget CLI app using strict TDD and quality gates. Use when implementing CLI features, CSV parsing or validation, transaction summaries, tests, refactors, bug fixes, or pre-commit quality review for this budgetApp repository.
---

# Budget CLI TDD

## Overview

Use this skill to work on the budgetApp project without drifting from its engineering rules: tests first, typed Python, small functions, and low complexity.

The app is a Python command-line household budget tool backed by CSV transaction data.

## Workflow

1. Read `AGENTS.md` before changing code.
2. Identify the smallest behavior to implement.
3. Write or update failing tests first.
4. Implement the smallest production change that passes the tests.
5. Keep all functions at 50 lines or fewer.
6. Add type hints to every function and method.
7. Run `pytest`.
8. Run `radon cc .`.
9. Before commit, ask the `qa_engineer` subagent to review the change.
10. Commit one completed feature or bug fix, then push.

## Implementation Rules

- Treat CSV parsing, validation, filtering, and summarization as domain logic.
- Keep CLI input/output thin and separate from domain logic where practical.
- Prefer small pure functions for calculations and row transformations.
- Return structured values from domain code instead of printing directly.
- Raise or report clear errors for missing files, malformed rows, invalid dates, invalid amounts, and unknown transaction types.

## Test Rules

- Write tests before implementation.
- Cover the behavior that will be visible to users or other modules.
- Include tests for invalid CSV rows and edge cases when touching parsing or validation.
- Include CLI tests when command output, arguments, or exit behavior changes.

## Quality Gates

Run these before handoff or commit:

```powershell
pytest
radon cc .
```

The expected complexity limit is 10 or below for each function.

## Pre-Commit Review

Before committing, invoke the `qa_engineer` subagent and provide:

- Summary of the behavior changed.
- Test files added or updated.
- `pytest` result.
- `radon cc .` result.
- Any known risks or skipped checks.

Do not commit while the review has unresolved blocking findings.
