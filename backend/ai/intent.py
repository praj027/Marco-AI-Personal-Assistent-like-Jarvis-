import re


def clean(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)
    return text.strip()


def detect_intent(command):
    command = clean(command)

    # Open website
    if command.startswith("open "):
        name = command.replace("open ", "").strip()

        apps = {
            "chrome",
            "notepad",
            "calculator",
            "paint",
            "cmd",
            "powershell",
            "explorer",
            "vscode",
            "visual studio code",
        }

        if name in apps:
            return {
                "action": "open_app",
                "app_name": name,
            }

        return {
            "action": "open_website",
            "name": name,
        }

    # Search Google
    if command.startswith("search "):
        return {
            "action": "google_search",
            "query": command.replace("search", "", 1).strip(),
        }

    if command.startswith("google "):
        return {
            "action": "google_search",
            "query": command.replace("google", "", 1).strip(),
        }

    # Play YouTube
    if command.startswith("play "):
        return {
            "action": "play_youtube",
            "query": command.replace("play", "", 1).strip(),
        }

    if "song" in command or "songs" in command:
        return {
            "action": "play_youtube",
            "query": command,
        }

    return None