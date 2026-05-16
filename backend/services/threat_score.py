def calculate_threat_score(

    failed_logins,
    foreign_ip,
    phishing_detected,
    anomaly_detected

):

    score = 0

    # Failed login scoring

    if failed_logins > 5:
        score += 30

    # Foreign IP scoring

    if foreign_ip:
        score += 25

    # Phishing scoring

    if phishing_detected:
        score += 25

    # AI anomaly scoring

    if anomaly_detected:
        score += 20

    return score


# Example Test

score = calculate_threat_score(
    failed_logins=8,
    foreign_ip=True,
    phishing_detected=True,
    anomaly_detected=True
)

print("\nThreat Score:", score)

# Threat level

if score >= 80:
    print("⚠ CRITICAL THREAT")

elif score >= 50:
    print("⚠ HIGH THREAT")

else:
    print("✅ LOW THREAT")