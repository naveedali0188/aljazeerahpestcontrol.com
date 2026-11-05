# Al Jazeerah Pest Control LLC — Website

Static, framework-free marketing site for **Al Jazeerah Pest Control LLC** (Dubai & Sharjah, UAE).
Rebuilt as a fast, accessible, bilingual (English / Arabic) single page that keeps the section
order and identity of the current live site.

- No build step, no dependencies, no backend required.
- Works from any static host (GitHub Pages, Cloudflare Pages, Netlify, cPanel…).

## Files

| Path | Purpose |
| --- | --- |
| `index.html` | The whole page: header, hero, quote form, services, stats, cleaning, testimonials, pests, sectors, FAQ, CTA, footer. Includes inline SVG icon sprite and JSON-LD. |
| `style.css` | Design system (colours, type, spacing), all section styles, responsive rules, RTL rules, reduced-motion handling. |
| `script.js` | English/Arabic i18n + RTL switching, mobile nav, FAQ accordion, form validation, counters, scroll reveal, sticky-header and active-link state. |
| `assets/` | Company logo, approval logos, photography, favicon and self-hosted fonts (Poppins + Tajawal). |
| `robots.txt`, `sitemap.xml` | Crawling and sitemap, with `hreflang` alternates for the two languages. |
| `.github/workflows/deploy.yml` | GitHub Pages deployment (Actions). |

## Local preview

```bash
python -m http.server 8123
# open http://127.0.0.1:8123/
```

Arabic: <http://127.0.0.1:8123/?lang=ar>

## Language behaviour

- English is the default. The switcher stores the choice in `localStorage` and mirrors it in the
  URL (`?lang=ar`) so a link can be shared or indexed per language.
- Arabic switches `<html lang="ar" dir="rtl">`, the Tajawal font, all copy, image `alt` text and
  ARIA labels. Layout uses CSS logical properties, so columns, icons and arrows mirror correctly.

## Quote form

The site is static, so there is no server to receive submissions. The form validates on the client
and then hands the message to the visitor's own email app (`mailto:`) pre-filled with name, phone,
email, subject and message. The status line says exactly that and offers a WhatsApp fallback — the
site never claims a message was sent.

To make submissions server-side later, point the form at an endpoint (Formspree, a Worker, etc.)
and keep the existing validation.

## Deployment — GitHub Pages

This repository deploys to **https://aljazeerahpestcontrol.com/** through the included
workflow (`.github/workflows/deploy.yml`), with the custom domain kept in `CNAME`.
Every push to `main` publishes automatically.

The previous multilingual generated site is preserved on the
`backup/legacy-multilingual-site` branch. Old `/en/` and `/ar/` links redirect to the new
page; `/zh/` and `/ru/` pages are intentionally gone because the site now supports exactly
English and Arabic.

To deploy from scratch:

1. Create an empty repository on GitHub.
2. Push this folder:

   ```bash
   git init -b main
   git add .
   git commit -m "Redesign: bilingual Al Jazeerah Pest Control website"
   git remote add origin https://github.com/<account>/<repo>.git
   git push -u origin main
   ```

3. In the repository: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
4. The included workflow publishes on every push to `main`. The URL appears in the Actions run
   summary and under Settings → Pages. If you use a custom domain, keep the `CNAME` file and set
   the domain under Settings → Pages.

If you prefer not to use Actions, delete `.github/workflows/deploy.yml` and choose
**Deploy from a branch → main → / (root)** instead.

## Content and claims

- Copy is limited to services, offices and contact details published on the existing site.
- Statistics are counts of what the site actually lists (2 offices, 10 pest types, 4 cleaning
  services, 3 emirates served) — no invented years of experience, customer counts or ratings.
- Municipality and NPMA logos are reused from the existing site as supplied company assets.
- Only the existing social profiles (Facebook, Instagram, LinkedIn) and the supplied Google Maps
  link are used.
- The testimonial shown is the one published on the existing site.

## Live

- Homepage (English): <https://aljazeerahpestcontrol.com/>
- Arabic: <https://aljazeerahpestcontrol.com/?lang=ar>
- 404: <https://aljazeerahpestcontrol.com/404.html>

## Verified

- All images, fonts and CSS/JS load with HTTP 200; no broken assets.
- No horizontal overflow at 1440, 1024, 820, 500 and 390 px, in both languages.
- Language switch, mobile menu (open/Escape/scroll-lock), FAQ accordion, counters, form validation
  and the mailto hand-off were exercised in Chromium.
- One `h1` per page, no skipped heading levels, labelled form fields, visible focus styles.
- `prefers-reduced-motion` disables entrance animation and counters land on their final values.
