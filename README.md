# 🛡️ Nginx Guardian

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![CI](https://github.com/Erharshita-cloud/nginx-guardian/actions/workflows/ci.yml/badge.svg)](https://github.com/Erharshita-cloud/nginx-guardian/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/docker-ready-blue)](https://github.com/users/Erharshita-cloud/packages/container/package/nginx-guardian)
[![GitHub stars](https://img.shields.io/github/stars/Erharshita-cloud/nginx-guardian?style=social)](https://github.com/Erharshita-cloud/nginx-guardian/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/Erharshita-cloud/nginx-guardian)](https://github.com/Erharshita-cloud/nginx-guardian/issues)

A **self-healing monitor** for Nginx. Guardian checks if your Nginx service is alive, restarts it if it fails, and exports Prometheus metrics so you can monitor failures and auto-restarts.  

---

## 🚀 Features
- ⏱️ **Health monitoring** — auto-checks Nginx availability
- 🔄 **Self-healing** — auto-restarts Nginx if it’s down
- 📊 **Prometheus metrics** — exposes failure & restart counters
- 🚨 **Alerting** — integrates with Alertmanager for Slack/email alerts
- 🐳 **Docker-ready** — deploy easily with Docker or Compose

---

## 🏁 Quick Start

### Run with Docker Compose
```bash
git clone https://github.com/Erharshita-cloud/nginx-guardian.git
cd nginx-guardian

# Copy sample env file
cp .env.example .env

# Start Nginx + Guardian + Prometheus + Alertmanager
docker-compose up -d

## 🐳 Run with Docker

You can pull the latest Guardian image from GitHub Container Registry:

```bash
docker run -d \
  --name nginx-guardian \
  -p 8080:80 \
  -p 9101:9101 \
  ghcr.io/erharshita-cloud/nginx-guardian:latest

