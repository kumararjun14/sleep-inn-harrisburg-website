# Sleep Inn Harrisburg — hotel website concept

A responsive Flask concept for a hotel near Harrisburg and Hershey. I built its room browsing flow, image led page design, gallery, map, and booking and contact form demonstrations as part of my **Local Business Website & SEO Platform** project.

> Portfolio concept, not an official booking channel. Images are illustrative remote stock photos. Room dimensions, amenities, and descriptions in this draft must be verified with the hotel; no live inventory, rates, reviews, reservations, or contact delivery is available. The forms do not transmit or store personal information.

## Features

- Home, rooms, booking request demo, and location/contact pages with a shared Jinja layout.
- Responsive CSS, image gallery, mobile menu, reduced motion support, keyboard skip link and focus indicators.
- Page titles, meta description, Open Graph tags, optional canonical URLs and basic `Hotel` JSON-LD.
- Map embed and room selection flow using a URL query parameter. The selection does not check inventory.

## Run locally

Requires Python 3.10 or newer:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000. Tests: `python -m unittest discover -s tests -v`. Set `SITE_URL` to the eventual public origin to output canonical URLs. A `.env.example` lists configuration names, but this minimal app reads environment variables directly; export them before starting or use a process manager.

## SEO and customer journey

| Element | Location | Intent |
| --- | --- | --- |
| Room overview | `/rooms` | Help visitors compare room styles |
| Page titles and descriptions | `app.py`, `templates/base.html` | Describe the page in search previews |
| Canonical URLs | `SITE_URL` | Indicate the public page address |
| Hotel schema | `templates/base.html` | Provide basic structured business identity |
| Gallery and map | Home and contact pages | Orient visitors to the stay and location |

Technical SEO and calls to action are implemented as a prototype. There are no analytics or ranking results here. Before any official launch, obtain approved room facts, actual hotel images, verified address and contact information, permission to use the name/brand, a real reservation provider, and analytics/Search Console measurement. GitHub Pages cannot host a Flask server on its own.

## Code map

- `app.py`: hotel content and four Flask routes.
- `templates/`: shared layout and page views.
- `static/css/styles.css`: responsive layout and motion.
- `static/js/main.js`: menu and section reveal behavior.
- `tests/`: route and demo submission checks.
