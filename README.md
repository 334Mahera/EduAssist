# 🎓 EduAssist – Context-Aware Educational Chatbot

## 📌 Overview

EduAssist is an AI-powered educational chatbot designed to provide personalized academic assistance through natural conversations. Unlike traditional chatbots, EduAssist maintains conversational context and remembers user preferences, enabling more relevant and engaging interactions.

The project demonstrates the implementation of **context awareness**, **short-term memory**, and **long-term memory** using modern Generative AI techniques.

---

## 🚀 Features

* Context-aware multi-turn conversations
* Short-term memory for recent interactions
* Long-term memory for storing user preferences
* Personalized responses based on learning level
* Conversation summarization for memory optimization
* Educational question answering
* Interactive Streamlit user interface
* Powered by Google Gemini API

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Google Gemini API
* Generative AI
* Prompt Engineering

---

## 📂 Project Structure

```text
EduAssist/
│
├── app.py
└── screenshots/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/334Mahera/EduAssist.git
cd EduAssist
```

### Configure Gemini API Key

Replace:

```python
api_key="YOUR_GOOGLE_API_KEY"
```

with your own Google Gemini API Key.

### Run the Application

```bash
streamlit run app.py
```

---

## 🧠 Working Principle

1. User enters an academic query.
2. The chatbot stores conversation history.
3. User preferences (Beginner/Advanced) are saved in memory.
4. Previous messages and summaries are used as context.
5. Gemini generates context-aware responses.
6. Older conversations are summarized to reduce memory usage.

---

## 🎯 Applications

* Student Learning Assistant
* Programming Guidance
* AI & Machine Learning Education
* Academic Doubt Resolution
* Personalized Learning Systems

---

## 📸 Output

### Home Screen

![Home Screen](screenshot 1.png)

### Chatbot Interaction

![Chatbot Interaction](screenshots 2.png)

### Personalized Response

![Personalized Response](screenshots 3.png)
---

## 📈 Future Enhancements

* Voice-based interaction
* Multi-language support
* User authentication
* Learning progress tracking
* Integration with educational resources

