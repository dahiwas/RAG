import streamlit as st
from preencher_colecao import realizar_upload
from QA import perguntar_gpt_fabrica, perguntar_gpt_4

# Configura a página (opcional)
st.set_page_config(page_title="RAG - ChatBot", layout="wide")

# CSS para título fixo e container do chat
st.markdown(
    """
    <style>
    .fixed-title {
        position: fixed;
        top: 20px;
        left: 0;
        width: 100%;
        background-color: white;
        z-index: 100;
        padding: 10px;
        border-bottom: 1px solid #ddd;
        text-align: center;
    }
    .chat-container {
        margin-top: 80px; /* Ajuste se precisar de mais espaço */
    }
    .menu-btn {
        margin-bottom: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título fixo
st.markdown("<div class='fixed-title'><h1>Aplicativo - DHW - MODO TESTE</h1></div>", unsafe_allow_html=True)

# Adiciona a logo na sidebar (substitua 'logo.png' pelo caminho da sua imagem ou URL)
st.sidebar.image("Imagens/Logo.png", use_container_width=True)
# Seção da sidebar: define o menu com logo e botões para selecionar a funcionalidade
st.sidebar.title("Menu")



# Inicializa o estado da página, se não existir
if "pagina" not in st.session_state:
    st.session_state.pagina = "Chatbot"

# Botões na sidebar para trocar de página
if st.sidebar.button("Chatbot", key="btn_chatbot"):
    st.session_state.pagina = "Chatbot"
if st.sidebar.button("Adicionar conteúdo", key="btn_upload"):
    st.session_state.pagina = "Upload de Arquivos"

# Container principal para exibir a opção escolhida
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

# ----- CHATBOT -----
if st.session_state.pagina == "Chatbot":
    st.subheader("Pergunte o que quiser")
    
    # Inicializa o histórico de mensagens
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Exibe as mensagens existentes
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    # Campo de entrada para o chat
    query = st.chat_input("Digite sua pergunta...")
    if query:
        
        # Armazena a mensagem do usuário
        st.session_state.messages.append({"role": "user", "content": query})
        # Resposta simulada (substitua pela sua IA, se desejar)
        resposta = perguntar_gpt_4(query)
        
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        st.rerun()

# ----- UPLOAD DE ARQUIVOS -----
elif st.session_state.pagina == "Upload de Arquivos":
    st.subheader("Faça o upload de seus artigos de texto (.pdf/.txt)")
    # Campo para inserir o tema
    tema = st.text_input("Digite o tema do arquivo:")
    arquivo = st.file_uploader("Selecione um arquivo", type=["txt", "pdf"])
    if arquivo is not None and tema is not None:
        st.success("Arquivo Aberto com sucesso!")
        
        try:
            realizar_upload(arquivo, tema)
            st.success("Arquivo upado com sucesso para o VectorDataBase")

        except Exception as e:
            st.error(f"Ocorreu um erro {e}")


        

st.markdown("</div>", unsafe_allow_html=True)

# Script opcional para rolar a página para o final (no caso do chat)
scroll_script = """
<script>
    window.scrollTo(0, document.body.scrollHeight);
</script>
"""
st.write(scroll_script, unsafe_allow_html=True)
