"""
FRIDAY - step 04: ACT (now with personality)
"""

import datetime
import random
import subprocess


def open_url(url):
    subprocess.run(["cmd.exe", "/c", "start", "", url])


def act(result):
    intent = result["intent"]
    detail = result["detail"]

    if intent == "greeting":
        return "Hey! I'm Friday. What can I do for you?"
    if intent == "how_are_you":
        return "I'm running perfectly, thank you. What can I do for you?"
    if intent == "who_are_you":
        return "I'm Friday, your personal assistant. Built from scratch, one step at a time."
    if intent == "thanks":
        return "Anytime. That's what I'm here for."
    if intent == "joke":
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs.",
            "There are 10 types of people. Those who understand binary, and those who don't.",
            "I'd tell you a UDP joke, but you might not get it.",
            "Why did the developer go broke? He used up all his cache.",
        ]
        return random.choice(jokes)

    if intent == "get_time":
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The time is {now}."
    if intent == "get_date":
        today = datetime.datetime.now().strftime("%A, %d %B %Y")
        return f"Today is {today}."

    if intent == "open_app":
        if not detail:
            return "Open what? I didn't catch the name."
        sites = {
            "youtube": "https://youtube.com",
            "google": "https://google.com",
            "github": "https://github.com",
            "gmail": "https://mail.google.com",
            "linkedin": "https://linkedin.com",
        }
        url = sites.get(detail, f"https://{detail}.com")
        open_url(url)
        return f"Opening {detail}."

    if intent == "search":
        if not detail:
            return "Search for what?"
        open_url(f"https://google.com/search?q={detail}")
        return f"Searching for {detail}."

    if intent == "play":
        query = detail or "music"
        open_url(f"https://youtube.com/results?search_query={query}")
        return f"Playing {query} on YouTube."

    if intent == "exit":
        return "Goodbye!"

    return "Sorry, I didn't understand that one yet."
