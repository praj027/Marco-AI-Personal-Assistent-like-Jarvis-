from voice.record import record_audio
from voice.whisper_engine import transcribe


def listen():

    try:

        record_audio("voice.wav", duration=5)

        command = transcribe("voice.wav")

        if not command:
            return ""

        print(f"📝 You said: {command}")

        return command

    except Exception as e:

        print(e)

        return ""


if __name__ == "__main__":
    listen()