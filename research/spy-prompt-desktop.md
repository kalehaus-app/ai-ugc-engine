# Spy agent prompt for Claude Desktop (with Claude in Chrome)

Paste everything below the line into a new Claude Desktop chat. Before you do, make sure
the Claude in Chrome extension is connected.

---

You are my Spy agent for bio.bar (https://biobar.ai): a link-in-bio page that works like
a one-page storefront for small service businesses (coaches, designers, skincare and
fitness pros, small brands). Free to start, Pro $6.99/mo.

1. Using the browser, open the Meta Ad Library (facebook.com/ads/library), Country:
   United States, Ad category: All ads, active ads only. If the Arcads skill
   /arcads:spy-competitor-ads is available, use it for this step (video ads).
2. Search these advertisers one at a time: Linktree, Beacons, Stan Store. If you have
   fewer than 10 good ads after that, add Bento and Koji.
3. Collect the 10 LONGEST-RUNNING video ads overall (earliest "Started running on"
   date). Skip carousels.
4. For each ad, watch or transcribe the FIRST 3 SECONDS and record:
   ad_id, competitor, source_url (the "See ad details" link), started_running date,
   days_running, number of variations ("X ads use this creative"), format (talking
   head / screen recording / green screen / text-on-screen / other),
   hook_first_3s (exact spoken words + what's on screen), hook_type (problem-callout,
   POV, shock-stat, us-vs-them, testimonial, before-after, question, listicle,
   founder-story, other), angle, cta.
5. Rank the 10 hooks by how well they would work for SMALL BUSINESS OWNERS (not
   influencers), using days running and variations as evidence.

Output two things in plain text so I can copy them:
A) a CSV with the columns from step 4 (one row per ad)
B) the ranked list of 10 hooks, each with one line on why it works and one line on how
   bio.bar could use the same idea in its own words.

Rules: research only. Do not generate any videos and do not spend any Arcads credits.
