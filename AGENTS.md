# GHProxy configuration repository

Follow D:/knowledgebase/standards/project-delivery.md version 1.1 and the central project register. Product source stays in sky22333/hubproxy; this repository owns reviewed Actions, packaging, deployment configuration and Skills only.

Target is 104.244.90.25 linux/amd64, domain ghproxy.stevenzxs.cn. Reuse sub2api-caddy and deploy_sub2api-network. Never create another gateway, replace existing sites, expose backend ports or delete certificate volumes. Never commit tokens, runtime env files, certificates or data. Pin source and image digest; no target-side builds. Build/publication does not authorize bypassing Hermes or governance gates. Validate before reload; preserve rollback backups and report actual evidence.
