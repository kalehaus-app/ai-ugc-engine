# ai-ugc-engine

A small three-agent workflow for AI UGC ads, run with Claude Code. HeyGen and
Higgsfield make the videos. You approve every step that costs money or goes public.

```
brand/brief.md ──► [Spy] ──► research/ ──(you pick 10 hooks)──► [Design] ──► scripts/
                     ▲                                  (you pick 5 → 3) ──► creatives/
                     │                                                         │
                     │                                     you launch in Ads Manager
                     │                                                         ▼
               learnings/latest.md ◄── [Optimizer] ◄── reports/ ◄── results/ (CSV export)
```

The agents communicate only through the files in this repo. Each agent is a skill in
`.claude/skills/`:

| Agent | Run it by saying | Reads | Writes |
|---|---|---|---|
| Spy | "run the spy agent" | `brand/brief.md`, `learnings/latest.md` | `research/ads.csv`, `research/hooks.md` |
| Design | "run the design agent" | brief, approved hooks | `scripts/`, `creatives/manifest.csv` |
| Optimizer | "run the optimizer" | `results/*.csv`, `creatives/manifest.csv` | `reports/`, `learnings/latest.md` |

## Rules

- Nothing is published and no ad budget is set by Claude. You launch ads yourself.
- No HeyGen or Higgsfield credits are spent until you approve a cost estimate.
- Competitor ads are used for patterns only. Scripts are written fresh, with no copied
  wording, actors, or branding.

## MVP goal

Research competitors → 10 hooks → 5 scripts → 3 test creatives → manual launch →
review the results after about 3 days.
