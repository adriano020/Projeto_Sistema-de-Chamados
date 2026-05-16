import streamlit as st
import random

#sidebar

st.sidebar.title("menu")

pagina = st.sidebar.selectbox(
    "escolha uma pagina",
    ["home", "grafico"]
)
#Home

if pagina == "home":

    st.title("pagina Home")
    st.write("sistema usando o Streamlit")

#input

    nome = st.text_input("digite seu nome:",)

    #selectbox
    curso = st.selectbox(
        "escolha um curso",
        ["python", "js", "banco de dados"]
    )

#slider
    nota = st.slider(
        "escolha sua nota",
        0,
        10,
        5
    )

#checkbox
    mostrar = st.checkbox("mostrar mensagem")

    if mostrar:
        st.success("checkbox marcado")


#botao
    if st.button("enviar"):
        st.write(f"Nome : {nome}")
        st.write(f"curso : {curso}")
        st.write(f"nota : {nota}")

    st.subheader ("colunas")

    col1, col2 = st.columns (2)

    with col1:
        st.info("informações coluna 1")

    with col2:
        st.warning("informações coluna 2")

elif pagina == "grafico":
    st.title("pagina de grafico")
    valores = []
   
    for i in range(5):
        valores.append(random.randint(1,100))
    st.bar_chart(valores)

