from utils import *

#client = logar()
##vectorStore = vector_store_create(client)
#qa = question(vectorStore)

#query = "O que é Epilepsia?"
#response = qa.run(query)
#print(response)

#documentos_retornados = buscar_documentos(vectorStore, query)

#print(documentos_retornados)

def perguntar_gpt_fabrica(query):
    client = logar()
    vectorStore = vector_store_create(client)
    qa = question(vectorStore)
    response = qa.run(query)
    return response