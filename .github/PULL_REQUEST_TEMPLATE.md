## Why

## What changed

## Scope

What this covers, and what it deliberately leaves out.

## Blast radius

## Verification

Evidence per acceptance criterion. Name the test, the CI run, the screenshot, or the measurement. If this repo has no CI, say so.

## Gate

Author, before requesting review (G3):

- [ ] Branch is `sdlc/<work_id>/<slice>` (or this PR is the foundation / docs PR and says so)
- [ ] CI is green on this head SHA, or there is no CI workflow yet
- [ ] Scope matches the slice
- [ ] Auto-merge is off

Reviewer, in the review and in `docs/sdlc/<work_id>/review.md` (G4):

- [ ] Every AC has evidence
- [ ] No open critical or high `/interrogate` finding
- [ ] Preview smoke-tested, or no preview exists
- [ ] Verdict is `PASS` or `REWORK:<stage>`

Docs PR only (delete when this is a code PR):

- [ ] Contains `brief.md`, `requirements.md`, `design.md`, the ADR, and `impl-plan.md`
- [ ] Merging is the H1/H2 record. Joseph merges it.

Joseph merges. Do not enable auto-merge. A `PASS` review does not merge this PR.

Work-Id:
Slice:
AC:
