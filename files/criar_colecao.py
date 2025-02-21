from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

# LangChain
# Importar Qdrant como vector store
from langchain_community.vectorstores import Qdrant
# Importar OpenAI embeddings
from langchain_community.embeddings import OpenAIEmbeddings
# Função para auxiliar na quebra do texto em chunks
from langchain.text_splitter import CharacterTextSplitter
# Módulo para facilitar o uso de vector stores em QA (question answering)
from langchain.chains import RetrievalQA
# Importar LLM (modelo de linguagem)
from langchain_community.llms import OpenAI

import os

from utils import *

client = logar()
client.create_collection(
    collection_name="openai_collection",
    vectors_config=VectorParams(size=1536, distance=Distance.COSINE)
)

