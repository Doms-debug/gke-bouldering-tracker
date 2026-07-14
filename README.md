# 🧗‍♂️ Bouldering tracker

A lightweight, cloud-native application for tracking bouldering and sport climbing sessions.

**Infra shift case study:** This project was originally built on Google Kubernetes Engine (GKE) using GitOps (ArgoCD). To optimize cloud expenditures for a personal portfolio project, the architecture was successfully migrated via a "Lift and Shift" approach to a zero-cost infrastructure using GCP's Always Free tier, reducing monthly costs from ~$50 to $0 without sacrificing CI/CD automation or secure networking.

## 🏗️ Architecture and tech stack

- **Frontend:** HTML5 + Vanilla JS + Bootstrap 5
- **Backend:** Python / FastAPI
- **Database:** PostgreSQL (Local containerized database with persistent volumes)
- **Containerization:** Docker and Docker Compose
- **Infrastructure:** GCP Compute Engine (`e2-micro` VM in `us-central1` - Always Free Tier)
- **Networking / Ingress:** Cloudflare Quick Tunnels (Secure public HTTPS exposure bypassing cloud Load Balancers)
- **CI/CD Pipeline:** GitHub Actions (Automated remote deployments via GCP Identity-Aware Proxy SSH)

## 📂 Repository structure

```text
.
├── .github/workflows/       # GitHub Actions CI/CD pipelines (VM deployment via IAP)
├── backend/                 # FastAPI application, HTML frontend, and Dockerfile
├── docker-compose.yml       # Multi-container orchestration (API, DB, Cloudflare)
└── README.md
```
