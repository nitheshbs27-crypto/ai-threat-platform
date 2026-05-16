import os

from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URL"))
db = client["threat_intelligence"]
alerts_collection = db["alerts"]

alerts = [
    {
        "ip": "192.168.1.100",
        "threat_type": "Brute Force",
        "severity": "Critical",
        "score": 99
    },
    {
        "ip": "192.168.1.101",
        "threat_type": "Malware",
        "severity": "High",
        "score": 85
    },
    {
        "ip": "192.168.1.102",
        "threat_type": "Suspicious Login",
        "severity": "Medium",
        "score": 60
    },
    {
        "ip": "192.168.1.103",
        "threat_type": "Port Scan",
        "severity": "Low",
        "score": 30
    }
]

alerts_collection.insert_many(alerts)

print("MongoDB Atlas alerts inserted successfully")