"""
FRIDAY - step 05: SPEAK (female voice)
Uses Windows' built-in speech engine via PowerShell. Picks a female
voice (Zira) so Friday sounds like the Iron Man assistant.
"""

import subprocess


def speak(text):
    if not text:
        return
    safe = text.replace("'", "''")
    command = (
        "Add-Type -AssemblyName System.Speech; "
        "$s = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        # Try to pick a female voice; fall back to default if none found.
        "try { $s.SelectVoiceByHints('Female') } catch {}; "
        "$s.Rate = 0; "
        f"$s.Speak('{safe}')"
    )
    subprocess.run(["powershell.exe", "-Command", command])


if __name__ == "__main__":
    speak("Hello, I am Friday. Your assistant is now online.")
