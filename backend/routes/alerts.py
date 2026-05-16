import os

from fastapi import APIRouter
from pymongo import MongoClient

router = APIRouter()

client = MongoClient(os.getenv("MONGO_URL"))
db = client["threat_intelligence"]
alerts_collection = db["alerts"]


def convert_alert(alert):
    alert["_id"] = str(alert["_id"])
    return alert


@router.get("/alerts")
def alerts():
    alerts_data = list(alerts_collection.find())
    return [convert_alert(alert) for alert in alerts_data]


@router.get("/analytics")
def analytics():
    alerts_data = list(alerts_collection.find())

    critical = 0
    high = 0
    medium = 0
    low = 0

    for alert in alerts_data:
        severity = alert.get("severity", "Low")

        if severity == "Critical":
            critical += 1
        elif severity == "High":
            high += 1
        elif severity == "Medium":
            medium += 1
        else:
            low += 1

    return {
        "labels": ["Critical", "High", "Medium", "Low"],
        "values": [critical, high, medium, low]
    }