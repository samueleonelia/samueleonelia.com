# STATUS — samueleonelia.com

Phase: **v2 — built, waiting on content** · Branch: `v2` · Folders: `v1/` live, `v2/` new · Last updated: 2026-10-15

- Live (v1): https://samueleonelia.com — frozen at tag `v1.0`
- v2 page: `v2/index.html` · phone preview (outdated, shows the old dark look): https://claude.ai/artifact/NAkDbkCXfK8ZojfeVb8qGx
- v2 plan and decisions: `plans/v2.md`
- Repo: https://github.com/samueleonelia/samueleonelia.com (private)
- Netlify admin: https://app.netlify.com/projects/samueleonelia
- Local preview: `site` server in `.claude/launch.json` → http://localhost:8765/v2/

## v2 phases

| Phase | State |
|---|---|
| Setup (`v1/` + `v2/` folders, tag v1.0, plan) | Done |
| 1. Brief | Done — AI + automation only, for clients and followers |
| 2–3. Structure + design | Done — restyled 2026-10-15 after dagorenouf.com: white page, heavy caps, boxed buttons |
| 4. Build into `v2/` | Done — checked at 1024px and phone width |
| 4b. Real content in the amber boxes | **Waiting on Samuele** |
| 4c. Automation log | Done — simulated, from a catalogue of 56 real automations; each line opens a details window |
| 5. Check (real phone, Safari, OG image) | Not started |
| 6. Launch (publish `v2`, deploy, tag v2.0) | Not started |

## v2 page sections

Hero (round portrait, handwritten notes, workflow background) · black automations.log bar · logos · numbers ·
3 offers as numbered rows (AI Employees, AI Training, Process automations) ·
8 case studies · Hypefury quote on a black band · FAQ · follow along · contact · footer.

## Next

1. Samuele reviews the phone preview and the 56 automation descriptions.
2. Samuele decides which clients (if any) to name in the details windows (`plans/automation-catalog.md`).
3. Samuele reviews the rest of the page and gives feedback.
4. Samuele supplies: result per project, price + timeline answers, newsletter / YouTube / podcast links.
5. OG share image, then real-phone + Safari check.

## Blocked on Samuele

- Check the automation descriptions; choose any client names to show.
- Feedback on the new white look (after dagorenouf.com) and the 3 offers.
- Amber-box content (results, FAQ answers, follow links).
- Verify an email on the Netlify account so pushes auto-deploy.
- Confirm Dream Travel Agency and Bmark logos are the right companies.
- Tell Yannick Veys the X thread is on the site.

## Known issues

- "Before" lines on project cards are Claude's wording from v1 text; Samuele should check them.
- Deploys are manual: `netlify deploy --prod --dir v1` (v2 only at launch).
- v1 and v2 not yet tested on a real phone or in Safari.
