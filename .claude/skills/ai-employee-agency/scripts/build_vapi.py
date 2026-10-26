#!/usr/bin/env python3
"""Build a Vapi assistant JSON from a receptionist system prompt.

Paste the output into the Vapi dashboard, or POST it to https://api.vapi.ai/assistant
with an "Authorization: Bearer $VAPI_API_KEY" header. Field names follow Vapi's
assistant schema. If the dashboard rejects a field, check https://docs.vapi.ai/api-reference
because provider and model names change over time.
"""
import argparse
import json

DEFAULTS = {
    "model_provider": "openai",
    "model": "gpt-4o",
    "voice_provider": "11labs",
    "voice_id": "burt",
    "transcriber_provider": "deepgram",
    "transcriber_model": "nova-2",
}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--business", required=True)
    ap.add_argument("--prompt", required=True, help="path to system-prompt.md")
    ap.add_argument("--first-message", required=True, help="the greeting the assistant speaks first")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model-provider", default=DEFAULTS["model_provider"])
    ap.add_argument("--model", default=DEFAULTS["model"])
    ap.add_argument("--voice-provider", default=DEFAULTS["voice_provider"])
    ap.add_argument("--voice-id", default=DEFAULTS["voice_id"])
    ap.add_argument("--max-duration-seconds", type=int, default=600)
    args = ap.parse_args()

    with open(args.prompt) as fh:
        system_prompt = fh.read().strip()
    if "{{" in system_prompt:
        raise SystemExit("system prompt still has unfilled {{placeholders}}; fill them in or remove them first")

    assistant = {
        "name": f"{args.business} Receptionist"[:40],
        "firstMessage": args.first_message,
        "model": {
            "provider": args.model_provider,
            "model": args.model,
            "temperature": 0.3,
            "messages": [{"role": "system", "content": system_prompt}],
        },
        "voice": {"provider": args.voice_provider, "voiceId": args.voice_id},
        "transcriber": {
            "provider": DEFAULTS["transcriber_provider"],
            "model": DEFAULTS["transcriber_model"],
            "language": "en",
        },
        "endCallMessage": "Thanks for calling. Have a great day!",
        "endCallPhrases": ["goodbye", "bye", "that's all"],
        "maxDurationSeconds": args.max_duration_seconds,
        "analysisPlan": {
            "summaryPlan": {"enabled": True},
            "structuredDataPlan": {
                "enabled": True,
                "schema": {
                    "type": "object",
                    "properties": {
                        "caller_name": {"type": "string"},
                        "callback_number": {"type": "string"},
                        "service_address": {"type": "string"},
                        "service_needed": {"type": "string"},
                        "preferred_time": {"type": "string"},
                        "is_emergency": {"type": "boolean"},
                    },
                },
            },
        },
    }
    with open(args.out, "w") as fh:
        json.dump(assistant, fh, indent=2)
        fh.write("\n")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
