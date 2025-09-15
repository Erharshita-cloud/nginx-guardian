# nginx-guardian

**Keep your Nginx alive — detect downtime, self-recover, and alert.**

---

## 📌 Overview
`nginx-guardian` is a lightweight recovery and monitoring tool for **Nginx**.  
It detects failures, automatically reloads or restarts Nginx safely, and integrates with Prometheus + Alertmanager for observability and alerting.

Project structure:
- `nginx/` → sample nginx configs
- `webhook/` → guardian scripts
- `prometheus/` → Prometheus configuration
- `alertmanager/` → alert rules
- `ansible/` → playbooks for deployment
- `docker-compose.yml` → base setup

---

## 🚀 Features
- Health checks (HTTP, TCP)
- Safe recovery with `nginx -t` + config rollback
- Prometheus metrics on port **9101**
- Docker Compose integration
- Alerting with Alertmanager, Slack, etc.
- Ansible automation

---

## ⚡ Quick Start (Dev via Docker Compose)
```bash
git clone https://github.com/Erharshita-cloud/nginx-guardian.git
cd nginx-guardian
docker-compose -f docker-compose.dev.yml up -d
