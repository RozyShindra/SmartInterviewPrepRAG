
# Smart Interview Preparation Q\&A System (RAG-based)

[![Python](https://img.shields.io/badge/Python-3+-blue.svg)](https://www.python.org/)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?logo=pytorch\&logoColor=white)](https://pytorch.org/)
[![LangChain](https://img.shields.io/badge/LangChain-2AB8FF?logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A **smart interview preparation system** using **Retrieval-Augmented Generation (RAG)**. Users can input a **resume PDF** or **portfolio link**, and the system generates **technical, managerial, or HR interview questions and answers** using the **Qwen LLM**, with context retrieved via **FAISS vector database**.

---

## Features

* Upload **Resume PDF** or provide a **Portfolio Link** (GitHub/personal website)
* Choose **Interview Type**: Technical, Managerial, or HR
* Generate **context-aware questions and answers** based on uploaded resume/portfolio
* Clean, readable output with **Question and Answer on separate lines**
* Simple setup using **LangChain data loaders** (no custom parsers required)
* Interactive **Streamlit UI**


---

## Quickstart

```bash
# 1. Clone repository
git clone https://github.com/RozyShindra/SmartInterviewPrepRAG.git
cd SmartInterviewPrepRAG

# 2. Build Docker image 
docker build -t smart-interview-prep-rag .

# 3. Run the container (map port 5000 → 5000)
docker run -p 5000:5000 smart-interview-prep-rag

```

---

## Example Output

**Question:**
Rozy, Tell me about yourself?

**Helpful Answer:**
I am Rozy Kumari, an AI/ML engineer with a strong background in mathematics and statistics. My expertise lies in solving complex problems across semiconductor manufacturing and research fields utilizing **NLP, Generative AI, and Optimization techniques**. Throughout my academic career, I have gained experience through **Internships, Research Work, GATE CS/IT exams**. I am particularly skilled in leveraging these technologies to solve intricate problems and innovate in real-world projects.

<img width="1755" height="857" alt="image" src="https://github.com/user-attachments/assets/d0f235a8-4bd7-4b64-af32-998078a839a3" />


---

## Dependencies

* **Python packages:** `streamlit`, `transformers`, `torch`, `langchain`, `langchain-community`, `sentence-transformers`, `faiss-cpu`, `pypdf`
* **LLM model:** `Qwen/Qwen2.5-0.5B-Instruct`
* **Embedding model:** `sentence-transformers/all-MiniLM-L6-v2`

---

## License

This project is open-source and available under the **MIT License**.


