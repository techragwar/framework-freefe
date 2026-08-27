from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from ..config import settings
from .retriever import build_retriever


PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are the AI assistant for the Ragwar Tech portfolio.

Answer questions using the supplied portfolio context.

Rules:

1. Only make claims supported by the context.
2. Do not invent employment history,
   clients, credentials, projects, or metrics.
3. If the context does not contain the answer,
   say that the information is not available.
4. Be concise but technically useful.

Portfolio context:

{context}
""",
        ),
        (
            "human",
            "{question}",
        ),
    ]
)


class PortfolioRAG:

    def __init__(self):

        self.retriever = None

        self.llm = None

        if settings.ai_api_key:

            self.retriever = build_retriever()

            self.llm = ChatOpenAI(
                model=settings.ai_model,
                api_key=settings.ai_api_key,
                temperature=0,
            )


    def answer(
        self,
        question: str,
    ):

        if not self.retriever:

            return (
                "The portfolio RAG system is not "
                "configured yet. Add AI_API_KEY "
                "to backend/.env."
            )


        documents = (
            self.retriever.invoke(
                question
            )
        )


        context = "\n\n".join(
            document.page_content
            for document in documents
        )


        messages = PROMPT.invoke(
            {
                "context": context,
                "question": question,
            }
        )

return {
    "response": response.content,
    "sources": [
        {
            "source": document.metadata.get(
                "source",
                "unknown",
            )
        }
        for document in documents
    ],
}
   
rag_service = PortfolioRAG()
