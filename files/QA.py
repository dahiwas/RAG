from utils import *

client = logar()
vectorStore = vector_store_create(client)
qa = question(vectorStore)

query = "supressao condicionada / Segundo Sidman, ensino de respostas por reforçamento negativo gera pouco comportamento exploratório e um responder restrito – um primeiro efeito colateral da fuga: “visão de túnel” (pp. 108-109). Qual provável procedimento e resultado sustentariam o seu argumento?"
response = qa.run(query)
print(response)

#documentos_retornados = buscar_documentos(vectorStore, query)

#print(documentos_retornados)