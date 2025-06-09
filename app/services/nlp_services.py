
from llama_index.core import VectorStoreIndex
from llama_index.llms.langchain import LangChainLLM
from llama_index.embeddings.langchain import LangchainEmbedding

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings

import os
from dotenv import load_dotenv
load_dotenv()

llm = LangChainLLM(
    llm=ChatGoogleGenerativeAI(
        model="models/gemini-1.5-pro-latest",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
)

embed_model = LangchainEmbedding(
    GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
)

def buildIndexFromDocuments(document_texts):
    return VectorStoreIndex.from_documents(document_texts, embed_model=embed_model)

def queryIndex(index, question):
    engine = index.as_query_engine(llm=llm)
    response = engine.query(question)
    return str(response)
