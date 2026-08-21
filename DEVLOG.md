# DEVLOG — samueleonelia.com

## 2026-08-21 — Session 1: mockup

**Status:** phase = mockup / review · branch = `main`

### What was done
- Initialised the Git repo and a `.gitignore` for a static site (OS files, editors, secrets, `build/`, `node_modules/`).
- Pulled the source content from the CV artifact (`b593c7bd-1e3f-4e6a-a1bc-3683fa6e79a2`). The pharmacy role was excluded as requested; the Pharmacy degree is also currently left off the site.
- Extracted the portrait photo out of the CV's base64 data URI into `assets/portrait.jpg` (65 KB JPEG).
- Built the whole site as a single `index.html` — inline CSS and JS, no build step, no framework. This keeps it deployable to Netlify by dropping the folder in, and readable by a non-developer.
- Wrote `tools/build-mockup.py`, which converts `index.html` into `build/mockup.html`: strips the `<!doctype>/<html>/<head>/<body>` wrapper and inlines local assets as data URIs, because the Claude Artifact host supplies its own document shell and its CSP blocks external hosts (Google Fonts excepted).
- Published the mockup: https://claude.ai/code/artifact/8112620f-a4ed-4353-b8c5-86e414ff3e64

### Key decisions
- **English only, all clients named, case-study cards** — chosen by Samuele up front.
- **Design direction deliberately away from the reference's warm cream.** The reference (sebastian-wittig.design) contributed the *structure*: single-page scroll, heavy whitespace, portrait hero, client marquee, narrative case studies. The palette is cool paper + cobalt `#1B44E8` + a green reserved strictly for "running" status, so it reads like a control panel rather than a design magazine — which fits an automation specialist better than a warm editorial look.
- **Type:** Bricolage Grotesque (display) / IBM Plex Sans (body) / IBM Plex Mono (labels, dates, machine voice). Google Fonts is the only font host the Artifact CSP allows, and all three are on it.
- **"By hand → Now" pair inside each project card.** The structure encodes the actual product: every card shows the manual process being replaced. It is the thing being sold, so it earns its place as a layout device rather than decoration.
- **Both light and dark themes** driven token-level off `prefers-color-scheme`, plus `[data-theme]` stamps so the Artifact viewer's toggle works. No in-page theme switch on the site itself.
- **Single file over a static site generator.** At this size a generator is overhead; if the EN/IT toggle is added later this decision should be revisited.

### Open issues
- Project "By hand" lines are inferred from the CV, not quoted from Samuele. They read as plausible but must be fact-checked by him before the site goes live.
- The phone number is public on the page. Samuele may want it removed.
- No favicon, no OG/social share image, no `netlify.toml` yet.
- Portrait is the CV headshot, 600×600 and slightly soft at large sizes. A higher-resolution original would help.
