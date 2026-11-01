import sounddevice as sd
from scipy.io.wavfile import write
import time

def record_audio(filename="voice.wav", duration=7):
    sample_rate = 16000

    print("🎤 Recording will start in 2 seconds...")
    time.sleep(2)

    print("🎙️ Speak now...")

    recording = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1,
        dtype="int16"
    )

    sd.wait()

    write(filename, sample_rate, recording)

    print("✅ Recording Saved:", filename)