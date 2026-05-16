import time

print("\n=== LIVE THREAT MONITOR ===\n")

alerts = [

    "⚠ Phishing attack detected",
    "⚠ Multiple failed logins",
    "⚠ Suspicious IP activity",
    "⚠ Malware communication detected"

]

for alert in alerts:

    print(alert)

    time.sleep(2)

print("\nMonitoring Completed")