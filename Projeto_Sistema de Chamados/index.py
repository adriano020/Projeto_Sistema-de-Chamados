import streamlit as st

st.title("Sistema de Chamado")

#Iniciar uma lista de chamados
if "chamados" not in st.session_state:
    st.session_state.chamados = []

#Abrir chamado
st.subheader("Abrir Chamado")
titulo=st.text_input("Título do Chamado")
descricao=st.text_area("Descriçao de Serviço")

#Botao
if st.button("Abrir Chamado"):
    if titulo != "" and descricao != "":
        chamado = {
            "titulo": titulo,
            "descricao": descricao,
            "status": "aberto"
        }
        st.session_state.chamados.append(chamado)
        st.success("Chamado aberto com Sucesso")