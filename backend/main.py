from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.alerts import router as alert_router
from routes.chatbot_route import router as chatbot_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(alert_router)
app.include_router(chatbot_router)


@app.get("/")
def home():
    return {"message": "Backend Running Successfully"}