---
description: SDLC pipeline rules for agents in the product repo. Branch names, PR trailers, pstack, and manual merge.
alwaysApply: true
---

# SDLC

These rules govern the product repo. Copy this file to `.cursor/rules/sdlc.md` there. Work items, branches, and pull requests for a slice belong in that repo. Adopter values are `docs/sdlc/config.yml`, copied from `docs/sdlc/config.example.yml` and left uncommitted. The spec is `docs/sdlc/SDLC_PIPELINE.md`. Templates are `docs/sdlc/_templates/`. The forge is GitHub. The tracker is GitHub Issues in the product repo.

When you implement a slice:

- Read, in order, `docs/sdlc/<work_id>/requirements.md`, `design.md`, `impl-plan.md`, and the ADR named in the plan. Do not redesign. Do not widen scope.
- Run pstack `/poteto-mode` with the playbook in the impl plan. Sequenced slices use `autopilot-stack` and stop at `STACK-READY`. Do not run `autopilot-full` or `shipping`.
- Branch: `sdlc/<work_id>/<slice-id>`. One PR per slice, in this product repo. A stack is base-chained on GitHub with `gh pr edit --base <parent-branch>`. Do not use Graphite or Origin.
- PR title: Conventional Commits, imperative, no trailing period.
- PR body is a short briefing: why, what changed, scope, blast radius, verification. It ends with these trailers, each on its own line:

```text
Work-Id: <work_id>
Slice: <slice-id>
AC: AC-1, AC-2
```

- Put runtime evidence for each AC in the body (a failing test that then passes, a screenshot, or a measurement). If this product repo has no CI workflow, say that. Do not claim CI is green.
- For T1 and T2, log decisions with `/show-me-your-work` to `docs/sdlc/<work_id>/decisions.tsv`.
- If an AC is ambiguous or the design does not fit the code, stop and report it. Do not guess.

Merge rule, every stage, every tier:

- Do not merge. Do not enable auto-merge. Do not retarget a stacked PR onto trunk. Do not close a PR unless Chief of Staff sent `CANCEL`.
- The owner merges every PR after Reviewer/QA approves. A `PASS` review is not a merge.
- Do not commit secrets, tokens, credentials, `.env` values, or `docs/sdlc/config.yml`. Name env vars only.
