from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams
import os
from dotenv import load_dotenv
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

import fitz


def logar():
    IP_QDRANT = os.getenv("IP_QDRANT")
    client = QdrantClient(host=IP_QDRANT, port=6333)
    print('Loguei')
    return client


#######################################################################################Injetar Dados


"""
def abrir_pdf(filepath):
    texto = ""
    with fitz.open(filepath) as pdf:
        for pagina in pdf:
            texto += pagina.get_text() + '\n'
    return texto
"""
def abrir_pdf(arquivo):
    texto = ""
    # Garante que o ponteiro do arquivo esteja no início
    arquivo.seek(0)
    # Abre o PDF a partir do stream, especificando o filetype
    pdf = fitz.open(stream=arquivo.read(), filetype="pdf")
    for pagina in pdf:
        texto += pagina.get_text() + '\n'
    return texto

def abrir_txt(filepath):

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text

def get_metadata(texts, tema, filepath):
    if not texts:  # Verifica se texts está vazio
        return []
    
    return [{"tema": tema, "arquivo": filepath} for _ in range(len(texts))]

def vector_store_create(client):
    
    load_dotenv()    
    OPENAI_API_KEY = os.getenv("OPENAI")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    
    vectorstore = Qdrant(
        client=client,
        collection_name="openai_collection",
        embeddings=embeddings
    )
    return vectorstore

def get_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def input_data(vector, text, metadata):
    vector.add_texts(texts=text,
                     metadatas=metadata)
    
    


#################################################### RETRIEVE

def question(vectorstore):
    load_dotenv()
    OPENAI_API_KEY = os.getenv("OPENAI")
    
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=OPENAI_API_KEY),
        chain_type='stuff',
        retriever=vectorstore.as_retriever(search_type='similarity')
    )
    return qa

def buscar_documentos(vectorstore, query, k=20):
    """
    Busca documentos similares à query no banco vetorial sem chamar o GPT.
    
    :param vectorstore: Objeto do banco vetorial (Qdrant, FAISS, etc.).
    :param query: Pergunta do usuário.
    :param k: Número de documentos similares a retornar.
    :return: Lista de textos encontrados.
    """
    retriever = vectorstore.as_retriever(search_type="similarity")  # Configura a busca
    documentos = retriever.get_relevant_documents(query, k=k)  # Busca os documentos
    # Filtrar documentos cujo metadado "tema" esteja na query
    documentos_filtrados = [
        doc for doc in documentos
        if doc.metadata['tema'].lower() in query.lower() 
    ]
    return documentos_filtrados

#def resposta(vectorstore):
    