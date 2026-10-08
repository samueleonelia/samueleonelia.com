# samueleonelia.com

## What this is
Samuele's personal portfolio site, live at https://samueleonelia.com. Plain static HTML/CSS/JS, no framework, no `package.json`, no build step. Page structure: hero → work → thread → services → contact.

## What's inside
- `public/` — the published site (Netlify publish dir). `index.html` is the actual page; `assets/` holds images and company logos.
- `netlify.toml` — build config (`publish = "public"`), the `.netlify.app` → custom domain redirect, and security headers.
- `plans/` — plans, e.g. `v2.md`. Not published.
- `tools/build-mockup.py` — inlines `public/index.html`'s local assets as base64 so it can be pasted into a Claude Artifact for previewing (the Artifact host blocks external asset hosts).
- `build/mockup.html` — output of that script. Not published (Netlify only serves `public/`).
- No `.claude/` folder, no `AGENTS.md`, no `CLAUDE.local.md` in this repo.

## Tools and connectors
None configured for this folder.

## Deploy
- GitHub: https://github.com/samueleonelia/samueleonelia.com (private)
- Netlify admin: https://app.netlify.com/projects/samueleonelia
- As of the last STATUS.md update, GitHub auto-deploy was **not** linked yet — deploys were manual via `netlify deploy --prod --dir public`. Check STATUS.md for current state before assuming either way.

## Versions
- `main` = the live site. Never commit unfinished work there.
- `v2` branch = the new version in progress. Plan and phases: `plans/v2.md`.
- v1 is frozen at tag `v1.0`.
- Preview v2 with `netlify deploy --dir public` (draft URL). Never `--prod` from `v2`.

## Rules
- Never edit `DEVLOG.md` or `STATUS.md` directly outside the normal session-continuity workflow (write history to DEVLOG, keep STATUS current) — see the global CLAUDE.md rules.
- Only `public/` is served live; anything outside it (DEVLOG, STATUS, tools/) stays private even if pushed.

## Remember
<!-- Things Samuele explicitly asked Claude to remember for this project. Claude adds items here when told "remember X". -->
