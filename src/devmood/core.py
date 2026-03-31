def debug_encouragement(error_type: str) -> str:
    raise NotImplementedError


def celebrate_small_win(task: str) -> str:
    raise NotImplementedError


def passive_aggressive_advice() -> str:
    raise NotImplementedError


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
    
