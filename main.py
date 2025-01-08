import streamlit as st

### Configuração da página
st.set_page_config(
    page_title="Teste Imagem Arredondada",
    page_icon="🎈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Sidebar recuada 
st.sidebar.title("Esta é a sidebar!")

st.balloons()

# Estilo CSS para centralizar e arredondar a imagem
st.markdown(
    """
    <style>
    .center {
        padding: 5x;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        margin-top: 5px;
    }
    .round-img {
        border-radius: 50%;
        width: 400px; /* Ajuste o tamanho da imagem */
        height: 400px;
        object-fit: cover; /* Garante que a imagem fique bem ajustada */
    }
    .titles {
        text-align: center;
        margin-top: 5px;
    }
    
    .titles h3 {
        margin: 5px;
    }
    .titles h1 {
        padding: 5px;
        color: #FFD700;
        font-size: 3em; /* Ajuste o tamanho do h1 se necessário */
    }
    .titles h5 {
        margin: 5px;
        color: gray; /* Ajuste a cor do h5 */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Adicionando a imagem com CSS
st.markdown(
    """
     <div class="center">
        <img src="asset/im"alt="Imagem arredondada" class="round-img">
        <div class="titles">
            <h4>Subtítulo H3</h4>
            <h1>Título Principal H1</h1>
            <h5>Descrição em H5</h5>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Texto abaixo da imagem
##st.markdown("## Teste de Nome Completo")
