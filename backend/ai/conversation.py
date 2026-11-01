MAX_HISTORY = 10

conversation_history = []


def add(role, message):
    global conversation_history

    conversation_history.append({
        "role": role,
        "message": message
    })

    if len(conversation_history) > MAX_HISTORY:
        conversation_history = conversation_history[-MAX_HISTORY:]


def history():
    text = ""

    for item in conversation_history:
        text += f'{item["role"]}: {item["message"]}\n'

    return text


def clear():
    global conversation_history
    conversation_history = []