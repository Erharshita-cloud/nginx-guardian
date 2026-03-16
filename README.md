# 🛡️ Nginx Guardian

<div align="center">

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=00D9FF&center=true&vCenter=true&width=600&lines=Checking+Nginx+status...+🔍;Nginx+is+DOWN!+🚨;Restarting+service...+🔄;Nginx+is+back+ONLINE!+✅;Guardian+never+sleeps.+🛡️" alt="Typing animation" />

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)
[![CI](https://github.com/Erharshita-cloud/nginx-guardian/actions/workflows/ci.yml/badge.svg)](https://github.com/Erharshita-cloud/nginx-guardian/actions/workflows/ci.yml)
[![Docker](https://img.shields.io/badge/docker-ready-blue?logo=docker)](https://github.com/users/Erharshita-cloud/packages/container/package/nginx-guardian)
[![Stars](https://img.shields.io/github/stars/Erharshita-cloud/nginx-guardian?style=social)](https://github.com/Erharshita-cloud/nginx-guardian/stargazers)
[![Issues](https://img.shields.io/github/issues/Erharshita-cloud/nginx-guardian)](https://github.com/Erharshita-cloud/nginx-guardian/issues)

> **Keep your Nginx alive — automatically detects downtime and self-recovers.**

</div>

---

## 🚨 The Problem

Nginx goes down. It happens — memory spikes, misconfigs, crashes. Without monitoring, your users hit a blank page and you find out hours later from a support ticket.

**Nginx Guardian fixes this automatically.** It watches your Nginx 24/7, detects failure in seconds, restarts the service, and fires an alert — all before your users notice anything is wrong.

---

## ⚙️ How It Works
```
┌─────────────────┐     Down?     ┌──────────────────┐
│  Nginx Guardian │──────────────▶│  Auto-Restart    │
│  (health loop)  │               │  nginx service   │
└─────────────────┘               └──────────────────┘
        │                                  │
        │ metrics                          │ alert
        ▼                                  ▼
┌─────────────────┐          ┌─────────────────────────┐
│   Prometheus    │          │  Alertmanager           │
│   /metrics      │          │  Slack / Email / PagerDuty│
└─────────────────┘          └─────────────────────────┘
```

---

## ✨ Features

| Feature | Description |
|---|---|
| ⏱️ **Health Monitoring** | Continuously checks Nginx availability |
| 🔄 **Self-Healing** | Auto-restarts Nginx the moment it goes down |
| 📊 **Prometheus Metrics** | Exposes failure & restart counters at `/metrics` |
| 🚨 **Smart Alerting** | Integrates with Alertmanager for Slack/email alerts |
| 🐳 **Docker Ready** | One command deploy with Docker Compose |
| 📝 **Audit Logging** | Every restart event is logged with timestamps |

---

## ⚡ Quick Start

### 🐳 Docker Compose (Recommended)
```bash
# Clone
git clone https://github.com/Erharshita-cloud/nginx-guardian.git
cd nginx-guardian

# Configure
cp .env.example .env

# Launch Nginx + Guardian + Prometheus + Alertmanager
docker-compose up -d
```

### 🐋 Docker Only
```bash
docker run -d \
  --name nginx-guardian \
  -p 8080:80 \
  -p 9101:9101 \
  ghcr.io/erharshita-cloud/nginx-guardian:latest
```

### 🐍 Run Locally
```bash
pip install -r requirements.txt
python guardian.py
```

---

## 📊 Prometheus Metrics

Once running, metrics are exposed at `http://localhost:9101/metrics`:
```
# Total times Nginx was found down
nginx_guardian_failures_total

# Total times Guardian restarted Nginx
nginx_guardian_restarts_total

# Current Nginx status (1 = up, 0 = down)
nginx_up
```

---

## 📂 Project Structure
```
nginx-guardian/
├── guardian.py           # Core monitoring & self-healing engine
├── docker-compose.yml    # Full stack: Nginx + Guardian + Prometheus
├── Dockerfile            # Container definition
├── prometheus.yml        # Prometheus scrape config
├── alertmanager.yml      # Alert routing (Slack/email)
├── .env.example          # Environment variable template
└── README.md
```

---

## 🤝 Contributing

Issues, ideas, and PRs are welcome!

1. Fork the repo
2. Create your branch: `git checkout -b feature/your-idea`
3. Commit: `git commit -m 'Add: your feature'`
4. Push and open a PR

---

<div align="center">

**Harshita Goel** · DevOps & Cloud Engineer

[GitHub](https://github.com/Erharshita-cloud) · harshitagoel1503@gmail.com

⭐ **Star this repo if Guardian saved your Nginx!**

</div>
