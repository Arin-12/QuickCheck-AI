from utils.disclaimer import DISCLAIMER_TEXT

def format_response(llm_response: str, urgency: str) -> str:

    urgency_badge = {
        "LOW": "🟢 LOW – Monitor and self-care",
        "MEDIUM": "🟡 MEDIUM – Medical consultation recommended",
        "HIGH": "🔴 HIGH – Seek immediate medical attention"
    }

    formatted_output = f"""
{llm_response}

------------------------------
🚨 Final Urgency Assessment:
{urgency_badge.get(urgency, "⚪ UNKNOWN")}

{DISCLAIMER_TEXT}
"""
    return formatted_output
