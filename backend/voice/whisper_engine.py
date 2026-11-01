import whisper

print("🔄 Loading Whisper model...")

model = whisper.load_model("base")

print("✅ Whisper Loaded Successfully!")


def transcribe(audio_file):

    result = model.transcribe(
        audio_file,
        task="transcribe",
        fp16=False,
        verbose=False
    )

    text = result["text"].strip()

    return text