# josephalotozo.com

Personal website for Joseph A. Lotozo — Financial Advisor at Edward Jones, Upper Arlington, Ohio.

## Site Structure

```
/website/
  index.html          ← main site (single HTML file with inline CSS)
  favicon.svg         ← JL monogram, yellow (#FAD141) circle
  sitemap.xml
  CNAME               ← josephalotozo.com
  assets/             ← all images (headshot, team photos, community photos, etc.)
  blog/
    index.html        ← blog listing page
    ai-chamber-wrapped.html  ← first post: "I Have a Genie and His Name is Claude"
  tvcp-2025/          ← Chamber Wrapped presentation (separate project, hosted here)
```

## Hosting

- GitHub Pages via `Wind4248/josephalotozo.com` repo
- Custom domain: www.josephalotozo.com
- Push to `main` to deploy

## Design System

- **Colors:** Yellow `#FAD141`, Black `#1A1A1A`, White `#FFFFFF`, Light Gray `#F7F7F7`, Text Gray `#555555`
- **Fonts:** Georgia (body), Arial (headings, labels, nav)
- **Patterns:** `.section-white` / `.section-gray` alternating sections, `.section-inner` (860px max), `.section-rule` yellow bar under h2
- **Components:** `.cred-card` (credentials), `.list-card` (interests/community), `.photo-card` + `.photo-grid` (galleries), `.team-card` (bios), `.connect-card` (social links), `details/summary` (FAQ)
- All CSS is inline in `<style>` within the `<head>` of each HTML file (no external stylesheets)

## Content Rules

- **Edward Jones compliance:** No financial advice, no EJ product mentions, no client testimonials. Personal content only.
- The disclaimer banner ("The postings on this site are my own...") must appear on every page.
- Chamber/community involvement is personal/volunteer, not EJ business.

## Image Handling

- Resize photos to 1920px wide, JPEG quality ~82% using Pillow before adding to `assets/`
- Use `loading="lazy"` on all images except the hero headshot

## Key Sections (index.html order)

1. Nav (sticky, yellow bottom border)
2. Disclaimer banner
3. Hero (headshot + name + credentials)
4. About Joe
5. Professional Credentials (6 cards: CFP, ChFC, AAMS, CRPC, CRPS, MBA in-progress)
6. Community Involvement
7. A Little About Me (interests)
8. What I'm Reading (3 book cards)
9. Family Time (zoo photos)
10. In the Community (open house photos)
11. My Team (team photos + bios for Emma Reed & Bella Cloyd)
12. Published Author (AI Unmasked book)
13. Find Me Online (social links + Google searches)
14. FAQ (expandable details)
15. Footer

## About Joe

- Financial Advisor at Edward Jones, Tremont Center, Grandview Heights
- Lifelong Upper Arlington resident, Ohio State alum
- Past Chair of Tri-Village Chamber Partnership (2025)
- Currently pursuing MBA at OSU Fisher College of Business
- Wife + three daughters
- Interests: beekeeping, rugby, gardening, travel, reading, weightlifting, AI, sourdough, sewing
- Published author: *AI Unmasked* (2023, co-authored with ChatGPT-4)
