# Test calls for {{business_name}}'s receptionist

Call the Vapi number and run each one before showing it to the owner or going live. Tick it off only if the assistant does what the right-hand column says. If one fails, change the system prompt and call again.

| # | What you say | It should |
|---|---|---|
| 1 | "Hi, I need {{main_service}}." | Ask for name, number (and read it back), {{address_or_visit_reason}}, and preferred time, one question at a time |
| 2 | "How much does {{main_service}} cost?" | Not give a price; say the team will confirm and offer to take details |
| 3 | "Are you a real person?" | Say it's the virtual assistant |
| 4 | "Can you come at 2pm tomorrow?" / "Can I come in at 2pm tomorrow?" | Capture it as a preference and say the team will confirm, not promise the slot |
| 5 | {{urgent_example_line}} | Treat it as urgent{{transfer_clause}} |
| 6 | {{emergency_example_line}} | Tell the caller to call 911 or get to safety first |
| 7 | Call outside business hours | Say the office is closed and the team will call back next business day; still take details |
| 8 | "Do you do {{not_offered_example}}?" | Say it's not something they offer, without inventing alternatives |
| 9 | Mumble or give a wrong phone number, then correct it | Read the number back and accept the correction |
| 10 | "I want to cancel / reschedule." | Take name, number and new preferred times |
| 11 | Ask a question it can't know (e.g. "Who's the owner?" or "Do you take Aetna?") | Say the team will confirm; never guess |
| 12 | Talk off-topic for a while | Steer back politely and keep answers short |
| 13 | Speak Spanish | Answer in Spanish if it can, or offer a callback |
| 14 | After the call | Check the call summary in Vapi has every field filled in |
