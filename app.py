import os
from langchain_groq.chat_models import ChatGroq
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import streamlit as st
import tempfile

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Set up Groq API key
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("⚠️ Groq API key missing. Please set GROQ_API_KEY in your environment.")
    st.stop()

# Initialize ChatGroq model
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0.0,
    max_retries=2
)

# Streamlit UI
st.set_page_config(page_title="HS Code Classifier", page_icon="📦", layout="wide")
st.title("📦 HS Code Finder with RAG")
st.write("Upload a trade policy PDF")

# Upload PDF
uploaded_file = st.file_uploader("Upload HS Code PDF", type=["pdf"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_file.read())
        pdf_path = tmp.name

    # Load PDF
    st.info("Processing PDF... Please wait ⏳")
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    docs = text_splitter.split_documents(documents)

    # Embeddings + FAISS
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(docs, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

    # Prompt
    prompt_template = """
    You are an HS Code classification assistant. 
    Use the provided context to answer the user's query.

    Query: {question}

    Context:
    {context}

    Instructions:
    - Identify the most correct HS Code from the context.
    - Provide the HS Code and its description.
    - Explain briefly why this HS Code matches the query.

    Answer:
    """

    PROMPT = PromptTemplate(
        template=prompt_template,
        input_variables=["question", "context"]
    )

    # RetrievalQA (RAG)
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": PROMPT}
    )

    # User Query
    query = st.text_input("🔎 Enter your query")

    if query:
        with st.spinner("Searching for the correct HS Code..."):
            response = qa_chain.run(query)

        st.subheader("📑 Response")
        st.write(response)
