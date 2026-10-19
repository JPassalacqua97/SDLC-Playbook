# Bot role instructions

Paste the body of each file into that bot after you replace every `<PLACEHOLDER>` from [../config.example.yml](../config.example.yml). The files already include the shared preamble where the specialist needs it. Read them before you paste.

The placeholders name the product repo and the bot routing ids. They do not name this playbook as the place where work runs.

| File | Bot | Stage | Placeholder |
|---|---|---|---|
| [chief-of-staff.md](chief-of-staff.md) | Chief of Staff | routes every stage | `<COS_BOT_ID>` is this bot. The file lists the others. |
| [product.md](product.md) | Product / Requirements Analyst | 1 | `<PRODUCT_BOT_ID>` |
| [architect.md](architect.md) | Architect | 2 | `<ARCHITECT_BOT_ID>` |
| [developer.md](developer.md) | Developer | 3 | `<DEVELOPER_BOT_ID>` |
| [reviewer.md](reviewer.md) | Reviewer / QA | 4 | `<REVIEWER_BOT_ID>` |
| [ops.md](ops.md) | Ops / Release Engineer | 5 and incidents | `<OPS_BOT_ID>` |
| [scribe.md](scribe.md) | Scribe / Documentation Engineer | 6 | `<SCRIBE_BOT_ID>` |

Routing ids are not credentials. The general Grok Bot has no id in the design. Chief of Staff uses it only as backup and for one-off research (D8 is still a working assumption).

The spec these instructions follow is [../SDLC_PIPELINE.md](../SDLC_PIPELINE.md).
