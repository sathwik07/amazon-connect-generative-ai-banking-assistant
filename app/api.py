from fastapi import FastAPI
from pydantic import BaseModel

from app.services.banking_service import BankingService
from app.services.conversation_service import ConversationService

app = FastAPI(title="Banking Virtual Assistant")

banking = BankingService()
assistant = ConversationService(banking)


class ChatRequest(BaseModel):
    message: str


@app.get("/health")
def health_check():
    return {"status": "running"}


@app.post("/chat")
def chat(request: ChatRequest):
    response = assistant.get_response(request.message)

    return {
        "response": response
    }
