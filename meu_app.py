import streamlit as st
import time
import random

def animar_texto(texto, delay=0.05):
    """Simula uma animação de digitação para o texto."""
    texto_animado = ""
    for letra in texto:
        texto_animado += letra
        st.write(texto_animado)
        time.sleep(delay)
        st.rerun()

# Configuração inicial do app
st.set_page_config(page_title="Uma mensagem especial", page_icon="💖", layout="centered")

# CSS para fundo pêssego e transições suaves
st.markdown(
    """
    <style>
        body {
            background-color: #FFDAB9;
            transition: background-color 1s ease;
        }
        .stApp {
            background-color: #FFDAB9;
            transition: background-color 1s ease;
        }
        .fade-in {
            animation: fadeIn 1.5s;
        }
        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("💖 Uma História Especial 💖")

# Botão para abrir a música no YouTube (somente na primeira página)
if "etapa" not in st.session_state:
    st.session_state.etapa = 0
    
if st.session_state.etapa == 0:
    st.markdown(
        """
        <a href="https://www.youtube.com/watch?v=D5P1R6CRsoM" target="_blank">
            <button style="background-color: #FF4B4B; color: white; padding: 10px; border-radius: 5px; font-size: 16px;">
                🎶 Ouvir "Fallin' All In You" do Shawn Mendes
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )

if st.session_state.etapa == 0:
    st.write("Opa, tudo bem? Você está aqui por um motivo...", unsafe_allow_html=True)
    st.write("Acho que é um bom motivo, então pode ficar tranquila. 💖", unsafe_allow_html=True)
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 1:
    st.write("🎶 'Baby, you light up my world like nobody else'")
    resposta = st.radio("Está pronta para relembrar algumas coisas e entrar nesse novo mundo?", ["Sim", "Não"])
    if st.button("Próximo"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 2:
    st.write("Há muitos anos atrás, nossos caminhos se cruzaram...")
    st.write("Mas somente no dia 10 de janeiro de 2025, algo muito importante aconteceu. ✨")
    nome = st.text_input("Agora por favor, digita seu nome")
    if nome:
        st.session_state.nome = nome
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 3:
    nome = st.session_state.get("nome", "Princesa")
    st.write(f"Então é você mesmo, a Princesa {nome}! 👑")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 4:
    st.write("Os dias foram passando e cada vez mais a princesa Luiza e esse rapaz que está aí atrás de você foram se aproximando...")
    st.write("Se conhecendo, compartilhando momentos e até as pequenas coisas foram fazendo os dias deles melhorarem. 💖")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 5:
    st.write("Será que estavam se apaixonando...?")
    st.write("A princípio os dois não sabiam de nada mas esse era o conto de fadas mais real que os dois já tinham visto")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 6:
    st.write("Luiza, eu sei que você estava agindo com cautela mas esse rapaz estava começando a se apaixonar desde antes daquele dia que você chegou de viagem e foi direto encontrar ele...")
    st.write("..mas ele também só não queria dar tão na cara. 💖")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()

elif st.session_state.etapa == 7:
    st.write("Foram ótimos momentos enquanto se conheciam.")
    st.write("O almoço EAD, as mensagens e conversas eternas, o pardinho, o dorama, as ligações, a parceria, os estudos de prótese e cirurgia...")
    st.write("as semanas sem geladeira, as noites de calor, as reuniões de rotaract, a skin care, o carnaval em casa, o torrão na praia e muito mais coisas")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()
        
elif st.session_state.etapa == 8:
    st.write("Agora, chegou o momento mais importante...vou deixar na mão do companheiro João Marco.")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()
        
elif st.session_state.etapa == 9:
    st.write("Vem cá Luiza...me dá sua mão. O seu desejo é sempre o meu desejo...")
    st.write("🎶 '..e um raio de sol nos seus cabelos, como um brilhante que partindo a luz explode em sete cores..'")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()
        
elif st.session_state.etapa == 10:
    st.write("Desde o nosso primeiro beijo, você não sai dos meus pensamentos e a cada dia que passamos juntos, eu tinha mais certeza de que você era a pessoa certa..")
    st.write("Nossa conexão é algo que eu nunca senti, tudo que estamos construindo é realmente muito especial e diferente.")
    st.write("Eu tenho então uma pergunta pra te fazer...")
    if st.button("Continuar"):
        st.session_state.etapa += 1
        st.rerun()
        
elif st.session_state.etapa == 11:

    resposta_final = st.text_input("Quer namorar comigo? (Digite 'Sim' ou 'Não')")
    
    if resposta_final.lower() == "sim":
        st.session_state.etapa += 1
        st.session_state.resposta_final = "💖 Você me faz a pessoa mais feliz do mundo! 💖"
        st.rerun()
    elif resposta_final.lower() == "não":
        st.session_state.etapa += 1
        st.session_state.resposta_final = "Tudo bem... eu continuo te achando incrível! 😊"
        st.rerun()

elif st.session_state.etapa == 12:
    st.write(st.session_state.resposta_final)
    st.write("Eu te amo muito e você é o amor da minha vida!")
    st.write(f"I can't see one thing wrong between the both of us, {st.session_state.nome}!")
    st.snow()