# samueleonelia.com

## What this is
Samuele's personal portfolio site, live at https://samueleonelia.com. Plain static HTML/CSS/JS, no framework, no `package.json`, no build step. Two versions side by side: `v1/` (live) and `v2/` (new version in progress). v1 page structure: hero → work → thread → services → contact.

## What's inside
- `v1/` — the live site (current Netlify publish dir). `index.html` is the page; `assets/` holds images and company logos.
- `v2/` — the new version in progress. Started as a copy of `v1/`. Not published.
- `netlify.toml` — build config (`publish = "v1"`, the live folder), the `.netlify.app` → custom domain redirect, and security headers.
- `plans/` — plans, e.g. `v2.md`. Not published.
- `tools/build-mockup.py` — inlines a version's `index.html` local assets (`python3 tools/build-mockup.py v1`, default `v2`) as base64 so it can be pasted into a Claude Artifact for previewing (the Artifact host blocks external asset hosts).
- `build/mockup-v1.html`, `build/mockup-v2.html` — output of that script. Not committed, not published.
- No `.claude/` folder, no `AGENTS.md`, no `CLAUDE.local.md` in this repo.

## Tools and connectors
None configured for this folder.

## Deploy
- GitHub: https://github.com/samueleonelia/samueleonelia.com (private)
- Netlify admin: https://app.netlify.com/projects/samueleonelia
- As of the last STATUS.md update, GitHub auto-deploy was **not** linked yet — deploys were manual via `netlify deploy --prod --dir v1`. Check STATUS.md for current state before assuming either way.

## Versions
- `v1/` = the live site. Don't change it except for urgent fixes to what's live.
- `v2/` = the new version. Plan and phases: `plans/v2.md`.
- Git: work on the `v2` branch, merge into `main` at checkpoints. v1 also frozen at tag `v1.0`.
- Preview v2: `netlify deploy --dir v2` (draft URL). Never `--prod` with v2 until launch.
- Live deploy: `netlify deploy --prod --dir v1`.

## Rules
- Never edit `DEVLOG.md` or `STATUS.md` directly outside the normal session-continuity workflow (write history to DEVLOG, keep STATUS current) — see the global CLAUDE.md rules.
- Only the folder in `netlify.toml`'s `publish` (now `v1/`) is served live; everything else (v2/, DEVLOG, STATUS, tools/, plans/) stays private even if pushed.

## Remember
<!-- Things Samuele explicitly asked Claude to remember for this project. Claude adds items here when told "remember X". -->
