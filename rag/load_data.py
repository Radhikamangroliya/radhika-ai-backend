from rag.knowledge import collection

# ✅ All of Radhika's knowledge (RAG database)
documents = [
    # ✅ Basic Summary
    "Radhika Mangroliya is an AI Engineer, ML Developer, and Full-Stack Developer completing MS CS at DePaul University (Graduating Nov 2025). She builds AI apps, RAG systems, agents, iOS apps, and full-stack platforms.",

    # ✅ About
    "Radhika is passionate about AI, LLMs, automation, UX, full-stack engineering, and DevOps. Mission: use AI to make experiences smarter, faster, more personal.",

    # ✅ Skills — Frontend
    "Frontend: React, Next.js, Vite, JavaScript, TypeScript, Tailwind CSS, HTML, CSS, Redux, UI/UX design.",

    # ✅ Skills — Backend
    "Backend: Python, FastAPI, Flask, Node.js, Express.js, REST APIs, microservices, JWT authentication, middleware.",

    # ✅ Skills — AI/ML
    "AI/ML: LLMs, GPT-4o, embeddings, RAG, FAISS, ChromaDB, agents, NLP, TF-IDF, VADER, tokenization, summarization, sklearn, XGBoost.",

    # ✅ Skills — DevOps
    "DevOps: Docker, GitHub Actions, CI/CD, Azure App Service, AWS Lambda, Terraform basics, Vercel deploy.",

    # ✅ Experience
    "BlueSAP Solutions: AI & Data Automation Engineer — Built AI pipelines, forecasting models, inventory workflows, serverless automation, recommendation systems.",
    "Cerebulb: Data Science Intern — CNN object detection, LSTM captioning, forecasting, IoT dashboards.",
    "Deloitte Virtual Internship — ETL, Tableau dashboards, Python scripting.",

    # ✅ Projects
    "MARS Multi-Agent Recommender System — multi-agent Gemini chatbot, FAISS, RAG, React frontend.",
    "CareerFit AI — resume parsing with TF-IDF + XGBoost, embeddings, React + FastAPI fullstack.",
    "Agent Chatbot — portfolio-integrated personal AI using RAG + tools.",
    "Home Cooking iOS App — Swift, Quartz 2D, Core Data, recipe planner.",
    "WhatsApp Chat Analyzer — NLP, VADER, Streamlit dashboard.",
    "Azure CI/CD Deployment — Terraform, Azure App Service, Docker.",
    "MERN To-Do App — Authentication, MongoDB, React.",
    ".NET Book Library API — JWT, EF Core, SQL Server.",
    "Gas Station Growth Dashboard — SQL, forecasting, analytics.",

    # ✅ Education
    "Education: MS Computer Science at DePaul University (GPA 3.5). BE Information Technology at GTU (GPA 3.8).",

    # ✅ Contact
    "Email: radhikamangroliya@gmail.com. GitHub: github.com/Radhikamangroliya. LinkedIn: linkedin.com/in/radhikamangroliya.",

    # ✅ Why hire
    "Why hire Radhika: strong AI + fullstack, real deployments, fast learner, excellent communicator, clean architecture, cloud DevOps experience."
]

# ✅ Generate IDs & metadata
ids = [f"doc_{i}" for i in range(len(documents))]
metadatas = [{"source": "radhika_profile"} for _ in documents]

# ✅ Insert into vector DB
collection.add(
    documents=documents,
    ids=ids,
    metadatas=metadatas
)

print("✅ RAG knowledge loaded!")
