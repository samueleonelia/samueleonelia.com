# Automation catalogue — private client map

PRIVATE. Not published (only the `publish` folder in netlify.toml is served).
The public page shows no client names: every entry in `AUTOMATIONS` in
`v2/index.html` has an empty last field (`client`). To show a client in an
entry's details window, put the name in that field. Decide per client.

Written 2026-10-12 from a read-only survey of the active workflows (trigger +
apps used). Descriptions are Claude's wording: check them.

| Client (internal) | Entry ids |
|---|---|
| Alessandro Bisol | deal-sync, invoice-match, sales-sync, course-reminder, customer-status, company-import, year-rollover |
| Daniele Rosini | wa-agent, web-agent, paper-research, paper-digest, linkedin-agent, market-report |
| Fabio Dal Zotto | ad-contract, form-analysis, deal-analysis |
| Marco Pisano | wa-order, email-order, order-check, order-notify, catalogue-sync |
| Nicola Zamorani | wa-router, survey, unhappy-guest, reply-classify, guest-thanks, booking-sync, guest-contact, peak-spread, shift-poll, staff-callin, staff-calc, missed-call |
| Salvatore Amato | maps-leads |
| Vincenzo Altomare | enrol-close, email-archive, deal-stage, postcode, enrolment, discount, booking-export, receipt, instalments, trip-list, flight-cost, teacher-proposal |
| SOS Automazioni (own instance) | site-videos, calendar-sync, yt-short, ig-reel, ig-comment-dm, site-forms, idea-backlog, payment-reminder |
| Every instance | backup, error-alert |

Left out on purpose: test/copy/temporary workflows, "Verifica Gmail",
"Cooperto Popup" (purpose unclear from its nodes), sandbox/learning flows.
