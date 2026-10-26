---
name: ai-employee-agency
description: Runs the "AI employee" agency playbook for Kale Haus. Finds local small businesses in a city and niche, runs an "X-ray" on each that estimates revenue lost to missed calls and slow follow-up (with stated, sourced assumptions), builds a Vapi-ready AI receptionist for the chosen business, writes a custom proposal at the user's monthly price, and drafts the outreach email for the user to review. Use this whenever the user wants to find businesses to sell AI receptionists, AI employees or voice agents to; mentions leads in a city ("roofers in San Jose", "dentists in Austin"); asks how much a business is losing to missed calls; wants a receptionist or voice agent set up for a specific business; or wants a proposal or cold email for an AI service, even if they never say "agency" or "X-ray".
---

# AI Employee Agency (Kale Haus)

This skill helps the user, who sells under the **Kale Haus** brand, become the middleman between local businesses and AI. It runs a five-stage pipeline:

1. **Leads**: find businesses in a city and niche, scored by how much an AI receptionist would help them.
2. **X-ray**: estimate what one business loses each month to missed calls and slow follow-up.
3. **AI employee**: build a receptionist for that business that is ready to load into Vapi.
4. **Proposal**: write a one-page proposal at the user's price.
5. **Outreach**: draft the email to the owner. **Never send it.**

The user can enter at any stage. For example, "X-ray this business: <url>" starts at stage 2. Ask only for what's missing. If no city is given, ask for one. If no niche is given, suggest three of the highest-value niches from `references/niches.md` and let the user pick.

## Why honesty is the product

The pitch only works if the owner believes the numbers. An inflated "you're losing $38,000 a month" that the owner can disprove from their own books kills the deal and the user's reputation. So:

- Every dollar figure is an **estimate shown as a range** (low / likely / high), and every input behind it is listed with where it came from.
- Inputs come from (a) facts about this business that you actually found, (b) the published benchmarks in `references/benchmarks.md` with their sources, or (c) clearly labeled assumptions. Never present an assumption as a fact about the business.
- Never invent reviews, call counts, ratings, owner names or emails. If you couldn't find something, write "not found" and move on.
- The receptionist always discloses that it's an AI assistant if asked, and never claims to be a person.

## Output folder

Put everything for a run in `kale-haus-leads/<city>-<niche>/` in the current working directory, unless the user says otherwise:

```
kale-haus-leads/san-jose-roofing/
├── leads.csv                      # stage 1
├── leads.md                       # stage 1, readable version
└── <business-slug>/
    ├── xray.md                    # stage 2
    ├── xray.json                  # stage 2, script output
    ├── receptionist/
    │   ├── system-prompt.md       # stage 3
    │   └── vapi-assistant.json    # stage 3
    ├── proposal.md                # stage 4
    └── outreach-email.md          # stage 5
```

## Stage 1: Leads

Use web search (and web fetch on listing pages) to find 10–20 real businesses of that niche in that city: Google Maps and Yelp listings, Angi or HomeAdvisor for trades, and the businesses' own sites. For each one, record what you can verify:

`name, website, phone, address, rating, review_count, hours, has_online_booking, has_chat_or_ai, after_hours_coverage, missed_call_signals, source_urls`

`missed_call_signals` are things like reviews that say "never called back", "went to voicemail" or "couldn't reach anyone"; hours that end at 5pm with no weekend cover; a "call for a quote" site with no booking form; or a single phone number for a one-person crew. Quote the review text and link it. These signals are the strongest part of the pitch.

Score each lead from 1 to 10 for *opportunity* (lots of inbound demand plus visible signs of missed calls) and explain the score in one line. Ratings are a good proxy for demand: many reviews means many customers calling. Sort by score, then write `leads.csv` and `leads.md`. Show the user the top five in a short table and ask which ones to X-ray. If they say "all" or "the top 3", do that.

Skip chains and franchises with corporate call centers. They don't buy from a local agency.

## Stage 2: X-ray

For the chosen business, dig deeper: fetch the website, read the most recent reviews, and check hours, booking options and whether a chat widget or AI answering service is already in place.

Then build the inputs for the calculator. Read `references/benchmarks.md` for the defaults and their sources, and `references/niches.md` for job values by niche. Adjust each input to this business with a stated reason. For example, a shop with 900 reviews gets more calls than one with 40, and a crew with no weekend hours misses more.

Run the calculator. It does the math so the numbers are consistent and reproducible:

```bash
python3 <skill-dir>/scripts/xray.py --input inputs.json --out <business-dir>/xray.json
```

The input format is documented at the top of `scripts/xray.py`. Each input takes `low`, `likely`, `high` and a `source` string. The script returns monthly and annual lost revenue. "Likely" is the product of the likely inputs. "Low" and "high" are the 10th and 90th percentiles of a seeded simulation, which gives a realistic band instead of multiplying every worst case together. It also returns the break-even point at the user's price. Don't do this math by hand: it keeps every X-ray consistent.

Write `xray.md` using this structure:

```markdown
# Revenue X-ray: <Business name>
Prepared by Kale Haus · <date>

## The short version
<One or two sentences: "We estimate <name> is missing about $X–$Y a month in booked work, most likely around $Z, mainly from <top reason>.">

## What we found
- <verified fact, with link>
- <review quote showing a missed call, with link>

## How we estimated it
| Input | Low | Likely | High | Where it comes from |
|---|---|---|---|---|
...

## What an AI receptionist changes
<Answers 24/7, books or captures every lead, texts back missed calls. Recovered revenue range, and how many recovered jobs a month pay for the service.>

## Caveats
<What we couldn't see, for example their real call volume. "Your phone records will tell you the real number: we're happy to check them with you.">
```

When you tell the user the headline number, use the *likely* figure and give the range alongside it.

## Stage 3: AI employee (Vapi receptionist)

Build a receptionist tailored to this business from what you found: services, service area, hours, how quotes and emergencies work, and the questions customers ask in reviews. Start from `assets/receptionist-prompt.md` and fill in every `{{placeholder}}`. If you don't know a fact (prices, for example), the receptionist captures the details and promises a callback. It never makes up an answer.

Then run:

```bash
python3 <skill-dir>/scripts/build_vapi.py --business "<name>" --prompt <business-dir>/receptionist/system-prompt.md --first-message "<greeting>" --out <business-dir>/receptionist/vapi-assistant.json
```

Defaults are listed in the script. Add `--voice-id` or `--model` if the user asks for them.

Tell the user how to test it: open the Vapi dashboard, go to **Assistants**, click **Create**, then paste the JSON or the prompt. Buy or attach a phone number, then call it. If a Vapi API key is available as `VAPI_API_KEY`, offer to create the assistant through the API, but only if the user says yes.

Compliance notes to pass on to the user (one line each, not a lecture):
- The greeting says calls may be recorded, because California and several other states require all parties to consent to recording.
- This is an **inbound** receptionist. Automated **outbound** calls or texts to consumers fall under TCPA rules, which is a separate question.

## Stage 4: Proposal

Ask for the monthly price if the user hasn't given one. The reel's example was $2,000 a month. Offer a setup fee as optional, and don't add one unless the user wants it. Fill in `assets/proposal-template.md`. The proposal reuses the X-ray's range. It compares the cost against the low end of recovered revenue (being conservative makes it more convincing) and against the cost of a human receptionist. For that cost, use the wage source in `references/benchmarks.md`, not a made-up "$8,000 a month".

## Stage 5: Outreach email (draft only)

Write `outreach-email.md` using `references/outreach.md`. It covers the structure, three subject lines, a follow-up, and the rules for US cold email (CAN-SPAM: honest subject, a physical address, an easy opt-out). Address it to the owner only if you found their name and email on a public source, and cite it. Otherwise leave `{{owner_email}}` for the user to fill in.

If a Gmail connector is available and the user asks, create a **draft** in Gmail. Never send. Sending is the user's decision, every time.

## Finishing a run

End with a short summary for the user: the leads file, each business X-rayed with its likely monthly figure and range, where the receptionist JSON is, and any facts you couldn't verify. Keep it to a few lines and point to the files.
