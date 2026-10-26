# Benchmarks for the X-ray

These are the defaults for the calculator's inputs. Each one has a source and an honest note on how good that source is. Use them as a starting point, then adjust for the business with a stated reason. If you find a better or newer source while researching, use it and cite it.

When you cite these in an X-ray or proposal, name the source ("a 2016 Moneypenny study found…"). Don't present them as facts about this particular business.

## Missed-call rate (`missed_call_rate`)

| low | likely | high |
|---|---|---|
| 0.25 | 0.40 | 0.62 |

- **411 Locals study:** 62% of calls to the small businesses in the study weren't answered by a person (about 38% went to voicemail and about 24% got no answer at all). It covered 85 businesses across 58 industries over 30 days. It is widely cited, and the date is reported as 2016 or later. It's small and old, so use it as the *high* case, not as a fact. Sources: https://www.nextiva.com/blog/best-ai-receptionist-small-business.html, https://getaira.io/blog/missed-business-calls-statistics
- Adjust upward for one-person or two-person crews, trades whose staff are on job sites (roofing, HVAC, plumbing), no weekend hours, or reviews saying "couldn't reach them". Adjust downward if they already have a front desk, an answering service or online booking.

## Lost after a missed call (`lost_after_miss_rate`)

The share of missed callers who never connect: they don't leave a voicemail, or they do and nobody calls back in time.

| low | likely | high |
|---|---|---|
| 0.50 | 0.70 | 0.85 |

- **Moneypenny Small Business Call Report (2016):** 69% of callers who reached voicemail hung up without leaving a message. https://moneypenny.com/us/resources/news/small-business-call-report/
- The "85% won't call back" statistic shows up on many vendor pages, but there's no primary study behind it. Use it only as the high case, and don't quote it as a finding.
- For urgent services (leaks, no heat, lockouts, emergency dental), callers move on to the next result quickly, so lean toward the high end.

## New-lead share (`new_lead_share`)

The share of inbound calls that are new-customer opportunities, as opposed to existing customers, vendors or spam. There's no good public benchmark, so **always label this as an assumption**. Reasonable starting points are 0.3 / 0.5 / 0.7 for trades and 0.2 / 0.35 / 0.5 for practices with many existing patients.

## Close rate (`close_rate`)

The share of leads that become paid jobs. This is also an assumption unless the owner tells you. Starting points are 0.2 / 0.3 / 0.5 for quote-based trades and 0.4 / 0.6 / 0.8 for appointment businesses (salons, dental cleanings, clinics).

## Monthly inbound calls (`monthly_inbound_calls`)

You can't see this from outside, so say so in the caveats. Estimate it from demand signals:
- Review count is the best proxy. Many reviews means many customers, and many customers means many calls.
- Also consider the number of locations or trucks, whether they run Google Ads (a "Sponsored" listing) and seasonality.
- A one-truck shop with a few dozen reviews might get 60–150 calls a month. A busy multi-crew shop with several hundred reviews might get 300–800. These are assumptions: state them as such and make the range wide.

## Average job value (`avg_job_value`)

Research this per niche and per city every time. Cost guides from Angi, HomeAdvisor, Fixr or the business's own price pages are good sources, and `niches.md` lists what to search for. Cite the URL. Use the typical job for the *low* case (a repair, not a full replacement).

## AI recovery rate (`ai_recovery_rate`)

| low | likely | high |
|---|---|---|
| 0.3 | 0.5 | 0.7 |

An assumption: an AI receptionist answers every call, but not every caller books. Keep it below 1 and say so.

## Cost of a human receptionist (proposal comparison)

- **BLS Occupational Employment and Wage Statistics, Receptionists and Information Clerks (43-4171), May 2023:** mean hourly wage $17.59, or a mean annual wage of $36,590. Check https://www.bls.gov/oes/current/oes434171.htm for a newer release and for the state or metro area figure.
- Monthly wage is about the annual figure divided by 12, roughly $3,050 at the national mean. Add benefits and payroll taxes only with a source. The BLS Employer Costs for Employee Compensation release is a good one. Cover 24/7 only by pointing out that one person covers about 40 of the 168 hours in a week. Don't multiply to an invented "$8,000 a month" figure.
