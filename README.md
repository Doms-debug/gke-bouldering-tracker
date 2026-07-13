# Bouldering tracker

A lightweight, cloud-native application for tracking bouldering and sport climbing sessions. Designed with a strict FinOps approach to run on Google Kubernetes Engine (GKE) at near-zero operational cost.

## Architecture & tech stack

This project implements a complete End-to-End GitOps workflow:

*   **Frontend:** HTML5 + Vanilla JS + Bootstrap 5 
*   **Backend:** Python / FastAPI
*   **Database:** PostgreSQL (Stateful workload with Persistent Volume Claims)
*   **Containerization:** Docker & Google Artifact Registry
*   **CI/CD Pipeline:** GitHub Actions (Automated build, image tagging and manifest updates)
*   **GitOps:** ArgoCD (Continuous synchronization with GKE cluster)
*   **Networking / Ingress:** Cloudflare Quick Tunnels (Secure public exposure bypassing expensive cloud Load Balancers)

```
## Repository structure
.
├── .github/workflows/       # GitHub Actions CI/CD pipelines
├── backend/                 # FastAPI application, HTML frontend, and Dockerfile
├── kubernetes/              # Kubernetes manifests
│   └── bouldering-tracker/  # Application deployment, DB, and Cloudflare tunnel config
└── README.md
```
Final product look:

<img width="686" height="693" alt="image" src="https://github.com/user-attachments/assets/ce886c55-f390-49d8-9430-0adfedc5faac" />


## TO DO:
- Move it to Cloud Run and host permanently

## Author
Dominik Czajka
