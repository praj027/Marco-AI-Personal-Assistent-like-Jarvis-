import os
import time

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODELS = [
    "gemini-flash-latest",
]


def ask_llm(prompt):

    last_error = None

    for _ in range(3):

        try:

            print("Using model: gemini-flash-latest")

            response = client.models.generate_content(
                model="gemini-flash-latest",
                contents=prompt,
            )

            return response.text

        except Exception as e:

            print(e)

            last_error = e

            time.sleep(2)

    raise Exception(last_error)