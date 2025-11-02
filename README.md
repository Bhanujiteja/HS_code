# HS_code📦 HS Code Finder — AI-Powered HS Classification using RAG
📘 Overview

HS Code (Harmonized System Code) classification is critical for global trade, customs processing, import/export taxes, and compliance.
Manually searching through long PDF documents is inefficient and error-prone.

This project solves that ✅
Upload any HS Code reference PDF → ask a query → get the correct HS Code + justification with AI.

🎯 Problem Statement

Trade policy documents and HS Code manuals are long and complex.
Users struggle to:

Quickly find correct HS Codes for their products

Understand classification rules

Avoid misclassification penalties

✅ Proposed Solution

An AI-powered document-based RAG system that:

✔ Extracts HS codes from uploaded PDF
✔ Organizes information using embeddings + FAISS
✔ Returns HS code, description & reasoning
✔ Works fast using Groq LLaMA-3.1-8B model

🧠 Key Features
Feature	Description
📤 PDF Upload	Accepts official HS Code PDF files
🧩 Intelligent Chunking	Breaks large PDF into retrievable units
🔍 Smart Retrieval	Uses vector search to fetch accurate context
🤖 HS Code Classification	HS code + explanation using RAG
💡 Explainability	Shows why that code is selected
🖥 Streamlit UI	User-friendly web interface
🏗️ System Architecture
┌─────────┐     Upload PDF     ┌───────────────┐
│  User   │ ─────────────────▶ │ Streamlit App │
└─────────┘                    └───────┬───────┘
                                       │
                                       ▼
                              ┌──────────────────┐
                              │ PDF Text Extract  │
                              └───────┬──────────┘
                                      │ Chunking
                                      ▼
                               ┌──────────────┐
                               │ Embeddings   │ ◀── Sentence-Transformers
                               └──────┬───────┘
                                      │ Store/Search
                                      ▼
                                ┌─────────┐
                                │ FAISS   │
                                └────┬────┘
                                     │ Retrieve Docs
                                     ▼
                           ┌──────────────────────┐
                           │ Groq LLaMA-3.1-8B LLM │
                           └─────────┬────────────┘
                                     │ Response
                                     ▼
                               Final HS Code Output ✅

🧩 Tech Stack
Layer	Technology
UI	Streamlit
Retrieval	LangChain + FAISS
LLM	Groq LLaMA-3.1-8B-Instant
Embeddings	Sentence Transformers (MiniLM)
File Loader	PyPDFLoader
Language	Python 3.10
📂 Project Structure
HS_Code_RAG/
│── app.py
│── requirements.txt
│── .env
│── sample_hs_code.pdf (example)
│── README.md

⚙️ Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Add your Groq API Key

Create a .env file:

GROQ_API_KEY=your_api_key_here

4️⃣ Run the Streamlit App
streamlit run app.py

📌 How to Use

1️⃣ Upload an HS Code PDF
2️⃣ Type a question like:

"HS code for women's synthetic jackets?"
3️⃣ AI retrieves correct code & explains why ✅
4️⃣ Use response for classification in trade documentation

📊 Sample Output
HS Code: 62043200  
Description: Women’s jackets and blazers — of synthetic fibers  
Reason: Query context matches "women + synthetic jackets"

🧪 Testing Scenarios
Query Type	Example
Product	"Cotton bedsheets HS Code"
Material-based	"Leather footwear HS code"
Category-based	"Electronics spare parts classification"
🚀 Future Improvements

✅ Save multiple PDFs as a knowledge base
✅ Show sources and chunk references
✅ Multi-PDF RAG with persistent FAISS DB
✅ UI enhancement with response confidence score
✅ Deploy on Streamlit Cloud / HuggingFace Spaces

👨‍💻 Author

Bhanuji Venkata Teja
AI Engineer • RAG Systems • Gen-AI Developer
📧 Email: bhanujiteja@gmail.com

🌐 GitHub: https://github.com/Bhanujiteja

⭐ Support the Project

If you like this work, please ⭐ the repository 🙌
Your support motivates more AI innovations!