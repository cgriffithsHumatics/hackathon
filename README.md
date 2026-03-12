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

> **Note:** The same bug surfaces across multiple log files (`app_error.log`, `billing_error.log`, `grafana_loki_export.txt`) with different context in each. A stronger tool correlates signals across all of them — connecting the application error, the billing retry behaviour, and the Grafana pod-level event into a single coherent bug report. That cross-file reasoning is where the interesting engineering is.

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
Build a tool that analyzes a module and suggests edge cases or unusual inputs that should be tested across all its functions. The goal is to improve robustness and uncover hidden bugs.

Example inputs:
- a module or file
- a list of functions

**Baseline output:** Given `app/report_service.py` as input, the tool identifies at least two edge cases not covered by existing tests: an empty input list passed to `build_percentile_report` (causes an `IndexError`) and `percentile=1.0` (index exceeds list bounds), and suggests test cases for each.

> **Note:** Scoping to a full module means the tool needs to prioritise — not every function has interesting edge cases. A stronger tool reasons about which functions are riskiest (e.g. those that index, divide, or call external dependencies) and focuses its output there rather than producing a flat list of obvious cases for every function.

---

## Demos

Each team gets **5 minutes** to present, followed by a few minutes for questions. With 7-8 teams, the demo hour will move fast — keep it tight.

### What to show

Run your tool live against this repo. Show the input, show the output. A working demo of something simple beats a polished walkthrough of something that doesn't quite run.

You don't need slides. You don't need to explain every design decision. Show the thing.

### What to talk about

Five minutes goes quickly. Spend it on:

1. **What your tool does** — one sentence, then show it running.
2. **One decision that mattered** — how did you structure the prompt, chunk the input, or format the output, and why?
3. **What surprised you** — something the AI did better than expected, worse than expected, or just differently than you assumed.

If you went beyond the baseline, show that too. But don't skip the basics to get to the fancy stuff.

### What judges are looking for

There are two prizes:

**Best in Show** — awarded by a judging panel. They'll be looking for:
- Does the tool actually work, reliably, on real input?
- Is the output genuinely useful — something an engineer would act on?
- Did the team make thoughtful choices about how to use the AI, or just wrap a single prompt?

**Peer Choice** — voted on by all participants. Vote for the team whose tool you'd most want to use in your actual day-to-day work.

### What not to stress about

- Code quality. This is a prototype, not a PR.
- Edge cases your tool doesn't handle. Every tool has them.
- Whether your approach was the "right" one. There isn't one.

The goal is to learn something about how AI tools fit into an engineering workflow. A demo that shows what didn't work is just as valuable as one that shows what did.

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

