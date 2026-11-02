#!/usr/bin/env bash
# Create a Vapi assistant from a JSON file built by build_vapi.py.
# Usage: VAPI_API_KEY=... ./create_assistant.sh path/to/vapi-assistant.json
# Get the key from the Vapi dashboard (Organization > API Keys, the private key).
set -euo pipefail

json="${1:?usage: VAPI_API_KEY=... $0 vapi-assistant.json}"
: "${VAPI_API_KEY:?set VAPI_API_KEY to your Vapi private API key}"

if grep -q '{{' "$json"; then
  echo "error: $json still has unfilled {{placeholders}}" >&2
  exit 1
fi

curl -sS -X POST https://api.vapi.ai/assistant \
  -H "Authorization: Bearer $VAPI_API_KEY" \
  -H "Content-Type: application/json" \
  --data @"$json"
echo
echo "Next: in the Vapi dashboard, open Phone Numbers, attach this assistant to a number, then call it."
