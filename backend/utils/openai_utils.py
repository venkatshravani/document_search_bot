# utils/openai_utils.py
import openai
from functools import lru_cache

# Function to fetch embedding from OpenAI
def get_embedding(text: str, model: str = "text-embedding-ada-002"):
    response = openai.Embedding.create(input=text, model=model)
    return response["data"][0]["embedding"]

# Cache-enabled wrapper to avoid repeated embedding calls
@lru_cache(maxsize=1024)
def get_embedding_with_cache(text: str, model: str = "text-embedding-ada-002"):
    return get_embedding(text, model)
