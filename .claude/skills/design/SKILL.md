---
name: design
description: Design agent. Turns approved hooks into original UGC ad scripts, then (after cost approval) renders test creatives with HeyGen or Higgsfield. Use when the user says "run the design agent", "write scripts", or "make the creatives".
---

# Design agent

Turn approved hooks into original scripts, then into test videos. **Every render costs
credits, so nothing renders without the user's explicit yes on a cost estimate.**

## Before starting
Read `brand/brief.md`, the `APPROVED` hooks in `research/hooks.md`, and
`learnings/latest.md`. If there are no approved hooks, stop and say the Spy agent must
run first.

## Step 1: 5 scripts → scripts/NN-short-name.md
Each script contains:
- **Hook (0–3s):** spoken line + on-screen text + what we see
- **Body:** problem → product → proof. Use only claims listed in the brief.
- **CTA:** one clear action matching the brief's optimisation result
- **Actor spec:** age range, gender, setting, energy, wardrobe
- **Format:** 9:16, 15–30s, 40–80 spoken words, written to be said aloud
- **Source hook id:** which approved pattern it adapts

Rules: adapt the *mechanism* of the hook, never a competitor's wording, actor, or
brand. Make no claims missing from the brief's "can make" list.

**Checkpoint:** show all 5 and ask the user to approve or edit, then pick 3 to produce.

## Step 2: pick the tool per script
- Talking actor to camera (testimonial, founder, problem-callout): HeyGen
  `create_video_from_avatar` with a stock avatar or the user's digital twin. Browse
  with `list_avatar_groups` → `list_avatar_looks`.
- Stylised product / influencer-style / b-roll-heavy: Higgsfield Ads Studio or AI
  Influencer (call `ads_studio_quote` / `ai_influencer_prepare` for the price first).

**Checkpoint:** show the user the chosen actor(s) and a cost estimate for all 3
renders. Wait for an explicit yes.

## Step 3: render and QA
Render, poll until done, and save links/files under `creatives/`. QA every video:
lip-sync, hands and faces, readable on-screen text, correct product name, no
off-brief claims. A failed render gets at most one automatic retry, then report it.
Log each one in `creatives/manifest.csv` with `status` = rendered / failed / approved.

**Checkpoint:** the user approves the final 3. Then give the user step-by-step launch
instructions for Ads Manager: one ad set, equal budget per ad, ad names matching
`creative_id`. **Never publish or upload to an ad account yourself.**
