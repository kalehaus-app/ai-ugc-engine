# Brand brief

Every agent reads this file first. A field marked TODO means the agents stop and ask
before guessing.

## Product
- Name: bio.bar
- Website: https://biobar.ai
- What it is, in one sentence: A link-in-bio page that works like a one-page
  storefront. A business's services, prices, reviews, and booking/contact sit on one
  mobile page instead of a messy list of links.
- Price / offer: Free to start. Pro $6.99/mo, Premium $11.99/mo.
- Product images or logo available: TODO (needed before rendering. Screen recordings
  of a real bio.bar page are the most useful.)
- Existing UGC style reference: @biobar.you

## Customer
- Who buys it: Solo operators and small service businesses, such as coaches,
  designers, skincare and fitness pros, and small brands. **Target business owners,
  not influencers/creators.** Power users lean small business.
- The problem: Their Instagram/TikTok bio sends people to a cluttered list of links.
  Ready-to-buy visitors don't have one clear place to see services, prices, proof,
  and how to book.
- Why they hesitate: TODO (assumed: "my Linktree works fine", switching effort, yet
  another subscription. Confirm when possible.)

## Proof and limits
- Claims we CAN make:
  - Free to start. Pro $6.99/mo, Premium $11.99/mo.
  - Puts services, prices, reviews, and booking/contact on one mobile page.
  - Visitors get one clear place to go from the bio link.
- Claims we must NOT make:
  - No AI / "smart" / optimization claims. GEO, auto-testing, sign-up optimization,
    and ad ROI are "coming soon", so don't mention them.
  - Don't say bio.bar processes payments or sells for you. It sends visitors to
    wherever the business already sells or books.
  - Don't use the site's stats (3x sign-ups, 2.8x CTR, "88% of top creators see
    growth"). They are unverified mockup numbers.
  - No competitor names in ads until Dillon signs off.
  - No "guaranteed" growth, sales, or more clients.

## Competitors
Linktree, Beacons, Stan Store (priority), then Bento, Koji. Research only. They are
never named in our ads (see limits).

## Testing setup
- Platform: Meta (Facebook + Instagram) only, to start.
- Result we optimise for: Sign-up (Meta pixel must fire on sign-up; see Blockers).
- Test budget per round: $150 → 3 ads × ~$16–17/day × 3 days.
- Ad account ready: TODO (unknown. Check whether a Meta ad account exists for
  bio.bar.)

## Creative preferences
- Actor: Higgsfield AI influencer, matching the @biobar.you UGC style. The Design
  agent shows options before rendering.
- Tone: TODO (assumed: friendly, practical, small-business-owner talking to peers)
- Language(s): English

## Blockers before spending ad money
- [ ] Meta pixel fires a sign-up event (check in Meta Events Manager → Test events).
- [ ] Upgrade flow failing. Fine for a sign-up-optimised test, but paid conversions
      can't be measured until it's fixed.
- [ ] Sign-up and publish events aren't tracked in PostHog. We'll only see ad-level
      sign-ups in Meta, not what those users do afterwards.
- [ ] Meta ad account exists, with a payment method.
