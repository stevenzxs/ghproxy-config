---
name: ghproxy-deploy
description: Build and deploy fixed HubProxy v1.2.5 GitHub download service on 104.244.90.25 using the existing Caddy gateway.
---

# Controlled delivery

Read AGENTS.md and the central project-delivery 1.1 governance before work. Default to preflight; production deployment requires approval. Source 320df5def5c202409d2beec0dd5b4b2266bedc02, linux/amd64, configuration SHA and Actions run must be recorded.

Hermes must dispatch reviewed build.yml at a fixed config commit, wait for completion, download ghproxy-evidence, verify SHA256SUMS and image source/config labels and RepoDigest. No server or local fallback builds. Never store token values in logs or Git. The workflow uses GITHUB_TOKEN with job-scoped packages:write. Do not start deployment until applicable governance gates have actual evidence or an explicitly approved exception.

On root@104.244.90.25 preserve existing containers, Caddy sites, certificate volumes and secrets. Pull only ghcr.io/stevenzxs/ghproxy@sha256:<verified digest>. Put verified config archive under a new /opt/ghproxy/releases/<config-sha> directory, write image reference into excluded runtime .env, run docker compose config, and start only the ghproxy service. No build and no backend ports.

Back up /opt/sub2api/deploy/Caddyfile with a unique suffix. Append config/Caddyfile.fragment once only, verify existing sub2api-caddy can resolve ghproxy-backend, run caddy validate in existing container then caddy reload. Never start another gateway. If file mount is inode-bound, update existing file content without replacing its inode. Detect concurrent changes before writing.

Check strict TLS on https://ghproxy.stevenzxs.cn/ready, frontend HTML/assets, raw/release content checksums, clone/pull, denied arbitrary targets, denied push, and existing site health. User approved public downloads and upstream root frontend on 2026-11-19; registry/API/Hugging Face remain blocked. Request rate limits do not cap bandwidth/concurrent transfers. Upstream may rewrite shell scripts; do not promise byte-identical shell/PowerShell downloads. Upstream redirect target policy remains a security-review item.

Upgrade by new verified digest, keeping old release and runtime configuration. On failure restore only the backed-up Caddy change after checking no intervening edits, validate/reload, and restore prior GHProxy digest. First-install rollback stops only this Compose project; do not remove unrelated networks or volumes. Uninstall removes only managed site block and project containers, preserving evidence and backups. Idempotency requires managed-block uniqueness and digest equality checks. Record actual health/rollback/Hermes evidence in central register; missing evidence is not compliance.
