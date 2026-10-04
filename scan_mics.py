import sounddevice as sd
import numpy as np

SR = 44100
for i, dev in enumerate(sd.query_devices()):
    if dev["max_input_channels"] < 1:
        continue
    print(f"\nDevice #{i}: {dev['name']}")
    print("  -> SPEAK NOW for 3 seconds...")
    try:
        audio = sd.rec(int(3 * SR), samplerate=SR, channels=1, device=i)
        sd.wait()
        level = float(np.abs(audio).max())
        mark = "✅ SOUND!" if level > 0.01 else "❌ silence"
        print(f"  level: {level:.4f}  {mark}")
    except Exception as e:
        print(f"  (couldn't use this device: {e})")
