from ai.planner import plan

while True:
    text = input("You: ")
    print(plan(text))