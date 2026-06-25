import streamlit as st
import os

from auth.login import authenticate
from rag.ingest import ingest_pdf
from rag.retriever import get_context
from rag.llm import ask_llm

# Page configuration
st.set_page_config(
    page_title="🏦 Banking AI Assistant",
    layout="wide"
)

st.title("🏦 Banking GenAI Assistant")

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "role" not in st.session_state:
    st.session_state.role = None

if "username" not in st.session_state:
    st.session_state.username = ""

# Sidebar Login
st.sidebar.header("Login")

username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login"):
    role = authenticate(username, password)

    if role:
        st.session_state.logged_in = True
        st.session_state.role = role
        st.session_state.username = username
        st.sidebar.success("Login Successful")
    else:
        st.sidebar.error("Invalid Username or Password")

# Main Application
if st.session_state.logged_in:

    st.success(f"Welcome {st.session_state.username}")
    st.info(f"Role: {st.session_state.role}")

    # PDF Upload Section
    uploaded_file = st.file_uploader(
        "Upload Banking PDF",
        type=["pdf"]
    )

    if uploaded_file is not None:

        os.makedirs("data", exist_ok=True)

        file_path = os.path.join(
            "data",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            result = ingest_pdf(file_path)
            st.success(result)

        except Exception as e:
            st.error(f"PDF Processing Error: {e}")

    # Question Section
    st.subheader("Ask a Banking Question")

    question = st.text_input("Enter your question")

    if st.button("Ask Question"):

        if not question.strip():
            st.warning("Please enter a question.")

        else:
            try:
                with st.spinner("Searching..."):

                    context = get_context(question)

                    answer = ask_llm(
                        question,
                        context
                    )

                st.subheader("Answer")
                st.write(answer)

            except Exception as e:
                st.error(f"Error: {e}")

# Logout Button
if st.session_state.logged_in:
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.role = None
        st.session_state.username = ""
        st.rerun()