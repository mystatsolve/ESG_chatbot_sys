from langchain_community.document_loaders import PyPDFLoader
import os
import openai
from langchain_openai import OpenAI
import getpass
os.environ["OPENAI_API_KEY"] = "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"
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import ElasticVectorSearch, Pinecone, Weaviate, FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA, ConversationalRetrievalChain
import json

import json

def generate_description(input):
   
    class Document:
        def __init__(self, page_content, metadata):
            self.page_content = page_content
            self.metadata = metadata

    # JSON 파일에서 데이터 불러오기
    with open('pages_new.json', 'r', encoding='utf-8') as file:
        loaded_data = json.load(file)
    
    # JSON 데이터를 Document 객체 리스트로 변환
    documents_list = [Document(doc['page_content'], doc['metadata']) for doc in loaded_data]

    # Chroma 인덱스 생성 및 설정
    directory = 'index_store'
    vector_index = Chroma.from_documents(documents_list, OpenAIEmbeddings(), persist_directory=directory)
    vector_index.persist()  # 인덱스 저장

   
    retriever = vector_index.as_retriever(search_type="similarity", search_kwargs={"k":6})
    #qa_interface = RetrievalQA.from_chain_type(llm=ChatOpenAI(), chain_type="stuff", retriever=retriever, return_source_documents=True)
    #제일 높은 버전 gpt-4--125-preview 사용
    qa_interface = RetrievalQA.from_chain_type(llm=ChatOpenAI(model="gpt-4-0125-preview"), chain_type="stuff", retriever=retriever, return_source_documents=True)

   
    reply = qa_interface(f"{input}")

    return reply
#현대의 ESG 전략을 알려줘
#uvicorn main:app --reload 
#가상환경 nlp1
#127:0.0.1:8000/docs