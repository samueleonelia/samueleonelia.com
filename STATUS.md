# STATUS — samueleonelia.com

Phase: **v2 — built, being refined, waiting on content** · Branch: `v2` · Folders: `v1/` live, `v2/` new · Last updated: 2026-10-16

- Live (v1): https://samueleonelia.com — frozen at tag `v1.0`
- v2 page: `v2/index.html` · phone preview (rebuild with `tools/build-mockup.py`): https://claude.ai/artifact/NAkDbkCXfK8ZojfeVb8qGx
- v2 plan and decisions: `plans/v2.md`
- Repo: https://github.com/samueleonelia/samueleonelia.com (private)
- Netlify admin: https://app.netlify.com/projects/samueleonelia
- Local preview: `site` server in `.claude/launch.json` → http://localhost:8765/v2/

## v2 phases

| Phase | State |
|---|---|
| Setup (`v1/` + `v2/` folders, tag v1.0, plan) | Done |
| 1. Brief | Done — AI + automation only, for clients and followers |
| 2–3. Structure + design | Done — white page after dagorenouf.com, all monospace (Azeret Mono heavy + Space Mono text), grey gradient on hover only |
| 4. Build into `v2/` | Done — checked at 1280px and 375px |
| 4b. Real content in the dashed boxes | **Waiting on Samuele** |
| 4c. Automation log | Done — simulated, 56 real automations, each line opens a details window |
| 5. Check (real phone, Safari, OG image) | Not started |
| 6. Launch (publish `v2`, deploy, tag v2.0) | Not started |

## v2 page sections

Hero (colour portrait, headline, handwritten notes, workflow background) · black automations.log bar ·
10 client logos · 3 offers (AI Employees, AI Training, Process automations) ·
8 case studies · Hypefury quote + X thread on a black band · FAQ · follow along · contact · footer (only place with Padova).

## Next

1. Samuele keeps reviewing the phone preview and sends changes.
2. Samuele supplies: result per project, price + timeline answers, newsletter / YouTube / podcast links.
3. Samuele checks the 56 automation descriptions and picks any client names to show (`plans/automation-catalog.md`).
4. OG share image, then real-phone + Safari check.

## Blocked on Samuele

- Dashed-box content (results, FAQ price/timeline, follow links).
- Automation descriptions and client names.
- Verify an email on the Netlify account so pushes auto-deploy.
- Confirm Dream Travel Agency and Bmark logos are the right companies.
- Tell Yannick Veys the X thread is on the site.

## Known issues

- "Before" lines on project cards are Claude's wording from v1 text; Samuele should check them.
- Hover colours don't show on phones (no hover there): the site is black and white on mobile.
- Deploys are manual: `netlify deploy --prod --dir v1` (v2 only at launch).
- v1 and v2 not yet tested on a real phone or in Safari.
