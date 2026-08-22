# LLM-Powered Chat Automation Hub

This project contains production-grade Python scripts that securely connect to Google's advanced genai API suite to build continuous, state-managed terminal chat sessions.

## 🚀 Technical Highlights
* *Secure Token Separation:* Leverages zero-exposure environment variable structures (.env) to mask secret API keys from the application code tier.
* *Contextual State Loop:* Utilizes native multi-turn chat sessions (chats.create()) to preserve long-range conversation history.
* *Resilient Parameterization:* Implements explicit model profiling controls (temperature=0.3) for deterministic, low-randomness answers.

## 🛠️ Stack & Libraries
* *Language:* Python 3.11+
* *AI Provider:* Google Gemini API via google-genai
* *Security Layer:* python-dotenv
