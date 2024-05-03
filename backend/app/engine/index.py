import logging
import os

from llama_index.core.indices import VectorStoreIndex
from llama_index.vector_stores.qdrant import QdrantVectorStore
from qdrant_client import AsyncQdrantClient


logger = logging.getLogger("uvicorn")


def get_index():
    logger.info("Connecting to Qdrant collection..")
    aclient = AsyncQdrantClient(
        os.getenv("QDRANT_URL"),
    )
    store = QdrantVectorStore(
        collection_name=os.getenv("QDRANT_COLLECTION"),
        aclient=aclient,
    )
    index = VectorStoreIndex.from_vector_store(vector_store=store)
    logger.info("Finished connecting to Qdrant collection.")
    return index
