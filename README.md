# Question Answering API (MLOps)

[![QA MLOps CI](https://github.com/chungngoc/question_answering_mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/chungngoc/question_answering_mlops/actions/workflows/ci.yml)

## Overview

This project is an end-to-end **Question Answering (QA) API** built with
**FastAPI** and **Hugging Face Transformers**, designed with
**production-grade MLOps practices**.

The service exposes a REST API that answers questions given a textual context,
and is fully containerized, tested, and CI/CD-enabled.

## Key Features

- REST API for extractive Question Answering
- Lazy & thread-safe model loading (efficient memory usage)
- FastAPI dependency injection and clean architecture
- Dockerized application
- CI/CD with GitHub Actions
- Docker image published to GitHub Container Registry (GHCR)
- Environment-based configuration
- Structured logging and request timing
- Unit and API tests with mocked ML model

## Architecture

```sequence
Client
  |
  v
FastAPI Application
  |
  v
Hugging Face QA Model (lazy-loaded, singleton)
```

The model is loaded lazily on the first request and shared across all requests
to minimize startup time and memory usage.

## API Endpoints

| Method | Endpoint   | Description |
|------|-----------|------------|
| POST | `/predict` | Answer a question given a context |
| GET  | `/version` | Application metadata |
| GET  | `/docs`    | Swagger UI |

Example request:

{
  "question": "What is MLOps?",

  "context": "MLOps combines machine learning and DevOps practices."
}

## Run locally
```bash
make install
make run
```

## Tech Stack
- Python
- FastAPI
- Hugging Face Transformers
- PyTorch
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)

## Future Improvements
- Retrieval-Augmented Generation (RAG)
- Metrics endpoint (Prometheus)
- Cloud deployment with autoscaling
- Model versioning and experiment tracking
