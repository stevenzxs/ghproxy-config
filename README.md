# GitHub download proxy configuration

Deployment target: **https://ghproxy.stevenzxs.cn**, 104.244.90.25 linux/amd64. Product implementation: [HubProxy v1.2.5](https://github.com/sky22333/hubproxy/releases/tag/v1.2.5), MIT; fixed source identity in sources.json. No product source is copied here.

The reviewed manual Actions workflow calls the upstream native Dockerfile, smoke-tests /ready, publishes ghcr.io/stevenzxs/ghproxy and exports source/config identities, digest and checksums. Invoke only after workflow review and applicable governance authorization. Floating upstream base tags mean full bit-for-bit reproducibility is not claimed; preserve actual image/build provenance.

compose.yml joins existing deploy_sub2api-network, has no host port, limits memory to 256 MiB and CPU to 0.5, runs non-root/read-only. Only existing sub2api-caddy terminates TLS. User approved public GitHub downloads and upstream frontend on 2026-11-19. Root page, frontend assets and health are public. No GitHub credentials are passed upstream. Registry, API, Hugging Face and push endpoints remain blocked even if the upstream UI advertises them. Request rate limits are not bandwidth or concurrent-download limits; public usage can consume the host traffic allowance.

Public usage:

```sh
curl -fLO 'https://ghproxy.stevenzxs.cn/https://github.com/OWNER/REPO/releases/download/TAG/FILE'
git clone 'https://ghproxy.stevenzxs.cn/https://github.com/OWNER/REPO.git'
```

See skills/ghproxy-deploy/SKILL.md for installation, verification, rollback and approval boundaries; docs/plans/2026-11-19-ghproxy.md for implementation status. No runtime secrets in Git. Upstream processes .sh/.ps1 content: verify signatures/checksums and do not execute downloaded scripts blindly. Production deployment, Hermes orchestration, negative-path/security checks and rollback are pending until recorded with actual evidence.
