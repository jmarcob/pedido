import streamlit as st

def pagina_inicial():
    st.title("Bem-vindo ao Evento Rotaract!")
    st.write("Prepare-se para uma experiência incrível de companheirismo, aprendizado e serviço!")
    st.image("https://via.placeholder.com/600x400", caption="Imagem do Rotaract", use_column_width=True)
    st.write("Clique em 'Próximo' para começar!")

def pagina_dados_pessoais():
    st.title("Dados Pessoais")
    nome = st.text_input("Nome completo:")
    clube = st.text_input("Clube Rotaract:")
    distrito = st.text_input("Distrito Rotaract:")
    if st.button("Próximo"):
        st.session_state.nome = nome
        st.session_state.clube = clube
        st.session_state.distrito = distrito
        st.success("Dados salvos!")

def pagina_mensagem_1():
    st.title("Mensagem 1")
    st.write(f"Olá, {st.session_state.nome}!")
    st.write("Lembre-se: 'A maior recompensa para o trabalho de alguém não é o que eles ganham com isso, mas o que eles se tornam com isso.' - John Ruskin")
    st.write("Continue fazendo a diferença em seu clube e distrito!")

def pagina_mensagem_2():
    st.title("Mensagem 2")
    st.write(f"Olá, {st.session_state.nome}!")
    st.write("'Sozinhos, podemos fazer tão pouco; juntos, podemos fazer muito.' - Helen Keller")
    st.write("Aproveite este evento para fortalecer laços e construir um futuro melhor!")

def pagina_mensagem_3():
    st.title("Mensagem 3")
    st.write(f"Olá, {st.session_state.nome}!")
    st.write("'O futuro pertence àqueles que acreditam na beleza de seus sonhos.' - Eleanor Roosevelt")
    st.write("Que este evento inspire você a sonhar grande e realizar seus objetivos!")

def pagina_final():
    st.title("Obrigado por participar!")
    st.write(f"Agradecemos a sua presença, {st.session_state.nome}!")
    st.write("Esperamos que este evento tenha sido enriquecedor e inspirador.")
    st.balloons()

paginas = {
    "Página Inicial": pagina_inicial,
    "Dados Pessoais": pagina_dados_pessoais,
    "Mensagem 1": pagina_mensagem_1,
    "Mensagem 2": pagina_mensagem_2,
    "Mensagem 3": pagina_mensagem_3,
    "Página Final": pagina_final,
}

st.sidebar.title("Navegação")
pagina_selecionada = st.sidebar.radio("Selecione a página:", list(paginas.keys()))

if "nome" not in st.session_state:
    st.session_state.nome = ""
if "clube" not in st.session_state:
    st.session_state.clube = ""
if "distrito" not in st.session_state:
    st.session_state.distrito = ""

paginas[pagina_selecionada]()