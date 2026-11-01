from record import record_audio
from whisper_engine import transcribe

record_audio()

text = transcribe("voice.wav")

print("\n📝 You said:")
print(text)