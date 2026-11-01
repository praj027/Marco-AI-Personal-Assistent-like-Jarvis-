import re

EMOTIONS = {
    "sad": [
        "sad",
        "mood bad",
        "bad mood",
        "depressed",
        "upset",
        "cry",
        "lonely",
        "hurt",
        "feeling low",
        "my mood is bad",
        "i am sad",
    ],

    "happy": [
        "happy",
        "awesome",
        "great",
        "excited",
        "good news",
        "i am happy",
    ],

    "angry": [
        "angry",
        "mad",
        "annoyed",
        "frustrated",
        "irritated",
    ],

    "tired": [
        "tired",
        "sleepy",
        "exhausted",
        "no energy",
    ],

    "romantic": [
        "love",
        "romantic",
        "miss her",
        "miss him",
    ]
}


RESPONSES = {

    "sad": [
        "I'm sorry you're feeling low, Sir.",
        "I'm here for you, Sir.",
        "I hope I can make your day a little better."
    ],

    "happy": [
        "That's wonderful, Sir!",
        "I'm really happy to hear that.",
        "Congratulations, Sir!"
    ],

    "angry": [
        "Please stay calm, Sir.",
        "Take a deep breath.",
        "We'll solve it together."
    ],

    "tired": [
        "You sound tired, Sir.",
        "Please don't forget to take some rest."
    ],

    "romantic": [
        "Love is a beautiful feeling, Sir.",
        "Let's make the moment special."
    ],

    "normal": []
}


def detect_emotion(text):

    text = text.lower()
    text = re.sub(r"[^\w\s]", "", text)

    for emotion, words in EMOTIONS.items():
        for word in words:
            if word in text:
                return emotion

    return "normal"


def emotion_reply(emotion):

    if emotion in RESPONSES and RESPONSES[emotion]:
        return RESPONSES[emotion][0]

    return ""