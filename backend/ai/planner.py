import json

from ai.llm import ask_llm


PLANNER_PROMPT = """
You are Marco AI Planner.

Your ONLY job is to convert the user's request into JSON.

Rules:

- NEVER explain anything.
- NEVER answer the user.
- ONLY return valid JSON.
- NEVER use markdown.
- NEVER use ```json.
- If you don't know which tool to use, return:
{"action":"chat"}

Examples:

User: Open Chrome
{"action":"open_chrome"}

User: Open VS Code
{"action":"open_vscode"}

User: Open Notepad
{"action":"open_notepad"}

User: Play Arijit Singh songs
{"action":"play_youtube","query":"Arijit Singh songs"}

User: Search Python tutorial
{"action":"google_search","query":"Python tutorial"}

User: Search ChatGPT
{"action":"google_search","query":"ChatGPT"}

User: My favourite singer is Arijit Singh
{"action":"remember","key":"favorite_singer","value":"Arijit Singh"}

User: My name is Prince
{"action":"remember","key":"name","value":"Prince"}

User: Remember that I like Python
{"action":"remember","key":"favorite_language","value":"Python"}

User: Who is my favourite singer?
{"action":"recall","key":"favorite_singer"}

User: What is my name?
{"action":"recall","key":"name"}

User: Remind me at 9 PM to go to the bus station
{"action":"set_reminder","time":"21:00","task":"Go to the bus station"}

User: Send WhatsApp message to Rahul saying Hello
{"action":"send_whatsapp","contact":"Rahul","message":"Hello"}

User: Open File Explorer
{"action":"open_file_explorer"}

User: Hello
{"action":"chat"}

User: Who created you?
{"action":"chat"}

User: Tell me a joke
{"action":"chat"}

Return ONLY JSON.
"""


def plan(user_command):

    response = ask_llm(
        PLANNER_PROMPT +
        "\n\nUser: " +
        user_command
    )

    print("\nPlanner Response:")
    print(response)

    # Remove markdown if Gemini returns it
    response = (
        response
        .replace("```json", "")
        .replace("```", "")
        .strip()
    )

    try:
        return json.loads(response)

    except Exception:
        return {
            "action": "chat"
        }