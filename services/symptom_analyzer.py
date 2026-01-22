from llm.prompt_template import Prompt_Template
from llm.llm_client import call_llm
from services.urgency_classifier import classify_urgency
from utils.formatter import format_response

def analyze_symptoms(symptoms: str) -> str:
    if not symptoms.strip():
        return "⚠️ Please enter valid symptoms."

    # Build prompt
    prompt = Prompt_Template.format(symptoms=symptoms)

    # LLM call
    llm_output = call_llm(prompt)

    # Safety urgency classification
    urgency = classify_urgency(symptoms, llm_output)

    # Final formatted response
    return format_response(llm_output, urgency)
