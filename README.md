# AI Hackathon Example Repo

A small Python repository designed for short AI prototyping exercises during an engineering AI hackathon.

The repository intentionally contains a mixture of:
- realistic structure
- incomplete tests
- subtle bugs
- performance issues
- refactoring opportunities

The goal is **not** to build production software, but to give AI tools enough signal to analyze, reason about, and improve code.

---

## Running the project

Run the example program:

```bash
python -m app.main
```

Run the tests:

```bash
python -m pytest tests/
```

---

## Hackathon Prompts

Each team should draw **one prompt** and build a small tool that helps engineers solve the problem.

> **On baseline expectations:** Each prompt below includes a *baseline output* — the minimum a working tool should produce when run against this repo. Meeting the baseline means your tool works. The interesting engineering is in everything beyond it: better structure, smarter prompting, more useful output, a real interface. Aim to exceed it.

---

### 1. Test Generator
Build a tool that analyzes a code file or module and generates meaningful test cases. Compare the generated tests with existing tests and highlight missing coverage or edge cases.

Example inputs:
- source file
- module
- repository folder

**Baseline output:** Given `app/analytics.py` as input, the tool produces runnable pytest tests covering the main functions, and identifies at least two behaviours not covered by existing tests (e.g. `build_hot_path`, `build_anomaly_preview`).

---

### 2. Debugging Assistant
Build a tool that analyzes logs, stack traces, or terminal output and identifies likely root causes. Generate a bug ticket with a summary, possible causes, and suggested fixes.

Example inputs:
- application logs
- stack traces
- CI logs

**Baseline output:** Given `logs/app_error.log` as input, the tool produces a bug ticket that correctly identifies the root cause (`build_daily_report` does not filter `None` before calling `max`), names the affected file and line, and suggests a fix.

---

### 3. Tooling Assistant
Build a tool that helps engineers discover existing utilities or helper functions in a codebase. Given a task description, suggest relevant functions, modules, or examples to encourage reuse.

Example inputs:
- utilities modules
- repository folder
- natural language task description

**Baseline output:** Given the task description *"I need to clean up a user-provided name before storing it"*, the tool returns `normalize_name` in `app/utils.py` as the top suggestion, with a short explanation of what it does and where it is used.

---

### 4. Codebase Explainer
Build a tool that explains the entire codebase to a new engineer. The explanation should cover what each module does, how they fit together, and the key data flows through the system.

**Baseline output:** The tool produces an onboarding guide — no longer than two pages — that a new engineer could read in under 10 minutes and understand: (1) what the system does, (2) which modules own which responsibilities, and (3) how a request flows from `app/main.py` through to its dependencies. The guide should flag any parts of the codebase that are confusing or worth asking about (e.g. `legacy_helpers.py`, `buildThing`).

---

### 5. PR Intelligence
Build a tool that analyzes a Pull Request and generates a useful summary. Highlight the purpose of the change, important files, and potential risks.

Example inputs:
- PR diff
- commit list
- PR metadata

**Baseline output:** Given the `sample_pr/open_onboarding_preview` PR as input, the tool produces a summary that describes the purpose of the change, lists the files modified, and flags at least one potential risk or concern (e.g. missing null check on `user.email`).

---

### 6. Refactoring Assistant
Build a tool that analyzes a function or module and suggests improvements to structure, readability, or maintainability. The tool should identify code smells and propose a refactored version.

**Baseline output:** Given `app/workflows.py` as input, the tool identifies `process_user_lifecycle` as a refactoring target, names at least two specific code smells (e.g. deep nesting, mixed concerns), and produces a refactored version that is meaningfully shorter and easier to read.

---

### 7. Performance Insight Tool
Build a tool that analyzes code and identifies potential performance issues or inefficiencies. Highlight expensive operations, redundant work, or opportunities for optimization.

**Baseline output:** Given `app/analytics.py` as input, the tool identifies that `get_user_summary` is called twice per user in `build_dashboard_data` (once to pre-build `summaries`, once inside the main loop), explains why this is wasteful, and suggests caching or deduplication.

---

### 8. Edge Case Finder
Build a tool that analyzes a function and suggests edge cases or unusual inputs that should be tested. The goal is to improve robustness and uncover hidden bugs.

**Baseline output:** Given `app/report_service.build_percentile_report` as input, the tool identifies at least two edge cases not covered by existing tests: an empty input list (causes an `IndexError`) and `percentile=1.0` (index exceeds list bounds), and suggests test cases for each.

---

## Design Intent

This repo intentionally includes:
- incomplete tests
- subtle bugs
- duplicated helpers
- inefficient loops
- inconsistent validation
- poorly structured legacy code

AI tools should be able to:
- analyze code structure
- connect logs to source code
- identify missing tests
- detect refactoring opportunities
- identify edge cases
- summarize changes

The goal is to explore **how engineers actually use AI tools during development.**

