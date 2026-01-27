#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export OPENAI_API_KEY="[your_key]"
export OPENAI_BASE_URL="https://api.openai.com"
export OPENAI_MODEL="GPT-5.2"

SHOT="${SHOT:-5}"            # 0 or 5
DATA_ROOT="${DATA_ROOT:-data}"
OUT_DIR="${OUT_DIR:-results/gpt}"

mkdir -p "$OUT_DIR"
python evaluation/gpt_eval.py \
  --shot "$SHOT" \
  --data-root "$DATA_ROOT" \
  --output "$OUT_DIR/shot${SHOT}.jsonl"
