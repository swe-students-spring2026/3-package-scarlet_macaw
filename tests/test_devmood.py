import pytest

from devmood import (
    ascii_hug,
    celebrate_small_win,
    debug_encouragement,
    passive_aggressive_advice,
)

# class TestDebugEncouragement:

# class TestCelebrateSmallWin:

# class TestPassiveAggressiveAdvice:

class TestAsciiHug:
    """
    Verifies the exact output for a name.
    """
    def test_ascii_hug_standard_name(self):
        expected = (
            "  ____________________\n"
            " / Need a hug, Alice? \\\n"
            " \\____________________/\n"
            "    \\\n"
            "      (\\_/)\n"
            "     (>'.'<)\n"
            '     (")_(")'
        )
        assert ascii_hug("Alice") == expected

    """
    Verifies the behavior when an empty string is provided.
    """
    def test_ascii_hug_empty_string(self):
        expected = (
            "  _______________\n"
            " / Need a hug, ? \\\n"
            " \\_______________/\n"
            "    \\\n"
            "      (\\_/)\n"
            "     (>'.'<)\n"
            '     (")_(")'
        )
        assert ascii_hug("") == expected

    """
    Tests handling of non-standard ASCII characters and emojis.
    """
    def test_ascii_hug_with_unicode_emoji(self):
        name = "ʕ•ᴥ•ʔ 👾"
        result = ascii_hug(name)
        
        expected_msg = f"Need a hug, {name}?"
        expected_border = "_" * len(expected_msg)
        
        assert f"  _{expected_border}_" in result
        assert expected_msg in result