# SDLC foundation

This repo is the pilot for the pipeline in [SDLC_PIPELINE.md](SDLC_PIPELINE.md).

The foundation PR adds the spec, the stage templates, the bot role text, the implementation rule, project-level pstack enablement, and the label definitions. It does not run a work item, merge anything, or turn on routines.

## Layout

| Path | What it is |
|---|---|
| [SDLC_PIPELINE.md](SDLC_PIPELINE.md) | Design. Decisions D1–D4 and D6 are recorded there. |
| [_templates/](_templates/) | Artifact templates for stages 0–7. Copy into `docs/sdlc/<work_id>/`. |
| [roles/](roles/) | Paste-ready instructions for each bot. |
| [../adr/0000-template.md](../adr/0000-template.md) | ADR template. |
| [../../.cursor/rules/sdlc.md](../../.cursor/rules/sdlc.md) | Rules for implementation agents. |
| [../../.cursor/settings.json](../../.cursor/settings.json) | Enables the pstack plugin for this repo. |
| [../../.github/sdlc-labels.json](../../.github/sdlc-labels.json) | Stage, tier, owner, and gate labels. |
| [../../.github/ISSUE_TEMPLATE/brief.md](../../.github/ISSUE_TEMPLATE/brief.md) | GitHub issue body matches the brief. |
| [../../.github/PULL_REQUEST_TEMPLATE.md](../../.github/PULL_REQUEST_TEMPLATE.md) | PR body matches gates G3 and G4, and ends with trailers. |

`<work_id>` is `YYYYMMDD-<slug>`. Branches are `sdlc/<work_id>/<slice>`.

## Decisions locked

- GitHub is the forge. GitHub Issues are the tracker. Linear is not used.
- Artifacts live in this repo.
- Joseph merges every PR after Reviewer/QA approves. No auto-merge and no merge delegation, at any tier.
- Implementation is a Cursor cloud agent running the pstack plugin.

D5 (prod promotion), D7 (which approval channel is canonical beyond the docs PR), D8 (general Grok Bot), D9 (connector re-auth), and D10 (Graphite) are still open. See §11 of the design.

## What Joseph does by hand

1. Install pstack in Cursor with `/add-plugin pstack`, then run `/setup-pstack` to pick models and a reasoning budget. The model rule is written to the Cursor account (`~/.cursor/rules/pstack-models.mdc`). Do not commit it. `.cursor/settings.json` only turns the plugin on for this repo; it does not install it.
2. Merge this PR on GitHub. Leave auto-merge off. That merge is the approval to adopt the foundation.
3. Create the labels. Either run `python3 scripts/create-sdlc-labels.py` locally with `gh` authenticated for this repo, or after this file is on `main` run the **Create SDLC labels** workflow (`workflow_dispatch`).
4. Paste each file in [roles/](roles/) into the matching bot. The Chief of Staff file lists the specialist routing ids.
5. Create the ledger at `sdlc/ledger.jsonl` in the Chief of Staff store. One JSON object per line, shaped like [_templates/ledger-event.json](_templates/ledger-event.json). Do not commit the live ledger.
6. Re-authenticate any connector a later stage will call (Figma, Vercel, Supabase, Sentry, PagerDuty). Skip Linear.
7. Pick one small T1 item and one T0 item for the manual-relay pilot. CoS sends every message by hand. Routines stay off until that retro.

This repo has no application CI and no preview deploy yet. A G3 note of "no CI workflow" is honest. Do not invent a green check.
