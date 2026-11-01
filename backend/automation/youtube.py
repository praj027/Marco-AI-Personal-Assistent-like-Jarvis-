import webbrowser
import time
import requests
from urllib.parse import quote_plus
from bs4 import BeautifulSoup


def play_youtube(query):
    query = query.strip()

    if not query:
        print("❌ No YouTube search query.")
        return False

    print(f"▶ Playing: {query}")

    # YouTube search URL
    search_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query)
    )

    try:
        # Get YouTube search page
        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/151.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(
            search_url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        # Find first YouTube video ID
        text = response.text

        marker = '"videoId":"'
        position = text.find(marker)

        if position == -1:
            print("⚠️ Video not found. Opening YouTube search.")
            webbrowser.open(search_url)
            return False

        start = position + len(marker)
        video_id = text[start:start + 11]

        # Validate video ID
        if len(video_id) != 11:
            print("⚠️ Invalid video ID.")
            webbrowser.open(search_url)
            return False

        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"🎵 Opening video: {video_url}")

        webbrowser.open(video_url)

        # Give Chrome/YouTube time to load
        time.sleep(4)

        return True

    except Exception as e:
        print(f"❌ YouTube error: {e}")

        # Fallback: open search page
        webbrowser.open(search_url)
        return False