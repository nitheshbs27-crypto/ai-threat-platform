def security_chatbot(question):

    question = question.lower()

    if "phishing" in question:
        return "Phishing is a cyberattack where fake emails or websites trick users into sharing passwords or bank details."

    elif "ransomware" in question:
        return "Ransomware is malware that locks files and demands payment to unlock them."

    elif "brute force" in question:
        return "A brute force attack tries many passwords until the correct one is found."

    elif "malware" in question:
        return "Malware is malicious software designed to damage, steal, or control data."

    elif "protect" in question or "secure" in question:
        return "Use strong passwords, enable 2FA, update software, avoid suspicious links, and monitor login activity."

    else:
        return "I am your AI Security Assistant. Ask me about phishing, ransomware, brute force, malware, or protection tips."