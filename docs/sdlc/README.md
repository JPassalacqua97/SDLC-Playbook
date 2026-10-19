# SDLC playbook

This folder is the pipeline design and the files you copy into the product repo `<PRODUCT_REPO>`. The repository that contains this folder is the playbook. Work items run in the product repo. Filled values are [config.example.yml](config.example.yml). The quick start is the repository [README](../../README.md).

## Layout

| Path | What it is | Where it runs |
|---|---|---|
| [SDLC_PIPELINE.md](SDLC_PIPELINE.md) | Design. Decisions D1–D4 and D6 are recorded there. | Read from the playbook. Copy it into the product repo so agents can read the same path. |
| [config.example.yml](config.example.yml) | Every placeholder and the merge defaults. | Copy to `docs/sdlc/config.yml` in the product repo and fill it. Do not commit the filled file. |
| [_templates/](_templates/) | Artifact templates for stages 0–7. | Copy into the product repo. Work artifacts are `docs/sdlc/<work_id>/` there. |
| [roles/](roles/) | Paste-ready instructions for each bot. | Paste into the bots. The text targets `<PRODUCT_REPO>`. |
| [../adr/0000-template.md](../adr/0000-template.md) | ADR template. | Copy into the product repo. Accepted ADRs live in that repo. |
| [../../.cursor/rules/sdlc.md](../../.cursor/rules/sdlc.md) | Rules for implementation agents. | Copy into the product repo. |
| [../../.cursor/settings.json](../../.cursor/settings.json) | Enables the pstack plugin for the checkout. | Copy into the product repo. It does not install the plugin. |
| [../../.github/sdlc-labels.json](../../.github/sdlc-labels.json) | Stage, tier, specialist, and gate labels. | Copy into the product repo and create the labels there. |
| [../../.github/ISSUE_TEMPLATE/brief.md](../../.github/ISSUE_TEMPLATE/brief.md) | GitHub issue body matches the brief. | Copy into the product repo. |
| [../../.github/PULL_REQUEST_TEMPLATE.md](../../.github/PULL_REQUEST_TEMPLATE.md) | PR body matches gates G3 and G4, and ends with trailers. | Copy into the product repo. |
| [../../scripts/create-sdlc-labels.py](../../scripts/create-sdlc-labels.py) | Creates the labels with `gh`. | Run in the product repo. |

`<work_id>` is `YYYYMMDD-<slug>`. Branches in the product repo are `sdlc/<work_id>/<slice>`.

## Decisions locked

- GitHub is the forge. GitHub Issues in the product repo are the tracker. Linear is not used.
- Artifacts live in the product repo.
- The owner merges every PR after Reviewer/QA approves. No auto-merge and no merge delegation, at any tier. Those defaults are in [config.example.yml](config.example.yml).
- Implementation is a Cursor cloud agent running the pstack plugin, checked out on the product repo.

D5 (prod promotion), D7 (which approval channel is canonical beyond the docs PR), D8 (general Grok Bot), D9 (connector re-auth), and D10 (Graphite) are still open. See §11 of the design.

## What you do by hand

The ordered steps are in the repository README. In short:

1. Install pstack in Cursor with `/add-plugin pstack`, then run `/setup-pstack`. Do not commit the model rule it writes.
2. Copy the scaffolding into the product repo and fill `docs/sdlc/config.yml` there.
3. Create the labels in the product repo with `python3 scripts/create-sdlc-labels.py`, or run the **Create SDLC labels** workflow.
4. Paste each file in [roles/](roles/) into the matching bot.
5. Create the ledger in the Chief of Staff store. Do not commit it.
6. Re-authenticate any connector a later stage will call (Figma, Vercel, Supabase, Sentry, PagerDuty). Skip Linear.
7. Pick one small T1 item and one T0 item for the manual-relay pilot. Chief of Staff sends every message by hand. Routines stay off until that retro.

Until the product repo has application CI, a G3 note of "no CI workflow" is the honest record.
