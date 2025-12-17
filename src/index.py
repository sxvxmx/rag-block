from llama_index.vector_stores.qdrant import QdrantVectorStore
import qdrant_client
from src.emb_service import chunks
from dotenv import load_dotenv
import os
import logging
from llama_index.core import StorageContext, VectorStoreIndex

load_dotenv()
logger = logging.getLogger(__name__)

try:
    client = qdrant_client.QdrantClient(
        host=os.getenv("DATABASE_URL"), port=os.getenv("DATABASE_PORT")
    )
except Exception as e:
    logger.error(f"{e}")

vector_store = QdrantVectorStore(
    client=client, collection_name="documents", dimension=384
)
logger.info(f"Создан vector_store")

storage_context = StorageContext.from_defaults(vector_store=vector_store)
logger.info(f"Создан storage_context: {storage_context}")

index = VectorStoreIndex(
    nodes=chunks,
    storage_context=storage_context,
    show_progress=True,
)

logger.info(f"Создан index: {index}")
