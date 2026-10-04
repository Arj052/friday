import sys
import whisper

def transcribe(audio_path):
    print("Loading Whisper model (first run downloads it, please wait)...")
    model = whisper.load_model("base")
    print(f"Listening to: {audio_path}")
    result = model.transcribe(audio_path)
    text = result["text"].strip()
    print("\n--- FRIDAY heard ---")
    print(text)
    print("--------------------\n")
    with open("transcript.txt", "w") as f:
        f.write(text)
    print("Saved to transcript.txt")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio-file>")
        sys.exit(1)
    transcribe(sys.argv[1])
