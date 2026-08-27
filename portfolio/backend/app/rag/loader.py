from pathlib import Path

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


KNOWLEDGE_DIR = (
    Path(__file__).resolve().parents[2]
    / "knowledge"
)


def load_documents():

    documents = []

    for path in KNOWLEDGE_DIR.glob("*.md"):

        text = path.read_text(
            encoding="utf-8"
        )

        documents.append(
            Document(
                page_content=text,
                metadata={
                    "source": path.name
                }
            )
        )

    return documents


def split_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=700,
        chunk_overlap=100,
    )

    return splitter.split_documents(
        documents
    )
