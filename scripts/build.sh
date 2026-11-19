#!/usr/bin/env bash
set -euo pipefail
root=$(cd "$(dirname "$0")/.." && pwd)
cd "$root"
python3 -m unittest discover -s tests -v
sha=$(python3 -c 'import json; print(json.load(open("sources.json"))["sha"])')
test "$(git -C source rev-parse HEAD)" = "$sha"
docker build --platform linux/amd64 --build-arg TARGETARCH=amd64 --build-arg VERSION=v1.2.5 \
  --label "org.opencontainers.image.revision=$sha" \
  --label "org.opencontainers.image.source=https://github.com/sky22333/hubproxy" \
  --label "io.ghproxy.config.revision=$GITHUB_SHA" \
  -t "ghcr.io/stevenzxs/ghproxy:config-$GITHUB_SHA" source
