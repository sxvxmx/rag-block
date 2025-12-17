# RAG Application

A Retrieval-Augmented Generation (RAG) application that comes as a building block for other agentic projects 😉.

## How It Works

1. Documents in `src/data/` are loaded and split into chunks
2. Chunks are embedded using Hugging Face transformer models
3. Embeddings are stored in Qdrant vector database
4. When querying, the system retrieves relevant chunks based on semantic similarity
5. The LLM generates responses using retrieved context and available tools

## Tech Stack

- **Framework**: Flask
- **LLM Integration**: LangChain & OpenAI API
- **Document Processing**: LlamaIndex
- **Embeddings**: Hugging Face BGE (BAAI/bge-small-en-v1.5)
- **Vector Store**: Qdrant
- **Containerization**: Docker

## Setup

### Prerequisites

- Python 3.13+
- Docker and Docker Compose (optional, for containerized deployment)
- Access to an OpenAI-compatible API (configured to use OpenRouter)

### Local Installation

1. Clone the repository:
```bash
git clone https://github.com/sxvxmx/rag-block.git
```

2. Install dependencies:
```bash
uv sync
```

3. Configure environment variables:
```bash
cp .env_example .env
# Edit .env to add your API keys and settings
```

5. Place documents in `src/data/` (PDF format supported)

6. Start Qdrant database:
```bash
docker run -p 6333:6333 -v ./qdrant_storage:/qdrant/storage:z qdrant/qdrant
```

7. Run the application:
```bash
uv run app.py
```

The API will be available at `http://localhost:8000`

### Docker Deployment

Build and run with Docker:

```bash
docker build -t rag-app .
docker run -p 8000:8000 --env-file .env rag-app
```

## Project Structure

```
src/
├── agent.py          # LLM agent configuration
├── emb_service.py    # Document embedding service
├── index.py          # Vector index creation
├── prompt.py         # Prompt templates
├── tools.py          # Available tools
└── data/             # Documents for RAG (PDF)
app.py               # Flask application entrypoint
```

## API Usage

Example cURL request for _Attention Is All You Need_:
```bash
curl -X POST http://localhost:8000/api/ask_stream \
  -H "Content-Type: application/json" \
  -d '{"question": "what is encoder description in database?"}'
```

Answer:
```bash
  {"token": "Based"}
  {"token": " on the database"}
  {"token": " search"}
  {"token": " results, the"}...
```
## Configuration

The application uses the following environment variables:

- `OPENAI_API_KEY`: API key for OpenAI-compatible service
- `DATABASE_URL`: Qdrant database URL (default: localhost)
- `DATABASE_PORT`: Qdrant database port (default: 6333)
- `PORT`: Application port (default: 8000)
