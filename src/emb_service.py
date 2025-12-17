from llama_index.core import SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
import logging
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

logger = logging.getLogger(__name__)


documents = SimpleDirectoryReader(
    input_dir="src/data",
    required_exts=[".pdf"],
).load_data(show_progress=True)

logger.info(f"Загружено {len(documents)} страниц")

node_parser = SentenceSplitter.from_defaults(
    chunk_size=512, chunk_overlap=50, paragraph_separator="\n\n"
)
chunks = node_parser.get_nodes_from_documents(documents)
logger.info(f"Разбито на {len(chunks)} блоков")

# Локальный эмбедер
model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
Settings.node_parser = SentenceSplitter(chunk_size=512, chunk_overlap=50)
Settings.embed_model = model
