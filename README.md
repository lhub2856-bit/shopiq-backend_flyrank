# ShopIQ - E-commerce Purchase Prediction & Customer Segmentation

## Overview
ShopIQ is an automated backend intelligence system designed for e-commerce platforms to predict customer purchase intent in real time and categorize visitors into distinct behavioral segments.

## Implemented Concepts (FlyRank Capstone)
This project satisfies the capstone requirements by implementing the following core program concepts:
1. **API Endpoints:** FastAPI REST routes (`/analyze`) handling live incoming payload metrics.
2. **Database Persistence:** Local/Cloud session logs and database storage integration.
3. **Authentication:** Token and boundary-secured administrative route access.
4. **ML Model Integration:** Embedded scikit-learn classification engine (`model.pkl`) providing real-time predictions.
5. **Containerized Deployment (Swap):** Fully containerized stack runnable via Docker Compose.
   * *Swap Reason:* Caching logic was swapped for Deployment to ensure the application is container-ready and accessible.

## Project Structure
shopiq-backend_flyrank/
├── model/
│   └── model.pkl
├── app.py
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
## How to Run (Quick Start)
1. Clone this repository.
2. Ensure Docker and Docker Compose are installed on your machine.
3. Build and run the system using the following single command:
   ```bash
   docker compose up --build
   Access the interactive API documentation (Swagger UI) in your browser at:
http://localhost:8000/docs

5-Minute Demo Path
Open http://localhost:8000/docs in your browser.

Expand the POST /analyze endpoint.

Click Try it out and pass sample numerical features in the JSON body.

Click Execute to see the predicted customer segment and classification response instantly.