import sounddevice as sd
import numpy as np

SAMPLE_RATE = 44100
DURATION = 5
print("🎤 Speak LOUDLY for 5 seconds...")
audio = sd.rec(int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1)
sd.wait()
level = float(np.abs(audio).max())
print(f"Loudest sound captured: {level:.4f}")
if level < 0.01:
    print("❌ Basically silence — the mic isn't reaching WSL.")
else:
    print("✅ Sound detected! The mic works.")
