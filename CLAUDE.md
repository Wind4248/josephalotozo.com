# josephalotozo.com

Personal website for Joseph A. Lotozo — CFP® professional, Financial Advisor and Partner at Edward Jones, Upper Arlington, Ohio.

## Current State — September 17, 2026

Live and deployed (commits `54330a7`, `e0ce6fd`). Everything below is on `main` and public.

**Shipped today**
- Instagram featured as the primary social channel: `#instagram` section (`.section-dark`),
  nav link, footer row. Facebook now points at the personal profile
  (`facebook.com/jolotozo`) with the Edward Jones page listed separately; X moved to `x.com`;
  `sameAs` went from 2 profiles to 6.
- `BlogPosting` JSON-LD on all 12 posts; `og:image` added to the 6 that had none (new cards in
  `assets/og/`); OG/Twitter/`Blog` schema on the blog index.
- RSS at `blog/feed.xml` + `tools/generate_feed.py`; branded `404.html`.
- MS in Personal Financial Planning added as a credential card; What I'm Reading reworked
  into a running log.
- Two defects fixed: footer paragraphs were invisible (global `p` rule set `#333`, same as the
  footer background), and `assets/streamnchill-homescreen.png` was publishing named contacts
  with their photos in an iOS share sheet — the contact row was cut out.

**Uncommitted drafts (intentionally not published, not in index/sitemap/feed)**
- `blog/streamnchill-play-store.html` — "I Said You Wouldn't Need an App Store. Now I Need 12
  Testers." Written Sept 17. Framed around Play Store *search discoverability*, which is Joe's
  actual reason — not a reversal of the April "no App Store required" post. Held pending a
  decision; its images (`assets/streamnchill-store-icon.png`, `assets/og/og-streamnchill-play.jpg`)
  are also uncommitted.
- `blog/chamber-chair-lessons.html` — finished draft dated **July 2026**, still unpublished.
  Not written by this session. Needs a publish/redate/kill decision.

**Open**
- The six `.ig-grid` tiles are site photos standing in for real Instagram posts. Instagram
  blocks programmatic extraction, so swapping them needs Joe to export images by hand. No bee
  photo exists in `assets/` despite beekeeping being his most-posted subject.
- Joe's Instagram bio still links the EJ-hosted advisor site rather than josephalotozo.com.
- Several StreamNChill screenshots show the retired `watchlist-joelotozo.web.app` URL.
- `index.html` is ~1,400 lines and each social lives in three places (card, `sameAs`, FAQ),
  which is why the Facebook label drifted out of sync. A refactor was deferred, not rejected.
- `sitemap.xml` does not list `tvcp-2025/`.

## Site Structure

```
/website/
  index.html          ← main site (single HTML file with inline CSS)
  404.html            ← branded not-found page (GitHub Pages serves this automatically)
  favicon.svg         ← JL monogram, yellow (#FAD141) circle
  sitemap.xml
  CNAME               ← josephalotozo.com
  assets/             ← all images (headshot, team photos, community photos, etc.)
    og/               ← 1200×630 social share cards (generated, see "Social Sharing")
  blog/
    index.html        ← blog listing page (keep in sync with posts + sitemap.xml + feed.xml)
    feed.xml          ← RSS feed (GENERATED — never hand-edit, see "Social Sharing")
    *.html            ← 12+ posts (first: ai-chamber-wrapped.html "I Have a Genie and His Name is Claude")
  tools/
    generate_feed.py  ← regenerates blog/feed.xml from blog/index.html
  tvcp-2025/          ← Chamber Wrapped presentation (separate project, hosted here)
  wpmba/              ← WP MBA Student Council pages (incl. Dosa Rush spotlight)
  tom/                ← Tom's photo site pages
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
- `.section-dark` (black bg, yellow top/bottom border) is the **feature** treatment, used only
  for the Instagram block. It deliberately breaks the white/gray rhythm — don't reuse it
  casually or it stops reading as a feature.
- Instagram is Joe's primary social channel (`@jlotozo`). It gets a nav link, the
  `#instagram` feature section, and a footer link. The `.ig-grid` tiles are **site photos,
  not live Instagram posts** — the copy says "a few frames from around here" for that reason.
  If the tiles are ever swapped for real Instagram exports, keep the alt text accurate.

## Social Sharing & Structured Data

Every published blog post carries, in this order after `<link rel="canonical">`:
`og:type`, `og:title`, `og:description`, `og:url`, `og:image`, `og:site_name`,
`article:published_time`, `twitter:card` (always `summary_large_image`), `twitter:image`,
then a `BlogPosting` JSON-LD block immediately before `<style>`.

- **`og:image` is required on every post.** Use a real post photo when a landscape one
  exists; otherwise generate a 1200×630 card into `assets/og/` (blurred, darkened cover of
  the source image with the photo centered on top and an 8px yellow bar at the bottom).
  Portrait photos and phone screenshots must never be used as `og:image` directly — they
  crop badly in LinkedIn and Facebook previews.
- **After adding or removing a post:** update `blog/index.html`, then `sitemap.xml`, then run
  `python3 tools/generate_feed.py` from the repo root. The generator reads `blog/index.html`,
  so a post that isn't listed there won't reach the feed.
- Drafts stay out of `blog/index.html`, `sitemap.xml`, and the feed until published.

## Content Rules

- **Edward Jones compliance:** No financial advice, no EJ product mentions, no client testimonials. Personal content only.
- **Never link to the EJ-hosted advisor site** (`edwardjones.com/joseph-lotozo`). Joe's instruction, Sept 17 2026: this site stays personal and deliberately separate from the firm-hosted one. Do not add it to a link card, the footer, or schema `sameAs`.
- The disclaimer banner ("The postings on this site are my own...") must appear on every page.
- Chamber/community involvement is personal/volunteer, not EJ business.

## Image Handling

- Resize photos to 1920px wide, JPEG quality ~82% using Pillow before adding to `assets/`
- Use `loading="lazy"` on all images except the hero headshot

## Key Sections (index.html order)

1. Nav (sticky, yellow bottom border — Blog, Instagram, Find Me Online)
2. Disclaimer banner
3. Hero (headshot + name + credentials)
4. Start Here (4 orientation cards)
5. About Joe
6. Professional Background & Credentials (7 cards: CFP, ChFC, AAMS, CRPC, CRPS, MS, MBA in-progress)
7. Community Involvement
8. A Little About Me (interests)
9. **On Instagram** (featured `.section-dark` block)
10. What I'm Reading — running log: Reading Now / Recently Finished / Also On the Shelf, with a "Last updated" stamp. Move titles between groups rather than deleting them.
11. Family Time (zoo photos)
12. In the Community (open house photos)
13. My Team (team photos + bios for Emma Reed & Bella Cloyd)
14. Published Author (AI Unmasked book)
15. Projects I'm Building With AI
16. Find Me Online (social links + Google searches)
17. FAQ (expandable details)
18. Footer (contact, social row, CFP Board trademark notice)

## About Joe

- CFP® professional, Financial Advisor and Partner at Edward Jones, Tremont Center, Upper Arlington (the office is in Upper Arlington — NOT Grandview Heights)
- **CFP Board rule:** Always reference as "CERTIFIED FINANCIAL PLANNER™ professional" or "CFP® professional" when describing Joe
- Lifelong Upper Arlington resident, Ohio State alum
- Past Chair of Tri-Village Chamber Partnership (2025)
- Currently pursuing MBA at OSU Fisher College of Business
- Wife + three daughters
- Interests: beekeeping, rugby, gardening, travel, reading, weightlifting, AI, sourdough, sewing
- Published author: *AI Unmasked* (2023, co-authored with ChatGPT-4)
