from ai.agent import run_agent

while True:

    text = input("You: ")

    if text == "exit":
        break

    print(run_agent(text))