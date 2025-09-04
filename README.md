# Embedding Service

Minimal FastAPI microservice for generating  embeddings.

## Overview
Exposes a single HTTP endpoint that accepts text and returns embedding vectors. Pydantic models define request/response. Internals split into controllers, services, implementations, workers, and shared models/enums.


## Requirements
Python 3.10+.  
Environment variables: `MISTRAL_API_KEY`.


## Run
```bash
python -B main.py
```

## Endpoint
POST `/api/v1/cte`  
Body accepts text or an array of texts. Returns JSON with `status`, `usage`, and `data` where each item has `index` and `embedding`.

Example body:
```json
{ "inputs": ["hello world"] }
```

Example response (shape):
```json
{
  "status": "SUCCESS",
  "usage": { "promptTokens": 2, "completionTokens": 0, "totalTokens": 2 },
  "data": [{ "index": 0, "embedding": [0.01, ...] }]
}
```
