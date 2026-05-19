import streamlit as st

st.title("Lista de Tarefas")

#Criar lista na memoria
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

#Campo de texto
nova_tarefa = st.text_input("Digite uma Tarefa")

#Botao Adicionar
if st.button("Adicionar"):

    if nova_tarefa != "":

        tarefa = {
            "nome": nova_tarefa,
            "concluida": False
        }
        st.session_state.tarefas.append(tarefa)
st.subheader("Minhas Tarefas")

for i, tarefa in enumerate(st.session_state.tarefas):

    col1, col2 = st.columns([5, 1])

    with col1:
        concluida = st.checkbox(
            tarefa["nome"],
            value=tarefa["concluida"],
            key=i
            )

        tarefa["concluida"] = concluida
    
    with col2:
        if st.button("x", key=f"delete{i}"):
            st.session_state.tarefas.pop(i)
            st.rerun()