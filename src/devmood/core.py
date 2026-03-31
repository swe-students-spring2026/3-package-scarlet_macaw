import random


def debug_encouragement(error_type: str) -> str:
    raise NotImplementedError


def celebrate_small_win(task: str) -> str:
    """Return an enthusiastic celebration message for a completed coding task.

    Args:
        task: A short description of the task that was completed.

    Returns:
        A celebratory string that includes the task name.

    Raises:
        TypeError: If task is not a string.
        ValueError: If task is empty or whitespace only.
    """
    # Ensure the caller passed a string, not an int or None
    if not isinstance(task, str):
        raise TypeError("task must be a string")

    # Strip leading/trailing whitespace so blank-padded strings are rejected
    cleaned_task = task.strip()
    if not cleaned_task:
        raise ValueError("task cannot be empty")

    # Short punchy openers to kick off the celebration
    openers = [
        "Nailed it!",
        "Victory!",
        "Shipped!",
        "Done and done!",
        "Champion move!",
    ]

    # Middle section that calls out the specific task by name
    middles = [
        f"You just '{cleaned_task}' like a pro.",
        f"'{cleaned_task}' is officially off the list.",
        f"Turns out '{cleaned_task}' was totally within your power.",
        f"The world now has one more developer who can '{cleaned_task}'.",
        f"'{cleaned_task}' has been conquered. Bow down.",
    ]

    # Motivational closers to keep the momentum going
    closers = [
        "Keep the momentum going!",
        "One small step for you, one giant leap for your codebase.",
        "Stack those wins.",
        "Future you will be grateful.",
        "Now go grab a coffee — you earned it.",
    ]

    # Randomly combine one opener, middle, and closer for variety
    return f"{random.choice(openers)} {random.choice(middles)} {random.choice(closers)}"

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
