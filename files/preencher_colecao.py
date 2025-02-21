from utils import *

#filepath = 'Artigos/supressao.pdf'
#tema = 'Supressao condicionada'

def realizar_upload(filepath, tema):

    client = logar()
    #Pegar o vetor client
    vector = vector_store_create(client)    

    raw_text = abrir_pdf(filepath)

    print('DEBUG TEXTO')
    #print(raw_text)

    texts = get_chunks(raw_text)

    #Inserir metadata
    metadata = get_metadata(texts, tema, filepath)

    print('METADATA')
    print(f"Tamanho de texts: {len(texts)}")
    print(f"Tamanho de metadata: {len(metadata)}")

    input_data(vector, texts, metadata)