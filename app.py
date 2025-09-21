import streamlit as st
from loaders.resume_loader import load_resume
from loaders.portfolio_loader import load_portfolio
from models.rag import RAGPipeline
from qa.questions import get_questions

st.set_page_config(page_title="Smart Interview Prep", layout="wide")
st.title("💡 Smart Interview Preparation (Q&A)")

# Sidebar Inputs
uploaded_file = st.sidebar.file_uploader("Upload Resume (PDF)", type=["pdf"])
portfolio_link = st.sidebar.text_input("Or enter Portfolio Link (GitHub/Website)")

interview_type = st.radio(
    "Choose Interview Type:",
    ("Technical", "Managerial", "HR")
)

if st.button("Start Interview"):
    documents = []
    if uploaded_file:
        documents.extend(load_resume(uploaded_file))
    if portfolio_link:
        documents.extend(load_portfolio(portfolio_link))

    if not documents:
        st.warning("Please upload a resume or enter a portfolio link.")
    else:
        rag = RAGPipeline(documents)
        st.subheader(f"{interview_type} Interview Questions")

        for q in get_questions(interview_type):
            # st.markdown(f"**Q:** {q}\n")
            answer = rag.ask(q)
            # st.markdown(f"✅ **A:** {answer}\n\n")
            st.markdown(f"❓ **Q:** {q}  \n\n✅ **A:** {answer}\n\n")

            st.write("---")
