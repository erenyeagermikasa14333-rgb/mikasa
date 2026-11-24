import streamlit as st

st.set_page_config(page_title="Mikasa AI")
st.title("🤖 Mikasa AI")
st.write("Vanakkam! Naan Mikasa!")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, message in st.session_state.messages:
    with st.chat_message(role):
        st.write(message)

prompt = st.chat_input("Mikasa kitta pesu...")

if prompt:
    st.session_state.messages.append(("user", prompt))

    reply = "Vanakkam! Un message kidaichathu."
    st.session_state.messages.append(("assistant", reply))
    st.rerun()
