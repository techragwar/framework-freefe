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

Answer using the supplied portfolio context.

Do not invent projects, clients, employment,
credentials, metrics, or accomplishments.

If information is unavailable, say so.

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
        self.initialized = False


    def initialize(self):

        if self.initialized:
            return

        if not settings.ai_api_key:
            return

        self.retriever = build_retriever()

        self.llm = ChatOpenAI(
            model=settings.ai_model,
            api_key=settings.ai_api_key,
            temperature=0,
        )

        self.initialized = True


    def answer(self, question: str):

        self.initialize()

        if not self.retriever:

            return {
                "response": (
                    "The AI service is not configured."
                ),
                "sources": [],
            }


        documents = self.retriever.invoke(
            question
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


        response = self.llm.invoke(
            messages
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
