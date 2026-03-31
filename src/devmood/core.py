import random


def debug_encouragement(error_type: str) -> str:
    if not isinstance(error_type, str):
        raise TypeError("error_type must be a string")

    cleaned_error_type = error_type.strip()
    if not cleaned_error_type:
        raise ValueError("error_type cannot be empty")

    openings = [
        "Deep breath",
        "You've got this",
        "Debugger mode activated",
        "One bug at a time",
        "This is still progress",
    ]
    validations = [
        f"{cleaned_error_type} is annoying, not unbeatable",
        f"even a stubborn {cleaned_error_type} can be cornered",
        f"{cleaned_error_type} does not get the final word here",
        f"you are allowed to outlast this {cleaned_error_type}",
        f"this {cleaned_error_type} is just today's puzzle piece",
    ]
    next_steps = [
        "Start with the smallest reproducible case.",
        "Check the last thing that changed and test one assumption.",
        "Print the value you trust least and follow the trail.",
        "Reduce the scope until the bug has nowhere left to hide.",
        "Turn one mystery into one concrete observation.",
    ]
    closers = [
        "You do not need magic, just the next clue.",
        "Momentum comes back fast once the first clue lands.",
        "Tiny, boring debugging steps win these battles.",
        "A fix is usually hiding behind one verified fact.",
        "You are closer than this error wants you to believe.",
    ]

    message = (
        f"{random.choice(openings)}: {random.choice(validations)}. "
        f"{random.choice(next_steps)} {random.choice(closers)}"
    )
    if random.random() < 0.4:
        message += " Hydrate, rerun, and collect one more clue."

    return message


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
    msg = f"Need a hug, {name}?"
    n = len(msg)

    top    = "  _" + "_" * n + "_"
    middle = " / " + msg + " \\"
    bottom = " \\_" + "_" * n + "_/"
    tail   = "    \\"
    
    bunny1 = "      (\\_/)"
    bunny2 = "     (>'.'<)"
    bunny3 = '     (")_(")'

    return "\n".join([top, middle, bottom, tail, bunny1, bunny2, bunny3])
    
