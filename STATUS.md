# STATUS — samueleonelia.com

Phase: **deployed to a temporary URL, domain pending DNS** · Branch: `main` · Last updated: 2026-09-03

- Live: https://samueleonelia.netlify.app
- Repo: https://github.com/samueleonelia/samueleonelia.com (private)
- Netlify admin: https://app.netlify.com/projects/samueleonelia
- Mockup artifact: https://claude.ai/code/artifact/8112620f-a4ed-4353-b8c5-86e414ff3e64

Page structure: hero → work → thread → services → contact.
Local file is now `public/index.html`.

## Feature areas

| Area | State |
|---|---|
| Design matched to sebastian-wittig.design | Done |
| Hero (rotating two-tone headline) | Done |
| Work: 9 rows, name-only until hover | Done — dark hover, white knockout logos |
| Hypefury thread section | Done |
| Services | Done — 4 items |
| Contact + footer | Done |
| GitHub repo | Done — private |
| Netlify site + first deploy | Done |
| Publish dir isolates working files | Done — verified 404 live |
| Custom domain (Netlify side) | Done |
| **DNS at Hover** | **Blocked on Samuele** |
| **GitHub auto-deploy** | **Blocked — needs the Netlify UI** |
| Favicon | Not started |
| OG / social share image | Not started |

## Next

1. Samuele adds two DNS records at Hover (see below).
2. Samuele links the repo in the Netlify UI so pushes auto-deploy.
3. Favicon + OG image.
4. Confirm Dream Travel Agency and Bmark are the right companies.

## DNS records to add at Hover

| Type | Host | Value |
|---|---|---|
| A | @ | 75.2.60.5 |
| CNAME | www | samueleonelia.netlify.app |

No MX or TXT records exist on the domain, so nothing else is at risk.

## Known issues

- Dream Travel Agency and Bmark logos matched by web search, unconfirmed.
- Yannick Veys has not been told the X thread is going on the site.
- Deploys are manual until GitHub is linked: `netlify deploy --prod --dir public`.
- Not yet tested on a real phone or in Safari.
