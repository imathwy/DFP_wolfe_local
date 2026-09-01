#!/usr/bin/env bash
set -euo pipefail
exec python3 -m paperforge build web "$(cd "$(dirname "$0")/.." && pwd)" "$@"
