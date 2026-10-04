"""
FRIDAY - step 03: UNDERSTAND (now with personality)
"""


def understand(text):
    t = text.lower().strip()
    for ch in "?.!,'":
        t = t.replace(ch, "")
    words = t.split()

    def has(*targets):
        return any(target in words for target in targets)

    # chit-chat / personality
    if "how are you" in t:
        return {"intent": "how_are_you", "detail": None}
    if "who are you" in t or "your name" in t:
        return {"intent": "who_are_you", "detail": None}
    if has("thanks", "thank"):
        return {"intent": "thanks", "detail": None}
    if has("joke") or "make me laugh" in t:
        return {"intent": "joke", "detail": None}

    # greetings / exit
    if has("hello", "hi", "hey") or "whats up" in t:
        return {"intent": "greeting", "detail": None}
    if has("exit", "quit", "stop", "bye", "goodbye"):
        return {"intent": "exit", "detail": None}

    # info
    if has("time"):
        return {"intent": "get_time", "detail": None}
    if has("date", "today") or has("day"):
        return {"intent": "get_date", "detail": None}

    # actions
    if has("open", "launch", "start"):
        detail = None
        for opener in ["open", "launch", "start"]:
            if opener in words:
                i = words.index(opener)
                if i + 1 < len(words):
                    detail = words[i + 1]
                break
        return {"intent": "open_app", "detail": detail}

    if has("search", "google") or "look up" in t:
        detail = None
        for trigger in ["search for", "search", "google", "look up"]:
            if trigger in t:
                detail = t.split(trigger, 1)[1].strip()
                break
        return {"intent": "search", "detail": detail or None}

    if has("play"):
        i = words.index("play")
        detail = " ".join(words[i + 1:]) or None
        return {"intent": "play", "detail": detail}

    return {"intent": "unknown", "detail": None}
