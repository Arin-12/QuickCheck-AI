def classify_urgency(symptoms: str, llm_output: str) -> str:


    # True emergency indicators ONLY
    emergency_keywords = [
        "chest pain",
        "difficulty breathing",
        "shortness of breath",
        "unconscious",
        "loss of consciousness",
        "severe bleeding",
        "seizure",
        "heart attack",
        "stroke"
    ]

    combined_text = (symptoms + " " + llm_output).lower()

    # Override only if clear emergency
    for keyword in emergency_keywords:
        if keyword in combined_text:
            return "HIGH"

    # Otherwise, trust LLM output
    if "🚦 urgency level" in llm_output.lower():
        if "high" in llm_output.lower():
            return "HIGH"
        elif "medium" in llm_output.lower():
            return "MEDIUM"
        else:
            return "LOW"

    # Safe fallback
    return "LOW"
