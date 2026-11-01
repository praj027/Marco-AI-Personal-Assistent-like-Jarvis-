import json
import os

PROFILE_PATH = "memory/profile.json"


def load_profile():
    if not os.path.exists(PROFILE_PATH):
        return {}

    with open(PROFILE_PATH, "r") as f:
        return json.load(f)


def save_profile(profile):
    with open(PROFILE_PATH, "w") as f:
        json.dump(profile, f, indent=4)


def remember(key, value):
    profile = load_profile()
    profile[key] = value
    save_profile(profile)


def recall(key):
    profile = load_profile()
    return profile.get(key)