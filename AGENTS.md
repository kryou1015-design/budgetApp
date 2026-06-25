# AGENTS.md

## Project Overview

This repository is a Python CLI budget app that stores and reads household transaction data from CSV files.

The application should support command-line workflows for recording, listing, summarizing, and validating income and expense data while keeping the CSV format simple and predictable.

## Coding Rules

- Use Python type hints for all public functions, internal functions, and methods.
- Keep each function to 50 lines or fewer.
- Prefer small, pure functions for parsing, validation, filtering, and summary calculations.
- Keep CLI input/output code separate from budget domain logic where practical.
- Handle invalid CSV rows and user input with clear errors.

## TDD Rules

- Write failing tests before implementing behavior.
- Do not add production logic until the expected behavior is covered by tests.
- Add or update tests for every bug fix and feature.
- Keep tests focused on observable behavior: CSV parsing, validation, calculations, and CLI output.

## Quality Rules

- Keep cyclomatic complexity at 10 or below for each function.
- Refactor branching-heavy logic into smaller named functions before it exceeds the limit.
- Avoid hidden global state; pass paths, data, and options explicitly.

## Quality Review Rules

- Before every commit, run the `qa_engineer` subagent for quality review.
- The `qa_engineer` review must check tests, type hints, function length, cyclomatic complexity, and TDD evidence.
- Do not commit while the `qa_engineer` has unresolved blocking findings.

## Test And Quality Commands

```powershell
pytest
radon cc .
```

## Commit Rules

- Commit when one complete feature or bug fix is developed.
- Run tests and quality checks before committing.
- Push after committing completed work.
- Keep commit messages concise and behavior-focused.
