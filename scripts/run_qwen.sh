#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

export QWEN_API_KEY="[your_key]"
export QWEN_BASE_URL="https://dashscope.aliyuncs.com/api/v1/services/aigc/text-generation/generation"
export QWEN_MODEL="Qwen-3-235B"

SHOT="${SHOT:-5}"            # 0 or 5
DATA_ROOT="${DATA_ROOT:-data}"
OUT_DIR="${OUT_DIR:-results/qwen}"

mkdir -p "$OUT_DIR"
python evaluation/qwen_eval.py \
  --shot "$SHOT" \
  --data-root "$DATA_ROOT" \
  --output "$OUT_DIR/shot${SHOT}.jsonl"
