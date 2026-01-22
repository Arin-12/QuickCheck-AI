from services.symptom_analyzer import analyze_symptoms

def run_test():
    print("🧪 Running QuickCheck AI Test...\n")

    test_symptoms = [
        "I have a mild headache and low fever for two days.",
        "I feel chest pain and difficulty breathing since morning.",
        "I am feeling tired and stressed with occasional dizziness."
    ]

    for i, symptoms in enumerate(test_symptoms, start=1):
        print(f"\n================ TEST CASE {i} ================\n")
        print("User Symptoms:")
        print(symptoms)

        result = analyze_symptoms(symptoms)

        print("\nAI Response:")
        print(result)
        print("\n==============================================\n")


if __name__ == "__main__":
    run_test()
