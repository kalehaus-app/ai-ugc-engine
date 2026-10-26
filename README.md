# ai-ugc-engine
## Skills

### `ai-employee-agency` (Kale Haus)
Lives in `.claude/skills/ai-employee-agency/`. It runs the "AI employee" agency playbook for small businesses:

1. **Leads**: real local businesses for a city and niche, scored by how much they're missing.
2. **X-ray**: estimated monthly revenue lost to missed calls, as a range with every input sourced (`scripts/xray.py`).
3. **AI employee**: a receptionist prompt plus a Vapi assistant JSON (`scripts/build_vapi.py`).
4. **Proposal**: a one-pager at your monthly price.
5. **Outreach**: a CAN-SPAM-compliant email, drafted only and never sent automatically.

Open Claude Code in this repo and ask something like *"find roofers in San Jose I can sell an AI receptionist to"*.
