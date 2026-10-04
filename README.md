# FRIDAY

A voice assistant inspired by FRIDAY from Iron Man, built from scratch in Python.

You speak, FRIDAY figures out what you want, does it, and answers out loud.

## How it works

FRIDAY runs as a simple four-step pipeline, one file per step:

| Step | File | What it does |
|------|------|--------------|
| 1. Listen | `listen.py` | Records audio from your microphone |
| 2. Transcribe | `friday.py` / `transcribe.py` | Turns speech into text with [OpenAI Whisper](https://github.com/openai/whisper) (runs locally, no API key) |
| 3. Understand | `understand.py` | Works out what you asked for (the "intent") |
| 4. Act | `act.py` | Does it and writes a reply |
| 5. Speak | `speak.py` | Reads the reply aloud with the Windows speech engine |

Everything runs on your own machine. No cloud services or API keys are needed.

## What it can do

- **Chat:** "hey", "how are you", "who are you", "thanks"
- **Jokes:** "tell me a joke"
- **Time and date:** "what time is it", "what's the date today"
- **Open websites:** "open youtube", "open github"
- **Search Google:** "search for python tutorials"
- **Play on YouTube:** "play lofi music"

## Requirements

- Windows with **WSL** (Ubuntu). FRIDAY runs in WSL but uses Windows to open
  the browser and to speak.
- Python 3.9+
- `ffmpeg` (needed by Whisper) and PortAudio (needed for the microphone)

## Setup

```bash
sudo apt install ffmpeg libportaudio2
git clone https://github.com/<your-username>/friday.git
cd friday
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

The first run downloads the Whisper `base` model (about 140 MB).

## Usage

Record a voice command (any audio format Whisper supports), then run:

```bash
python friday.py my_command.m4a
```

Example output:

```
========================================
  You said:  "Open YouTube."
  Friday:    Opening youtube.
========================================
```

### Helper scripts

- `scan_mics.py` lists your input devices and checks which one picks up sound
- `mictest.py` checks that the default mic works
- `checkrec.py` records a clip and checks its volume
- `listen.py` records a 6-second clip to `live.wav`. Set `MIC_DEVICE` to your
  mic's number from `scan_mics.py` first.

## Roadmap

- [ ] Listen live from the mic instead of a recorded file
- [ ] Wake word ("Hey Friday")
- [ ] Smarter understanding using a language model
- [ ] More commands (weather, reminders, opening apps)

## Disclaimer

This is a fan project. It is not affiliated with or endorsed by Marvel.

## License

[MIT](LICENSE)
