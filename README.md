# 🩺 QuickCheck AI

QuickCheck AI is an **LLM-powered health symptom pre-screening tool** that allows users to describe symptoms in natural language and receive **non-diagnostic health guidance** along with an **urgency assessment**.

⚠️ This tool is for **informational purposes only** and does **not** replace professional medical advice.

---

## 🚀 Features
- Natural language symptom input
- AI-powered symptom analysis using **Google Gemini**
- Urgency classification: **LOW / MEDIUM / HIGH**
- Emergency-aware safety logic
- Clear medical disclaimers
- Simple and clean **Streamlit UI**

---

## 🧠 How It Works
1. User enters symptoms in plain text  
2. Gemini LLM analyzes the input using a safety-constrained prompt  
3. The system provides:
   - Symptom summary  
   - General possible causes (non-diagnostic)  
   - Urgency level  
   - Recommended next steps  
4. A rule-based layer overrides urgency for critical emergencies

---

## 🛠 Tech Stack
- Python  
- Google Gemini API  
- Streamlit   

---

## How to Run
```bash
pip install -r requirements.txt
setx GEMINI_API_KEY "your_api_key_here"
streamlit run app.py
```
