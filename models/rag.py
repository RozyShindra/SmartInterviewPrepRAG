import torch
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from transformers import pipeline
from langchain.llms import HuggingFacePipeline
from langchain.chains import RetrievalQA
import re
import warnings
warnings.filterwarnings("ignore")

class RAGPipeline:
    def __init__(self, documents):
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vectordb = FAISS.from_documents(chunks, embedder)
        retriever = self.vectordb.as_retriever()

        device = "cuda" if torch.cuda.is_available() else "cpu"
        model = "qwen/qwen2.5-0.5B-Instruct"
        gen_pipeline = pipeline("text-generation", model=model, max_new_tokens=200, device=device)
        llm = HuggingFacePipeline(pipeline=gen_pipeline)

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=llm, retriever=retriever, return_source_documents=False
        )


    def ask(self, query):
        raw_answer = self.qa_chain.run(query)


        pattern = r'(Question:.*?Helpful Answer:.*)'
        match = re.search(pattern, raw_answer, re.DOTALL)

        if match:
            answer = match.group(1).strip()
        else:
            answer = f'Question: {query}\nHelpful Answer:'
    
        return answer


