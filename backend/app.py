import asyncio
import edge_tts
import os
import subprocess

from voice.listen import listen
from ai.brain import process_command


# -----------------------------
# Marco Voice Configuration
# -----------------------------
VOICE = "hi-IN-MadhurNeural"
VOICE_FILE = os.path.abspath("voice.mp3")


async def speak(text):
    """Generate and play Marco's voice."""

    if not text:
        return

    text = str(text).strip()

    if not text:
        return

    print(f"🔊 Marco: {text}")

    try:
        communicate = edge_tts.Communicate(
            text=text,
            voice=VOICE,
            rate="-5%",
            volume="+0%",
        )

        await communicate.save(VOICE_FILE)

        if not os.path.exists(VOICE_FILE):
            print("❌ Voice file not created.")
            return

        process = subprocess.Popen(
            [
                "ffplay",
                "-nodisp",
                "-autoexit",
                "-loglevel",
                "quiet",
                VOICE_FILE,
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            creationflags=subprocess.CREATE_NO_WINDOW,
        )

        # Wait until Marco finishes speaking
        await asyncio.to_thread(process.wait)

    except FileNotFoundError:
        print("❌ ffplay not found.")
        print("Install FFmpeg and add it to PATH.")

    except Exception as e:
        print("❌ TTS Error:", e)


async def main():

    print("=" * 60)
    print("🤖 MARCO AI Started")
    print("=" * 60)

    await speak(
        "Hello Sir. I am Marco AI. How can I help you?"
    )

    while True:

        print("\n🎤 Listening...")

        try:
            command = listen()

        except Exception as e:
            print("❌ Listening Error:", e)
            continue

        if not command:
            continue

        command = command.strip()

        print(f"\n👤 You: {command}")

        if command.lower() in [
            "exit",
            "quit",
            "goodbye",
            "stop marco",
            "bye",
        ]:
            await speak("Goodbye Boss.")
            break

        try:

            response = process_command(command)

            if response:

                parts = str(response).split("||")

                for part in parts:

                    part = part.strip()

                    if part:
                        await speak(part)

        except Exception as e:

            print("❌ Marco Error:", e)

            await speak(
                "Sorry Boss, something went wrong."
            )


if __name__ == "__main__":
    asyncio.run(main())