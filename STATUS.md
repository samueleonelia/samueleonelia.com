# STATUS — samueleonelia.com

Phase: **v2 — built, being refined, waiting on content** · Branch: `v2` · Folders: `v1/` live, `v2/` new · Last updated: 2026-10-31

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
| 2–3. Structure + design | Done — white page, dark green text (#062123), teal only on clickable things (#0F766E), all monospace (Azeret Mono heavy + Space Mono text), pale teal gradient on hover only, teal dot field behind the whole page (as on sosautomazioni.com) |
| 4. Build into `v2/` | Done — checked at 1280px and 375px |
| 4b. Real content in the dashed boxes | Dropped 2026-10-31 — result lines removed from all case studies |
| 4c. Automation log | Removed 2026-10-31 at Samuele's request (in git before that date) |
| 5. Check (real phone, Safari, OG image) | Not started |
| 6. Launch (publish `v2`, deploy, tag v2.0) | Not started — contact form needs Netlify setup: turn on form detection, add an email notification, send a test message |

## v2 page sections

Dark green header · Hero (colour portrait, headline, handwritten notes, one button) · "I've worked with": 10 logos, white, scrolling on a dark green strip ·
2 offer cards, as on sosautomazioni.com (Process automation, AI Training), both booking a free call ·
Past projects: 9 rows with the CV's copy and order, open on hover or tap · dark band: Yaron Brook video testimonial · contact form (Netlify Forms) · footer (only place with Padova).

## Next

1. Samuele reviews the redesign and keeps sending changes. The phone preview needs a rebuild to show it.
2. OG share image, then real-phone + Safari check.

## Blocked on Samuele

- Which phone number is right: the site shows +39 348 584 3362, the CV shows +39 392 595 7421.
- Verify an email on the Netlify account so pushes auto-deploy.
- Confirm Dream Travel Agency and Bmark logos are the right companies.

## Known issues

- Hover colours, the card tilt and the mouse line don't show on phones (no mouse there). Project rows open with a tap.
- Deploys are manual: `netlify deploy --prod --dir v1` (v2 only at launch).
- v1 and v2 not yet tested on a real phone or in Safari.
