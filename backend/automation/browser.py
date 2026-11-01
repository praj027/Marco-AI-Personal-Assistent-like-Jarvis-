import webbrowser
from urllib.parse import quote


def search_google(query):
    url = f"https://www.google.com/search?q={quote(query)}"
    webbrowser.open(url)
    return True


def open_website(name):

    name = name.lower().strip()

    websites = {
        "google": "https://google.com",
        "youtube": "https://youtube.com",
        "github": "https://github.com",
        "chatgpt": "https://chat.openai.com",
        "gmail": "https://mail.google.com",
        "facebook": "https://facebook.com",
        "instagram": "https://instagram.com",
        "amazon": "https://amazon.in",
        "netflix": "https://netflix.com",
        "linkedin": "https://linkedin.com",
        "twitter": "https://twitter.com",
        "x": "https://twitter.com",
        "leetcode": "https://leetcode.com",
        "geeksforgeeks": "https://geeksforgeeks.org",
        "stackoverflow": "https://stackoverflow.com",
        "spotify": "https://spotify.com",
    }

    if name in websites:
        webbrowser.open(websites[name])
        return True

    webbrowser.open(f"https://www.google.com/search?q={quote(name)}")

    return True