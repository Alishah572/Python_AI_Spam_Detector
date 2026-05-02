# 📩 Mini Spam Detection AI (Keyword-Based)

A simple Python-based spam detection system that identifies spam messages using keyword matching and predefined spam message patterns.

---

## 🚀 Project Overview
This project is a basic **rule-based spam detection system**. It checks user input messages against:

*   **A list of spam-related keywords**
*   **A list of known spam messages**

If a match is found, the message is classified as **Spam**, otherwise it is marked as **Safe**.

> [!WARNING]
> This is a beginner-level AI simulation using keyword matching (not machine learning).

---

## 🧠 How It Works
The program performs two primary checks:

1.  **Keyword Matching**: Checks if any spam-related word exists in the message.
2.  **Exact Message Matching**: Compares the input with known spam messages.

---

## 📂 Project Structure
```Python
project/
│
├── main.py          # Main spam detection script
├── DB_Spam.py       # Contains spam keywords and messages database
└── README.md        # Project documentation
```
---

## 📜 Spam Database (DB_Spam.py)

```python
spam_db = {
    "spam_words": [
        "win", "free", "click", "prize", "money", "offer",
        "urgent", "buy now", "guarantee", "limited"
    ],
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
```
---

## ▶️ How to Run

#### 1. Clone or download the project
    git clone <repo-url>
    cd project

#### 2. Run the script
    python main.py

#### 3. Enter a message
    Enter your message: Win a free prize now!

#### 🧪 Example Output
#### Input:
``` 
        Click this link to get free money
```    
#### Output: 
``` 
        Spam Detected 
```

#### Input:
```
        Hello, are you coming to class today?
```
#### Output:
``` 
        Safe Message
```
#### 📌 Features
* ⚡ Fast and lightweight
* 🧠 Keyword-based spam detection
* 👶 Beginner-friendly Python project
* 🔧 Easy to extend and modify

#### ⚠️ Limitations
* Not AI/ML-based (rule-based only)
* Cannot detect advanced spam patterns
* Depends heavily on predefined keywords

#### 💡 Future Improvements
* Add Machine Learning (Naive Bayes / NLP)
* Improve text preprocessing (stemming, stopwords)
* Build GUI (Tkinter / Streamlit)
* Add email/SMS spam filtering support
* Multi-language spam detection

### 👨‍💻 Author
Sayed Muhammad Ali Shah

Created as a beginner Python AI simulation project for learning purposes.