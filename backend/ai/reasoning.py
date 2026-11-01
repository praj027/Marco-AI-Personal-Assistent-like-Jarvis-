def enrich_command(command: str):

    text = command.lower().strip()

    # -------------------------
    # Mood Detection
    # -------------------------

    if any(x in text for x in [
    "mood kharab",
    "mera mood kharab",
    "mood off",
    "sad",
    "dukhi",
    "feeling low",
    "depressed",
    "मूड खराब",
    "मूड ऑफ",
    "दुखी",
    "उदास",
    "कराब",
    "खराब"
]):
      return "play sad songs on youtube"

    if any(x in text for x in [
        "romantic",
        "love song",
        "girlfriend",
        "boyfriend",
        "crush"
    ]):
        return "play romantic songs on youtube"

    if any(x in text for x in [
        "gym",
        "workout",
        "exercise"
    ]):
        return "play workout songs on youtube"

    if any(x in text for x in [
        "study",
        "coding",
        "programming"
    ]):
        return "play lofi coding music on youtube"

    if any(x in text for x in [
        "bhajan",
        "hanuman",
        "shiv"
    ]):
        return "play devotional songs on youtube"

    if any(x in text for x in [
        "news"
    ]):
        return "search latest news"

    if any(x in text for x in [
        "weather",
        "temperature"
    ]):
        return "search today's weather"

    return command