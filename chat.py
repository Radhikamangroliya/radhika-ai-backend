from fastapi import APIRouter
from schemas import ChatRequest, ChatResponse
from model import ask_gpt

router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
async def ask_chatbot(payload: ChatRequest):
    answer = await ask_gpt(payload.question)
    return ChatResponse(answer=answer)
