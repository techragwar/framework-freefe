from .rag.service import rag_service


class AIService:

    def chat(
        self,
        message: str,
    ):

        return rag_service.answer(
            message
        )


ai_service = AIService()
