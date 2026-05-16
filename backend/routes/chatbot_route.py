from fastapi import APIRouter
from services.chatbot import security_chatbot

router = APIRouter()

@router.post("/chatbot")
def chatbot(data: dict):

    question = data["question"]

    answer = security_chatbot(question)

    return {
        "answer": answer
    }