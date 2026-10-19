---
work_id: YYYYMMDD-slug
---

| Slice | Goal | ACs | Depends on | pstack playbook | Verification | Est. size |
|-------|------|-----|------------|-----------------|--------------|-----------|
| S1 | | AC-1 | — | feature | | S |

Delivery mode: single PR | autopilot-stack | orchestrate

`autopilot-full` is not a delivery mode. Joseph merges every PR. Sequenced slices use `autopilot-stack` and stop at `STACK-READY`.

Playbook values: `feature`, `bug fix`, `refactoring`, `perf`, `prototype`. Verification names a test, a measurement, or a manual check.
