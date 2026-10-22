import ollama

print("Subject-Based Question Answering System")
print("Welcome Student!")

while True:
    subject = input("\nEnter Subject (or type exit): ")

    if subject.lower() == "exit":
        print("Thank you! Goodbye.")
        break

    question = input("Enter your Question: ")

    if question.lower() == "exit":
        print("Thank you! Goodbye.")
        break

    try:
        response = ollama.chat(
            model="llama3.2",
            messages=[
                {
                    "role": "user",
                    "content": f"""
You are a subject expert in {subject}.
Answer the student's question only if it is related
to {subject}.

If the question is unrelated, politely say:
Please ask a question related to {subject}.

Explain the answer in simple English.

Question: {question}
"""
                }
            ]
        )

        print("\nAnswer:")
        print(response["message"]["content"])

    except Exception as e:
        print("Error:", e)
        print("Please check whether Ollama is running.")

