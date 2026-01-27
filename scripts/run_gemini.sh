#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export GEMINI_API_KEY="[your_key]"
export GEMINI_MODEL="Gemini-3-flash"

SHOT="${SHOT:-5}"            # 0 or 5
DATA_ROOT="${DATA_ROOT:-data}"
OUT_DIR="${OUT_DIR:-results/gemini}"

mkdir -p "$OUT_DIR"
python evaluation/gemini_eval.py \
  --shot "$SHOT" \
  --data-root "$DATA_ROOT" \
  --output "$OUT_DIR/shot${SHOT}.jsonl"
