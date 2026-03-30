import random


def debug_encouragement(error_type: str) -> str:
    raise NotImplementedError


def celebrate_small_win(task: str) -> str:
    raise NotImplementedError


def passive_aggressive_advice(topic: str) -> str:
    if not isinstance(topic, str):
        raise TypeError("topic must be a string")

    cleaned_topic = topic.strip()
    if not cleaned_topic:
        raise ValueError("topic cannot be empty")

    openings = [
        "Bold strategy",
        "Amazing choice",
        "Iconic engineering move",
        "Truly inspiring workflow",
        "Incredible commitment to suspense",
    ]
    jabs = [
        f"to treat '{cleaned_topic}' like a weekend-long side quest",
        f"to poke '{cleaned_topic}' with a stick and hope it refactors itself",
        f"to wait for '{cleaned_topic}' to solve itself through vibes",
        f"to escalate '{cleaned_topic}' into a full cinematic universe",
        f"to turn '{cleaned_topic}' into a philosophical discussion",
    ]
    action_steps = [
        "Write the smallest next step and run it immediately.",
        "Set a ten-minute timer and ship one tiny improvement.",
        "Pick one failing edge case and make it boringly pass.",
        "Delete one unnecessary thing before adding anything new.",
        "Explain the plan in one sentence, then execute sentence one.",
    ]
    closers = [
        "You are one focused commit away from momentum.",
        "Future-you would like fewer mysteries and more checkmarks.",
        "Progress beats drama every single time.",
        "Tiny wins compound faster than panic.",
        "Go earn a smug, well-deserved green test.",
    ]

    advice = (
        f"{random.choice(openings)} {random.choice(jabs)}. "
        f"{random.choice(action_steps)} {random.choice(closers)}"
    )
    if random.random() < 0.4:
        bonus_minutes = random.choice([5, 8, 10, 12, 15])
        advice += f" Bonus round: no context switching for {bonus_minutes} minutes."

    return advice


def ascii_hug(name: str) -> str:
    raise NotImplementedError
