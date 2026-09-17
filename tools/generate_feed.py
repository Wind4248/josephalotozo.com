#!/usr/bin/env python3
"""Regenerate blog/feed.xml from the posts listed in blog/index.html.

Run from the repo root after publishing a new post:
    python3 tools/generate_feed.py

Source of truth is blog/index.html — a post only reaches the feed once it is
listed there, which keeps the feed, the listing page and the sitemap in step.
"""
import html
import os
import re
from datetime import datetime, timezone
from email.utils import format_datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://josephalotozo.com/"


def main():
    os.chdir(ROOT)
    listing = open("blog/index.html").read()
    posts = re.findall(r'href="([a-z0-9-]+\.html)"(?:.*?)post-date">([^&<]+)&nbsp;', listing, re.S)
    if not posts:
        raise SystemExit("No posts found in blog/index.html — did the markup change?")

    items = []
    for filename, date_text in posts:
        page = open(os.path.join("blog", filename)).read()

        def meta(pattern):
            found = re.search(pattern, page)
            if not found:
                raise SystemExit(f"{filename}: missing required tag for {pattern}")
            return html.unescape(found.group(1))

        title = meta(r'<meta property="og:title" content="([^"]*)"')
        description = meta(r'<meta name="description" content="([^"]*)"')
        image = meta(r'<meta property="og:image" content="([^"]*)"')
        published = datetime.strptime(date_text.strip(), "%B %d, %Y").replace(
            hour=12, tzinfo=timezone.utc
        )
        url = SITE + "blog/" + filename

        local_image = image.replace(SITE, "")
        length = os.path.getsize(local_image) if os.path.exists(local_image) else 0
        mime = "image/png" if image.endswith(".png") else "image/jpeg"

        items.append(
            f"""    <item>
      <title>{html.escape(title)}</title>
      <link>{url}</link>
      <guid isPermaLink="true">{url}</guid>
      <pubDate>{format_datetime(published)}</pubDate>
      <description>{html.escape(description)}</description>
      <enclosure url="{image}" type="{mime}" length="{length}" />
    </item>"""
        )

    feed = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Joseph A. Lotozo — Blog</title>
    <link>{SITE}blog/</link>
    <atom:link href="{SITE}blog/feed.xml" rel="self" type="application/rss+xml" />
    <description>Building things with AI, community notes, family trips, and life in Upper Arlington, Ohio.</description>
    <language>en-us</language>
    <copyright>Copyright {datetime.now().year} Joseph A. Lotozo</copyright>
    <lastBuildDate>{format_datetime(datetime.now(timezone.utc))}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
    open("blog/feed.xml", "w").write(feed)
    print(f"blog/feed.xml regenerated with {len(items)} items")


if __name__ == "__main__":
    main()
