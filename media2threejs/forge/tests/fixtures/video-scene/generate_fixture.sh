#!/usr/bin/env bash
set -euo pipefail
ffmpeg -hide_banner -loglevel error -f lavfi -i "color=c=steelblue:s=160x90:d=1:r=4" -pix_fmt yuv420p -y "$(dirname "$0")/fixture.mp4"
