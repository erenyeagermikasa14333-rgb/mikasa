
import streamlit as st

st.set_page_config(page_title="Mikasa AI", page_icon="🤖")

st.title("🤖 Mikasa AI")
st.write("Vanakkam! Naan Mikasa!")
st.write("வணக்கம்! நான் மிகாசா!")

if "messages" not in st.session_state:
    st.session_state.messages = []

def mikasa_reply(message):
    msg = message.lower()

    if any(word in msg for word in ["வணக்கம்", "hello", "hi", "ஹாய்"]):
        return "வணக்கம்! எப்படி இருக்கிறாய்? 😊"

    elif any(word in msg for word in ["உன் பெயர்", "your name", "who are you"]):
        return "என் பெயர் Mikasa AI! 🤖"

    elif any(word in msg for word in ["எப்படி இருக்க", "how are you"]):
        return "நான் நன்றாக இருக்கிறேன்! நீ எப்படி இருக்கிறாய்?"

    elif any(word in msg for word in ["நன்றி", "thank you", "thanks"]):
        return "உனக்கு உதவியது மகிழ்ச்சி! 😊"

    elif any(word in msg for word in ["உதவி", "help"]):
        return "நிச்சயமாக! என்ன உதவி வேண்டும்?"

    elif any(word in msg for word in ["bye", "போயிட்டு வரேன்"]):
        return "சரி! மீண்டும் பேசலாம். 👋"

    else:
        return "உன் மெசேஜ் புரிந்துகொள்ள முயற்சி செய்கிறேன்! இன்னும் கொஞ்சம் தெளிவாகச் சொல்ல முடியுமா?"

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

prompt = st.chat_input("Mikasa kitta pesu...")

if prompt:
    st.session_state.messages.append(("user", prompt))

    reply = mikasa_reply(prompt)

    st.session_state.messages.append(("assistant", reply))

    st.rerun()
