import subprocess, wave, numpy as np
from listen import record

record("live.wav")

# measure how loud the recording actually is
with wave.open("live.wav", "rb") as w:
    frames = w.readframes(w.getnframes())
    data = np.frombuffer(frames, dtype=np.int16).astype(np.float32)

if len(data) == 0:
    print("❌ The WAV file is EMPTY — recording captured nothing.")
else:
    level = np.abs(data).max() / 32768.0
    print(f"Recording length: {len(data)} samples")
    print(f"Loudest point: {level:.4f}")
    if level < 0.02:
        print("❌ Too quiet — Whisper can't hear this. Mic gain is low.")
    else:
        print("✅ Good volume — this should transcribe fine.")
