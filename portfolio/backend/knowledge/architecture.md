# Framework-FreeFE Architecture

The application is divided into frontend, backend, AI, and data layers.

## Frontend

The frontend is framework-free.

HTML provides semantic structure.

CSS provides responsive presentation.

JavaScript modules provide application behavior.

## API

FastAPI exposes REST endpoints.

Important endpoints include:

GET /api/health

POST /api/contact

POST /api/chat

## AI

The AI layer is isolated from HTTP routing.

The RAG service retrieves relevant portfolio knowledge before generating
an answer.

LangChain provides document processing and retrieval abstractions.

## Data

SQLite stores contact messages.

The vector store stores embeddings for portfolio knowledge.

## Security

Secrets are stored in environment variables.

The browser must never receive an LLM provider API key.

The backend owns all calls to external AI services.

## Deployment

The frontend and backend can be deployed independently.

The architecture can later be containerized and deployed through a CI/CD
pipeline.
