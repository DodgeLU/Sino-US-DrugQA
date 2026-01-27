#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export DEEPSEEK_API_KEY="[your_key]"
export DEEPSEEK_BASE_URL="https://api.deepseek.com"
export DEEPSEEK_MODEL="DeepSeek-V3.2"

SHOT="${SHOT:-5}"            # 0 or 5
DATA_ROOT="${DATA_ROOT:-data}"
OUT_DIR="${OUT_DIR:-results/deepseek}"

mkdir -p "$OUT_DIR"
python evaluation/deepseek_eval.py \
  --shot "$SHOT" \
  --data-root "$DATA_ROOT" \
  --output "$OUT_DIR/shot${SHOT}.jsonl"
