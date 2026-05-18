import streamlit as st

st.title("Sistema de Chamado")

#Iniciar uma lista de chamados
if "chamados" not in st.session_state:
    st.session_state.chamados = []

#Abrir chamado
st.subheader("Abrir Chamado")
titulo=st.text_input("Título do Chamado")
descricao=st.text_area("Descrição de Serviço")

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
st.subheader("lista de chamados")
if len(st.session_state.chamados) == 0:
    st.warning("Nenhum Chamado Aberto")
else:
    for i, chamado in enumerate(st.session_state.chamados):
        st.write(f"{chamado['titulo']}")
        st.write(f"Descrição: {chamado['descricao']}")
        st.write(f"Status: {chamado['status']}")

        #Alterar espaço
        novo_status = st. selectbox(
            "Alterar Status",
            ["Aberto", "Em Andamento", "Finalizado"],
            key=f"status{i}"
        )

        #Botao para Alterar
        if st.button("Atualizar Status", key=f"btn{i}"):
            st.session_state.chamados[i]["status"] = novo_status
            st.success("Status Atualizado!")
            st.rerun()
        st.divider()