from fastapi import APIRouter
from jose import jwt
from pymongo import MongoClient
from datetime import datetime

router = APIRouter()

SECRET = "SECRET123"

client = MongoClient("mongodb://localhost:27017")
db = client["threat_intelligence"]
alerts_collection = db["alerts"]

@router.post("/login")
def login(data: dict):

    email = data["email"]

    token = jwt.encode(
        {
            "email": email
        },
        SECRET,
        algorithm="HS256"
    )

    # Create different threat based on email text
    if "critical" in email:
        severity = "Critical"
        score = 99
        threat_type = "Critical Login Threat"

    elif "high" in email:
        severity = "High"
        score = 85
        threat_type = "High Risk Login"

    elif "medium" in email:
        severity = "Medium"
        score = 60
        threat_type = "Suspicious Login"

    else:
        severity = "Low"
        score = 30
        threat_type = "Normal Login Activity"

    alert = {
        "ip": "127.0.0.1",
        "email": email,
        "threat_type": threat_type,
        "severity": severity,
        "score": score,
        "timestamp": str(datetime.now())
    }

    alerts_collection.insert_one(alert)

    return {
        "token": token,
        "message": "Login success and alert stored",
        "severity": severity
    }