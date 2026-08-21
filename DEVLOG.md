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

## 2026-08-21 — Session 1 (cont.): streamlining

Samuele's read: the page was crammed, and the availability badge ("taking on new
work") was filler. Cut hard, including two devices that were mine rather than his:

- **Removed the status ticker** under the portrait. It was the page's one flourish,
  but it invented statuses ("queued", "compiling") that were never facts.
- **Removed the "By hand → Now" pair from every project card.** It was a good
  structural idea, but the left half was always my inference from the CV rather
  than something Samuele told me. Cutting it halves the text per card *and*
  removes the site's only unverified claims. Each card is now one sentence.
- Removed the seven hero skill pills (the services section already says this),
  the second CTA button, the per-card tech chips (the mono `kind` label in the
  card meta already carries that signal), and the explanatory paragraph under
  every section heading.
- Kept only result chips that carry a real number.
- Stats trimmed from five to four; dropped "13 years doing this" as filler.
- Cut the pharmacist origin line from About — Samuele had already excluded the
  pharmacy from scope, and it applied to the narrative too.
- Work heading went from "Every project below started as somebody's boring
  Tuesday" to the plain "What I've built, and who for." Cute framing is exactly
  what he was asking me to cut.
- Card list restyled from floating boxes to hairline-separated rows, which suits
  nine short entries better than nine cards did.
- Deleted the now-dead CSS (`.avail`, `.dot`, `.tag`, `.ticker`, `.flow`,
  `.chip`) rather than leaving it orphaned. Verified no class is used without a
  rule and no rule is unused.

`index.html` went from 31,375 to 19,548 bytes — about 38% less page.

## 2026-08-21 — Session 1 (cont.): actually matching the reference, plus real logos

Samuele: "I asked you to replicate this design, but it's actually completely
different." Correct. Session 1 took the reference's *structure* but deliberately
swapped its palette for a cool grey/cobalt scheme, on the reasoning that a
control-panel look suited an automation specialist. That reasoning was mine, not
his brief. He asked twice for the reference design, so the divergence was wrong.

Rather than work from a prose description again (the original mistake — the first
WebFetch returned "off-white with warm yellow accents", which is what produced
the wrong palette), this pass drove a real browser to sebastian-wittig.design and
read the computed styles off the live DOM:

- cream `#F5EFDF` ground, white `#FFFFFF` for one alternating section
- brown `#4B3E39` text, dark brown `#30231E` for buttons and the contact block
- yellow `#E9CB55` accent (the reference paints the second half of its rotating
  H1 in it — "I DESIGN FOR **FINANCE**")
- Inter everywhere; Merriweather only for quotes; 9999px pill buttons; 12px cards
- section labels are small 16px uppercase Inter 500, NOT big headlines; item
  titles are 32px Inter 600. That inversion is most of why the reference reads
  the way it does, and the earlier build had it backwards.

Committed to a single light theme like the reference, painting every colour
explicitly so the page still holds on a dark host background.

### Client logos
Found each company's real site by search, then pulled its mark. Three treatments,
because the source files are not alike:
- `hypefury`, `grillpark`, `italianindie` were black-on-white with no alpha. A
  script makes near-neutral bright pixels transparent using a soft ramp
  (210–245) so the type keeps its antialiasing instead of jagging.
- `financer`, `fbisol` ship as white-on-transparent SVGs — invisible on cream
  under grayscale, so they get `brightness(0)`. Both are plain wordmarks, so a
  silhouette loses nothing.
- the rest are coloured artwork and get `grayscale(1)`, which preserves internal
  detail that a flat silhouette would erase.

### Two things caught only by rendering it
- `.nav a` (specificity 0,1,1) was beating `.pill` (0,1,0), so the header
  button's label rendered brown-on-brown and was unreadable. Exactly the
  cascade collision to watch for. Fixed with `.nav a.pill`.
- SOS Automazioni and Italian Indie are Samuele's own ventures, not clients.
  They were sitting in a wall captioned "Clients I build for". Removed from the
  wall (eight real clients now fill a 4×2 grid) and kept in Work under "My own".

Also replaced the hero's `blur(250px)` layer with equivalent gradients — at that
radius Chromium promotes it to a very large composited layer for no visual gain.

### Still open
- `Dream Travel Agency` and `Bmark` were matched by search, not confirmed by
  Samuele. dreamtravelagency.it fits (it runs enrolment-based student trips,
  which matches the CV's "customer enrolments"), and bmark.it is a marketing
  agency, which fits the Facebook Ads work — but both need his confirmation
  that they are the right companies.
- Using client logos is normal for a portfolio but is their trademark; worth a
  quick heads-up to each before the site goes public.
