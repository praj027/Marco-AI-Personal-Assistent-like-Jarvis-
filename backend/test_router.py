from ai.planner import plan
from ai.router import execute

while True:
    command = input("You: ")

    task = plan(command)

    print("Task:", task)

    result = execute(task)

    print("Result:", result)