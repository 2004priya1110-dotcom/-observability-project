# Complete Observability System – Metrics, Logs & Traces

## Project Overview

This project implements a complete observability system for a Python Flask application using Prometheus, Grafana, Loki, Grafana Alloy, Jaeger and Docker Compose.

It demonstrates how to monitor application metrics, collect centralized logs and trace application requests.

## Technologies Used

- Python and Flask
- Docker and Docker Compose
- Prometheus – Metrics monitoring
- Grafana – Dashboards and visualization
- Loki – Log aggregation
- Grafana Alloy – Log collection and forwarding
- OpenTelemetry – Application instrumentation
- Jaeger – Distributed tracing
- Pytest – Automated testing

## Project Architecture

The project collects three observability signals:

1. **Metrics:** Flask application → Prometheus → Grafana
2. **Logs:** Docker containers → Grafana Alloy → Loki → Grafana
3. **Traces:** Flask application → OpenTelemetry → Jaeger

## Project Structure

```text
observability-project/
│
├── app/
│   ├── __init__.py
│   └── app.py
│
├── tests/
│   └── test_app.py
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│   └── provisioning/
│       ├── datasources/
│       └── dashboards/
│
├── loki/
│   └── loki-config.yml
│
├── alloy/
│   └── config.alloy
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/2004priya1110-dotcom/-observability-project.git
cd -observability-project
```

### 2. Start Docker Desktop

Make sure Docker Desktop is running.

### 3. Start all services

```bash
docker compose up -d --build
```

### 4. Check container status

```bash
docker compose ps
```

## Application and Monitoring URLs

| Service | URL |
|---|---|
| Flask Application | http://localhost:5000 |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Loki | http://localhost:3100 |
| Jaeger | http://localhost:16686 |
| Grafana Alloy | http://localhost:12345 |

### Grafana Login

- Username: `admin`
- Password: `admin123`

## Testing

Run the Flask application tests locally:

```bash
py -m pytest -v
```

All three application tests passed during project verification.

## Results

- Prometheus successfully collected Flask application metrics.
- Grafana displayed application request rate, total HTTP requests and request duration.
- Grafana Alloy collected Docker container logs and forwarded them to Loki.
- Jaeger successfully received application traces.
- All six Docker Compose services were running during final verification.

## Conclusion

This project demonstrates an end-to-end observability solution using open-source DevOps tools. It provides practical experience with Docker containerization, metrics monitoring, centralized logging, distributed tracing and service orchestration.
