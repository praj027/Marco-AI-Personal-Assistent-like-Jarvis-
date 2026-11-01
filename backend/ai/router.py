import json

from ai.tools import TOOLS
from ai.memory import remember, recall


def execute(plan):
    """
    Execute one action OR multiple actions.

    Old format:
        {"action": "open_app", "app_name": "chrome"}

    New format:
        {
            "actions": [
                {"action": "open_app", "app_name": "chrome"},
                {"action": "play_youtube", "query": "romantic songs"}
            ]
        }

    The old single-action format remains fully supported.
    """

    if isinstance(plan, str):
        try:
            plan = json.loads(plan)
        except Exception:
            print("❌ Invalid JSON")
            return None

    if not isinstance(plan, dict):
        return None

    # -------------------------------------------------
    # MULTI-ACTION PLAN
    # -------------------------------------------------

    if isinstance(plan.get("actions"), list):

        results = []

        for index, action_plan in enumerate(plan["actions"], start=1):

            if not isinstance(action_plan, dict):
                print(f"❌ Invalid action #{index}")
                return None

            print(f"➡️ Executing action {index}: {action_plan}")

            result = execute(action_plan)

            if result is None:
                print(f"❌ Action {index} failed")
                return None

            results.append(str(result))

        return " ".join(results)

    # -------------------------------------------------
    # SINGLE ACTION
    # -------------------------------------------------

    action = plan.get("action")

    if not action:
        return None

    # -------------------------------------------------
    # MEMORY
    # -------------------------------------------------

    if action == "remember":
        key = plan.get("key")
        value = plan.get("value")

        if not key or value is None:
            return None

        remember(key, value)
        return "Okay Sir, I'll remember that."

    if action == "recall":
        key = plan.get("key")

        if not key:
            return None

        value = recall(key)

        if value:
            return value

        return "I don't know that yet."

    # -------------------------------------------------
    # TOOL EXECUTION
    # -------------------------------------------------

    tool_info = TOOLS.get(action)

    if tool_info is None:
        print(f"❌ Unknown action: {action}")
        return None

    tool = tool_info["function"]

    kwargs = {
        key: value
        for key, value in plan.items()
        if key != "action"
    }

    try:
        print(f"🛠️ Tool: {action}")
        print(f"📦 Arguments: {kwargs}")

        result = tool(**kwargs)

        if result is False:
            return None

        if result is None:
            return "Action completed."

        return str(result)

    except Exception as error:
        print(f"❌ Tool execution error: {error}")
        return None
