from pathlib import Path

from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

from .loader import load_documents
from .loader import split_documents
from ..config import settings


VECTOR_DIR = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "chroma"
)


def build_retriever():

    if not settings.ai_api_key:

        return None


    embeddings = OpenAIEmbeddings(
        api_key=settings.ai_api_key
    )


    documents = load_documents()

    chunks = split_documents(
        documents
    )


    vectorstore = Chroma.from_documents(

        documents=chunks,

        embedding=embeddings,

        persist_directory=str(
            VECTOR_DIR
        ),

        collection_name="portfolio",

    )


    return vectorstore.as_retriever(
        search_kwargs={
            "k": 4
        }
    )
