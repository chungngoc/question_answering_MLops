# Question Answering API (MLOps)

[![QA MLOps CI](https://github.com/chungngoc/question_answering_mlops/actions/workflows/ci.yml/badge.svg)](https://github.com/chungngoc/question_answering_mlops/actions/workflows/ci.yml)

## Overview

This project is an end-to-end **Question Answering (QA) API** built with
**FastAPI** and **Hugging Face Transformers**, designed with
**production-grade MLOps practices**.

The service exposes a REST API that answers questions given a textual context,
and is fully containerized, tested, and CI/CD-enabled.

## Retrieval-Augmented Generation (RAG)

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline
to answer questions using an internal knowledge base.

Instead of requiring the user to provide a context manually, the system:
1. Retrieves the most relevant documents using semantic search
2. Builds a context dynamically from retrieved documents
3. Applies an extractive Question Answering model to produce the final answer


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
FastAPI API
  |
  +--> Embedding Model (Sentence Transformers)
  |        |
  |        v
  |     FAISS Vector Store
  |        |
  |        v
  |  Top-K Relevant Documents
  |
  v
Question Answering Model (Hugging Face)
  |
  v
Answer + Source Documents
```

The embedding model and FAISS index are loaded lazily and shared across requests. This ensures efficient memory usage and fast inference while keeping application startup time low.

## API Endpoints

| Method | Endpoint   | Description |
|------|-----------|------------|
| POST | `/predict` | Answer a question using Retrieval-Augmented Generation. |
| GET  | `/version` | Application metadata |
| GET  | `/docs`    | Swagger UI |

**Example** :

*Request*:
```json
{
  "question": "What is MLOps?"
}
```
*Response*
```json
{
  "answer": "MLOps combines machine learning and DevOps practices...",
  "score": 0.87,
  "sources": ["mlops.txt"]
}
```

## Run locally
```bash
make install
make run
```

## Tech Stack
- Python
- FastAPI
- Uvicorn
- Hugging Face Transformers
- Sentence Transformers
- PyTorch
- FAISS (vector similarity search)
- Docker
- GitHub Actions
- GitHub Container Registry (GHCR)

## Future Improvements
- Extend RAG pipeline with generative models (LLMs)
- Metrics endpoint (Prometheus)
- Cloud deployment with autoscaling
- Model versioning and experiment tracking
