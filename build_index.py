from sentence_transformers import SentenceTransformer
import faiss

from config import config
from utils import get_logger, load_documents

logger = get_logger()
logger.info("Loadindg documents")
cat_documents = load_documents(json_path=config["DOC_PATH"])

logger.info("Creating embedder")
embedder = SentenceTransformer(config["EMBED_MODEL"])
doc_embeddings = embedder.encode(cat_documents)


dim = doc_embeddings[0].shape[0]
index = faiss.IndexFlatL2(dim)
index.add(doc_embeddings)

faiss.write_index(index, config["INDEX_PATH"])
logger.info(f"✅ FAISS Index Saved! {config['INDEX_PATH']}")