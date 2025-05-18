from sentence_transformers import SentenceTransformer
import faiss
from llama_cpp import Llama

from config import config
from utils import get_logger, load_documents

def make_prompt(context, query):
    return (
        "<|user|>\n"
        "社内ルールに載っていることのみに基づいて答えてください．"
        f"社内ルール：{context}\n\n"
        f"質問：{query}\n"
        "<|end|>\n"
        "<|assistant|>\n"
    )

logger = get_logger()
logger.info("📦 Loading Index and Document...")
index = faiss.read_index(config["INDEX_PATH"])


cat_documents = load_documents(json_path=config["DOC_PATH"])

embedder = SentenceTransformer(config["EMBED_MODEL"])

logger.info("📦 Crating LLM Model...")
llm = Llama(
    model_path=config["MODEL_PATH"],
    n_ctx=2048,
    n_threads=4,
)

query = "社内規則に関して，朝の挨拶のルールを教えてください"
# query = "朝の挨拶ってどこまで丁寧にしたほうがいいですか？"
# query = "水を飲みに行ってきてもいいですか？"
# query = "今日、定時で帰っていいですか？"
query_vec = embedder.encode([query])
distance, indices = index.search(query_vec, config["TOP_K"])

context_chunks = [cat_documents[i] for i in indices[0]]
context_text = "\n\n".join(context_chunks)

logger.info("[RAG なし] 推論中...")
prompt_wo_RAG = make_prompt("", query)
res_wo_RAG = llm(prompt_wo_RAG, max_tokens=256, stop=["<|end|>", "<|user|>", "<|assistant|>"])
answer_wo_RAG = res_wo_RAG["choices"][0]["text"].strip()

logger.info("[RAG あり] 推論中...")
prompt_w_RAG = make_prompt(context_text, query)
res_w_RAG = llm(prompt_w_RAG, max_tokens=256, stop=["<|end|>", "<|user|>", "<|assistant|>"])
answer_w_RAG = res_w_RAG["choices"][0]["text"].strip()

logger.info("[RAG なし] answer")
print(answer_wo_RAG)
print()
logger.info("[RAG あり] answer")
print(answer_w_RAG)