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

## 2026-08-21 — Session 1 (cont.): cuts, and Work as a 3-column grid

Samuele's review, applied verbatim:

- **Cut the "Most businesses don't need more software…" pull quote.** His word for
  it was "bullshit". It was my line, not his, and it was doing consultant-speak
  work rather than saying anything.
- **Cut "English and Italian, from Padova, for clients across Europe and the US."**
  Marked irrelevant. The footer and contact block already carry the location.
- **Cut the stats table under About** ("doesn't make any sense"). It was right:
  those four numbers came from two specific engagements (Hypefury, SOS
  Automazioni) but were presented as if they described his practice as a whole.
  Nothing is lost — 40,000 / ~40% still sit on the Hypefury card, and the
  19,000 / 200+ figures are in the SOS card's copy.
- **Then: cut the entire About section, and the "Clients I build for" logo wall.**
  The wall was redundant once every project card carries its own client logo,
  and dropping it removed the awkward SOS-Automazioni-in-a-client-wall problem
  for good.
- **Work rebuilt as a 3-column card grid, dates removed, ordered by length of
  engagement**: SOS Automazioni (2013) → Hypefury (2022) → Financer.com (2022–25)
  → the 2025 cohort → F. Bisol (2026). Nine cards fill three rows exactly.

Page is now hero → work → services → contact. `index.html` is 16.9 KB, down from
22.5 KB. Removed the CSS the deleted sections owned (`.clients`, `.logo-wall`,
`.logo-cell`, `.prose`, `.split`, `.stats`, `.quote`) and dropped Merriweather
from the font request, since the pull quote was its only consumer — verified
afterwards that no class is used without a rule and no rule is unused.

Worth flagging: ordering by engagement length puts SOS Automazioni — his own
company — in the first card, ahead of Hypefury, his biggest-name client. That is
what was asked for, but it is the weaker opening for selling.

## 2026-08-21 — Session 1 (cont.): client name becomes the yellow pill

- Removed the yellow stat pills from the work cards (they only appeared on two
  of nine, which read as inconsistent).
- The client name now *is* the yellow pill, sitting top-right of each card with
  the logo top-left. Kept it marked up as `<h3>` rather than a `<span>` so each
  card still has a real heading for screen readers and search engines — only its
  styling changed.
- Narrowed the card logo to 96px max width and set the pill to `nowrap` so the
  two never collide inside a 3-up column. Verified across all nine cards at
  1400px: every pill sits right of its logo, flush to the card's right edge, no
  overflow.

Note: screenshot capture stopped responding in the browser tooling partway
through this pass, so the last checks were done by measuring the rendered
geometry rather than by looking at an image.

## 2026-08-21 — Session 1 (cont.): Dream Travel logo fix

Samuele reported the Dream Travel logo missing. It was: measuring the rendered
geometry showed it at **0x0** while every other logo had a real size.

Cause: `dreamtravel.svg` declares only a `viewBox`, no `width`/`height`. Without
intrinsic dimensions it collapses to zero as a flex item under `width:auto`.
`financer.svg` and `fbisol.svg` both carry explicit width/height, which is why
they were unaffected. Fixed by writing `width="294.63" height="238.57"` onto the
SVG root, taken from its own viewBox.

Second, related problem: the card logo cap was 26px tall / 96px wide, which suits
wide wordmarks but crushes the squarish illustrated marks — Dream Travel is a
detailed 21-path drawing that turns to mush at 32px across. Added a `.tall`
modifier (44px tall, 88px wide, slightly higher opacity) for Dream Travel, Grill
Park, Acarent and SOS Automazioni, and raised the logo row to 44px to fit it.

Verified all nine render with real dimensions and clear the name pill.

## 2026-08-21 — Session 1 (cont.): project list rebuilt as the reference's big-type list

Samuele: use the design from the reference's About area for the project list.

`.section-about` itself turned out to be a scroll-driven video stage with a
sticky canvas, a rotating badge and a giant yellow circle — not a list at all.
The list design in that part of the page is the **history / customers** pattern,
and that is what was replicated:

- `.hist-row` items, 156px tall, stacked in a plain `flex-direction: column`
- item name as an **h3 at 64px, weight 600**, in brown `#4B3E39`
- one small 16px line underneath (the reference uses it for the employer; here
  it carries the project description)
- **no borders between rows** — the reference separates purely by rhythm

Applied to the nine projects, replacing the 3-column card grid. The client logo
moved to the right of each row.

Two deliberate departures, both worth reverting if he disagrees:
- **Kept a very faint hairline between rows** (`box-shadow: 0 -1px 0` at 8%
  alpha). The reference's rows carry a name plus one short line and are airy;
  ours carry 2–4 line descriptions, and with nine of them pure spacing muddles
  where one project ends and the next begins.
- **Dropped the yellow name pill.** The client name is now a 64px headline, so a
  pill repeating the same name directly above it was pure duplication.

`.tall` logos get 64px here (up from 44px) since the rows are much taller.
