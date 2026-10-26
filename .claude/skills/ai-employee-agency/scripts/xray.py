#!/usr/bin/env python3
"""Revenue X-ray calculator: estimates monthly revenue lost to missed calls.

Input JSON (each factor is {"low", "likely", "high", "source"}):

{
  "business": "Eastman Roofing",
  "monthly_price": 2000,                 # what Kale Haus charges per month (optional)
  "inputs": {
    "monthly_inbound_calls": {...},      # calls per month
    "missed_call_rate":      {...},      # 0-1, share of calls not answered live
    "lost_after_miss_rate":  {...},      # 0-1, missed callers who never reach them (no voicemail, no callback)
    "new_lead_share":        {...},      # 0-1, calls that are new-customer opportunities
    "close_rate":            {...},      # 0-1, leads that become paid jobs
    "avg_job_value":         {...},      # dollars per job
    "ai_recovery_rate":      {...}       # 0-1, share of lost leads an AI receptionist recovers
  }
}

Lost revenue = calls x missed x lost_after_miss x new_lead_share x close_rate x avg_job_value.
"likely" multiplies the likely values. "low" and "high" are the 10th and 90th percentiles of a
seeded simulation that draws each input from a triangular (low, likely, high) distribution.
That gives a realistic band instead of multiplying every worst case together. The output is
reproducible: the same inputs always give the same numbers.
"""
import argparse
import json
import math
import random
import sys

CHAIN = [
    "monthly_inbound_calls",
    "missed_call_rate",
    "lost_after_miss_rate",
    "new_lead_share",
    "close_rate",
    "avg_job_value",
]
RATES = {"missed_call_rate", "lost_after_miss_rate", "new_lead_share", "close_rate", "ai_recovery_rate"}
LEVELS = ("low", "likely", "high")


def validate(inputs):
    errors = []
    for key in CHAIN + ["ai_recovery_rate"]:
        f = inputs.get(key)
        if not isinstance(f, dict):
            errors.append(f"missing input: {key}")
            continue
        if not str(f.get("source", "")).strip():
            errors.append(f"{key}: every input needs a 'source' (a URL, a fact found, or 'assumption: why')")
        vals = []
        for lvl in LEVELS:
            v = f.get(lvl)
            if not isinstance(v, (int, float)) or v < 0:
                errors.append(f"{key}.{lvl} must be a non-negative number")
                continue
            if key in RATES and v > 1:
                errors.append(f"{key}.{lvl} is a rate and must be between 0 and 1 (got {v})")
            vals.append(v)
        if len(vals) == 3 and not (vals[0] <= vals[1] <= vals[2]):
            errors.append(f"{key}: need low <= likely <= high")
    return errors


def round_money(x):
    # Round to 2 significant figures so estimates don't look falsely precise.
    if x <= 0:
        return 0
    digits = int(math.floor(math.log10(x)))
    step = 10 ** max(digits - 1, 0)
    return int(round(x / step) * step)


def draw(rng, f):
    if f["low"] == f["high"]:
        return f["likely"]
    return rng.triangular(f["low"], f["high"], f["likely"])


def simulate(inputs, n=20000, seed=7):
    rng = random.Random(seed)
    jobs, lost, rec = [], [], []
    for _ in range(n):
        j = 1.0
        for key in CHAIN[:-1]:
            j *= draw(rng, inputs[key])
        l = j * draw(rng, inputs["avg_job_value"])
        jobs.append(j)
        lost.append(l)
        rec.append(l * draw(rng, inputs["ai_recovery_rate"]))
    pct = lambda xs, q: sorted(xs)[int(q * (len(xs) - 1))]
    return {name: (pct(xs, 0.10), pct(xs, 0.90)) for name, xs in
            (("jobs", jobs), ("lost", lost), ("rec", rec))}


def run(data):
    inputs = data["inputs"]
    out = {"business": data.get("business", ""), "monthly": {}, "annual": {}, "recoverable_monthly": {},
           "lost_jobs_monthly": {}, "method": "likely = product of likely inputs; low/high = P10/P90 of simulation",
           "inputs": inputs}
    jobs = 1.0
    for key in CHAIN[:-1]:
        jobs *= inputs[key]["likely"]
    lost = jobs * inputs["avg_job_value"]["likely"]
    point = {"jobs": jobs, "lost": lost, "rec": lost * inputs["ai_recovery_rate"]["likely"]}
    band = simulate(inputs)
    for lvl, idx in (("low", 0), ("likely", None), ("high", 1)):
        val = (lambda k: point[k]) if idx is None else (lambda k: band[k][idx])
        out["lost_jobs_monthly"][lvl] = round(val("jobs"), 1)
        out["monthly"][lvl] = round_money(val("lost"))
        out["annual"][lvl] = round_money(val("lost") * 12)
        out["recoverable_monthly"][lvl] = round_money(val("rec"))
    price = data.get("monthly_price")
    if price:
        job = inputs["avg_job_value"]["likely"]
        out["monthly_price"] = price
        out["jobs_to_break_even"] = round(price / job, 2) if job else None
        low_rec = out["recoverable_monthly"]["low"]
        out["roi_multiple_at_low_recovery"] = round(low_rec / price, 1) if low_rec else 0
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="inputs JSON file")
    ap.add_argument("--out", help="where to write the result JSON (default: stdout)")
    args = ap.parse_args()
    with open(args.input) as fh:
        data = json.load(fh)
    errors = validate(data.get("inputs", {}))
    if errors:
        print("Input problems:\n  " + "\n  ".join(errors), file=sys.stderr)
        sys.exit(1)
    result = json.dumps(run(data), indent=2)
    if args.out:
        with open(args.out, "w") as fh:
            fh.write(result + "\n")
    print(result)


if __name__ == "__main__":
    main()
