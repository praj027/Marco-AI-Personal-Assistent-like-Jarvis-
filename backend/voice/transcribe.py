import whisper
from ai.brain import process_command

print("Loading Whisper model...")

model = whisper.load_model("base")

print("Transcribing...")

result = model.transcribe("voice.wav")

text = result["text"]

print("\nYou said:", text)

process_command(text)