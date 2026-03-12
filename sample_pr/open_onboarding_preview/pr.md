# PR #148 - Add onboarding preview endpoint and workflow wiring

Status: open
Author: dev2
Reviewers: architect1
Labels: api, onboarding

## Summary
Expose a lightweight onboarding preview response from the API layer.

## Motivation
The frontend wants a single response it can call to preview onboarding details.

## Testing
- added local manual verification from REPL
- automated tests still TODO

## Risks
- touches API and workflow boundaries
- may surface downstream billing or notification errors directly

## Open Questions
- should this endpoint tolerate invalid payment amounts?
- should notification delivery run during preview generation?

