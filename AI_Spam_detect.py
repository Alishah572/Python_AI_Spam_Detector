spam_db = {
    "spam_words": ["win", "free", "click", "prize", "money", "offer", "urgent", "buy now", "guarantee", "limited"],
    "spam_messages": [
        "Win ₹1,00,000 now!",
        "Click this link to claim your free prize!",
        "Congratulations! You have been selected!",
        "Earn money from home easily!",
        "Limited time offer, act now!"
    ],
    "safe_messages": [
        "Hey, how are you?",
        "Let's meet tomorrow at 5pm",
        "Don't forget your homework",
        "Happy Birthday!",
        "Can you send me the notes?"
    ]
}

# Mini spam detection AI using a simple keyword-based approach
# from DB_Spam import spam_db

# Test message ( in real AI, take input from user )
msg = input("Enter your message: ").strip()

# Detection logic
if any(word in msg.lower() for word in spam_db["spam_words"]) or msg in spam_db["spam_messages"]:
    print("Spam Detected")
else:
    print("Safe Message")