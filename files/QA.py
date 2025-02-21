from utils import *

import openai

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



def perguntar_gpt_4(query):
    client = logar()
    vectorStore = vector_store_create(client)
    documentos = buscar_documentos(vectorStore, query)
    response = openai.ChatCompletion.create(        
        model="gpt-4o-mini",
        messages = [
        {"role": "system", "content": "Você é um assistente da empresa DNA Consult, sempre responda em português"},
        {"role": "user", "content": f"""
            INSTRUÇÃO: Você deve responder a QUERY
            INSTRUÇÃO: Sua base de conhecimento DEVE ser APENAS o CONTEXTO!
            INSTRUÇÃO: Responda APENAS sempre em Português!
            INSTRUÇÃO: Se souber que não sabe, SEJA EXPLICITO que não sabe!
         
            Query:{query}
            Contexto:{documentos}
         
            """}],
            temperature=0.7
    )

    print(response.choices[0].message.content)