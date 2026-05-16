from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Sample URLs

urls = [
    'https://google.com',
    'https://github.com',
    'http://free-money.xyz/login',
    'http://verify-bank-account.ru',
    'https://openai.com'
]

# Labels
# 0 = Safe
# 1 = Phishing

labels = [0, 0, 1, 1, 0]

# Convert text into vectors

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(urls)

# Create AI model

model = LogisticRegression()

# Train model

model.fit(X, labels)

# Test suspicious URL

test_url = [
    'http://claim-free-prize.xyz'
]

test_vector = vectorizer.transform(test_url)

prediction = model.predict(test_vector)

print("\nURL Tested:")
print(test_url[0])

print("\nPrediction Result:")

if prediction[0] == 1:
    print("⚠ PHISHING WEBSITE DETECTED")
else:
    print("✅ SAFE WEBSITE")