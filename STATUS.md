# STATUS — samueleonelia.com

Phase: **v2 live since 2026-10-31, contact form set up, delivery not yet tested** · Branch: `v2` · Folders: `v2/` live, `v1/` old · Last updated: 2026-10-31

- Live (v2): https://samueleonelia.com — tag `v2.0`. Old site: `v1/`, tag `v1.0`
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
| 5. Check (real phone, Safari, OG image) | Not done — launched without it at Samuele's request |
| 6. Launch (publish `v2`, deploy, tag v2.0) | Done 2026-10-31 |

## v2 page sections

Dark green header · Hero (colour portrait, headline, one button) · "I've worked with": 10 logos, white, scrolling on a dark green strip ·
2 offer cards, as on sosautomazioni.com (Process automation, AI Training), both booking a free call ·
Past projects: 9 compact rows with the CV's names, copy and order, expand downward on hover or tap · dark band: Yaron Brook video testimonial · contact form (Netlify Forms) · footer (only place with Padova).

## Next

1. Samuele sends one test message through the live form and confirms the email arrives.
2. OG share image, then real-phone + Safari check.

## Blocked on Samuele

- Test message through the form (see Next), and check the privacy policy covers the form.
- Which phone number is right: the site shows +39 348 584 3362, the CV shows +39 392 595 7421.
- Verify an email on the Netlify account so pushes auto-deploy.
- Confirm Dream Travel Agency and Bmark logos are the right companies.

## Known issues

- Hover colours, the card tilt and the mouse line don't show on phones (no mouse there). Project rows open with a tap.
- Deploys are manual: `netlify deploy --prod --dir v2`, from the repo root.
- Form delivery is set up but not yet proven with a real message.
- No share image (OG) yet. Not tested on a real phone or in Safari.
