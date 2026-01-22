import streamlit as st
from services.symptom_analyzer import analyze_symptoms

# Page config
st.set_page_config(
    page_title="QuickCheck AI",
    page_icon="🩺",
    layout="centered"
)

# Header
st.title("🩺 QuickCheck AI")
st.subheader("LLM-Powered Health Symptom Pre-Screening Tool")
st.caption("⚠️ Not a diagnostic tool. For informational purposes only.")

st.divider()

# User input
symptoms = st.text_area(
    "Describe your symptoms",
    placeholder="Example: I have a mild headache and low fever for two days...",
    height=150
)

# Analyze button
if st.button("🔍 Analyze Symptoms"):
    if not symptoms.strip():
        st.warning("Please enter your symptoms before clicking Analyze.")
    else:
        with st.spinner("Analyzing symptoms using AI..."):
            result = analyze_symptoms(symptoms)

        st.divider()
        st.markdown("### 🧠 AI Pre-Screening Result")
        st.markdown(result)

# Footer disclaimer
st.divider()
st.caption(
    "🛑 Disclaimer: QuickCheck AI provides non-diagnostic health information only. "
    "It does not replace professional medical advice, diagnosis, or treatment."
)
