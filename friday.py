"""
FRIDAY - record mode (single run, clean output for filming).
Give it one audio file. It runs the full pipeline once, then stops.

Run:  python friday.py your_clip.m4a
"""

import sys
import whisper
from understand import understand
from act import act
from speak import speak


def listen_from_file(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result["text"].strip()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python friday.py <audio-file>")
        sys.exit(1)

    print("\n========================================")
    text = listen_from_file(sys.argv[1])
    print(f'  You said:  "{text}"')

    result = understand(text)
    reply = act(result)
    print(f'  Friday:    {reply}')
    print("========================================\n")

    speak(reply)
