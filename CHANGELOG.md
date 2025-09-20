# Changelog

All notable changes to **nginx-guardian** will be documented here.

## [Unreleased]
- Add support for custom alert integrations
- Improve Grafana dashboards

## [0.1.0] - 2025-09-20
### Added
- Initial release 🎉
- Nginx health check and auto-restart
- Prometheus metrics exporter (`guardian_failures_total`, `guardian_restarts_total`)
- Docker Compose setup (dev + prod)
- Ansible playbooks for deployment
- CI workflow (lint, tests)
- Docker publish workflow (GitHub Container Registry)
