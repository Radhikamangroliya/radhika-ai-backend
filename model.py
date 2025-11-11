import os
from dotenv import load_dotenv
from openai import OpenAI
from rag.knowledge import collection

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ System Persona for Radhika
SYSTEM_PROMPT = """
You are **Radhika AI** — the official AI agent for Radhika Mangroliya.

Rules:
- Always answer based on Radhika’s skills, projects, experience, and biography.
- Be short, friendly, confident.
- If question is about Radhika → ALWAYS use RAG context.
- If unrelated to Radhika → answer normally as an AI assistant.
"""

# ✅ RAG Search Function
def search_rag(query: str):
    results = collection.query(
        query_texts=[query],
        n_results=5
    )
    documents = results.get("documents", [[]])[0]
    return "\n".join(documents)

# ✅ Chat Function (used by /ask API)
async def ask_gpt(question: str) -> str:
    try:
        # 1️⃣ Retrieve RAG knowledge
        rag_context = search_rag(question)

        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"QUESTION:\n{question}\n\nRAG CONTEXT:\n{rag_context}\n\nANSWER:"}
        ]

        # 2️⃣ Generate answer
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            max_tokens=250
        )

        return response.choices[0].message.content

    except Exception as e:
        print("❌ ERROR:", e)
        return "⚠️ Error contacting AI model."
