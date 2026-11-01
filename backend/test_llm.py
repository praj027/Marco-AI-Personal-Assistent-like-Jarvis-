from ai.llm import ask_llm

print("=" * 50)
print("🤖 MARCO AI LLM TEST")
print("=" * 50)

while True:
    text = input("You: ")

    if text.lower() == "exit":
        print("Goodbye!")
        break

    try:
        reply = ask_llm(text)

        print("\nMarco:")
        print(reply)
        print("-" * 50)

    except Exception as e:
        print("Error:", e)