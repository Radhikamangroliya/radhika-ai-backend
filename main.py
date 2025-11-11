from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import router as chat_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# CORS (frontend to backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# include chatbot routes
app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Radhika AI backend is running!"}