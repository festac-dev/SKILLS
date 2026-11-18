#!/usr/bin/env bash
set -euo pipefail
ffmpeg -hide_banner -loglevel error -f lavfi -i "color=c=0xaab8ba:s=320x180:d=2:r=4" -pix_fmt yuv420p -y "$(dirname "$0")/room.mp4"
