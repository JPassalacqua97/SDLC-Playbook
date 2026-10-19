# SDLC Playbook

A reusable software delivery playbook for a multi-bot team. You copy the scaffolding into a product repository and run the work there. This repository is the playbook.

The team is Chief of Staff, Product, Architect, Developer, Reviewer/QA, Ops, and Scribe. Implementation is a Cursor cloud agent with the [pstack](https://cursor.com/marketplace/cursor/pstack) plugin. The tracker is GitHub Issues. You, the owner, merge every pull request after Reviewer/QA records `PASS`. Auto-merge stays off.

The design is [docs/sdlc/SDLC_PIPELINE.md](docs/sdlc/SDLC_PIPELINE.md). Every value you must fill in is [docs/sdlc/config.example.yml](docs/sdlc/config.example.yml).

## Prerequisites

- Cursor.
- pstack. In Cursor, run `/add-plugin pstack`, then `/setup-pstack` to choose models and a reasoning budget. `/setup-pstack` writes `~/.cursor/rules/pstack-models.mdc` on that Cursor account. Do not commit that file.
- GitHub, with the [GitHub CLI](https://cli.github.com/) (`gh`) authenticated for the product repo.

## Quick start

1. Copy these paths into the product repo, keeping the same layout:
   - `.cursor/rules/sdlc.md`
   - `.cursor/settings.json`
   - `.github/ISSUE_TEMPLATE/brief.md`
   - `.github/ISSUE_TEMPLATE/config.yml`
   - `.github/PULL_REQUEST_TEMPLATE.md`
   - `.github/sdlc-labels.json`
   - `.github/workflows/sdlc-labels.yml`
   - `scripts/create-sdlc-labels.py`
   - `docs/adr/0000-template.md`
   - `docs/adr/README.md`
   - `docs/sdlc/_templates/`
   - `docs/sdlc/config.example.yml`
   - `docs/sdlc/SDLC_PIPELINE.md`
   - `docs/sdlc/README.md`
   - `docs/sdlc/roles/`
2. In the product repo, copy `docs/sdlc/config.example.yml` to `docs/sdlc/config.yml` and replace every `<PLACEHOLDER>`. Add `docs/sdlc/config.yml` to that repo's `.gitignore`. The filled file holds bot routing ids. Do not commit it.
3. Create the labels from the product repo:

   ```bash
   python3 scripts/create-sdlc-labels.py
   ```

   `python3 scripts/create-sdlc-labels.py --dry-run` checks the label file without calling GitHub. After the label files are on the product repo's default branch, you can run the **Create SDLC labels** workflow instead. The workflow triggers on `main`. If `product.base_branch` in your config is not `main`, change `branches` in `.github/workflows/sdlc-labels.yml` to match.
4. Create the seven bots in Cursor. Paste each file in `docs/sdlc/roles/` into the matching bot. Replace every placeholder from your config before you paste. Record each bot id in `docs/sdlc/config.yml`.
5. Create the ledger at `ledger.path` (default `/cursor/stores/<COS_STORE_ID>/sdlc/ledger.jsonl`) in the Chief of Staff store. One JSON object per line, shaped like `docs/sdlc/_templates/ledger-event.json`. Do not commit the ledger.
6. Run a pilot in the product repo. Pick one small T1 item and one T0 item. Chief of Staff sends every message by hand. You merge only after Reviewer/QA records `PASS`. Leave routines off until that retro.

The copied rules, issue template, pull request template, label script, and workflow do not name a GitHub repository. They apply to the product repo you copied them into. Role text targets `<PRODUCT_REPO>` from the config, which is the product repo, not this playbook.

## What the owner approves

You are the owner. Bots stop and ask. A `PASS` review asks you to merge. It does not merge.

| Gate | When | What you do |
|---|---|---|
| H0 | T2, or the priority is unclear | Reply go or no-go. |
| H1 | T1 and T2 scope | Approve `requirements.md`. Merging the docs PR is the record. |
| H2 | T2 design | Approve the design by merging the docs PR. |
| H3 | Every tier, including T0 and docs | Merge the PR or stack on GitHub after Reviewer/QA `PASS`. |
| H4 | Production release for T1 and T2 | Reply naming the SHA. |
| H5 | A destructive database change | Reply quoting the migration name. |

Shipped defaults in `docs/sdlc/config.example.yml` keep merge with you: `owner_merges_every_pr: true`, `after_reviewer_qa_pass: true`, `auto_merge: false`, `delegate_merge: false`. Change those only by reopening decision D4 in the design.

## License

[MIT](LICENSE).
