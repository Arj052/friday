"""
FRIDAY - step 01: LISTEN (locked to RDPSource, the real mic)
"""

import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write

SAMPLE_RATE = 44100
DURATION = 6
MIC_DEVICE = 4          # RDPSource — your real mic from earlier


def record(filename="live.wav", seconds=DURATION):
    print(f"\n🎤 Recording {seconds}s from device #{MIC_DEVICE}... speak now.")
    audio = sd.rec(int(seconds * SAMPLE_RATE),
                   samplerate=SAMPLE_RATE, channels=1,
                   device=MIC_DEVICE, dtype="float32")
    sd.wait()

    level = float(np.abs(audio).max())
    print(f"   captured level: {level:.4f}", "✅" if level > 0.02 else "⚠️ quiet")

    # Save as 16-bit WAV for Whisper
    write(filename, SAMPLE_RATE, (audio * 32767).astype(np.int16))
    print("✓ Saved.")
    return filename


if __name__ == "__main__":
    record()
