import pytest

from devmood import (
    ascii_hug,
    celebrate_small_win,
    debug_encouragement,
    passive_aggressive_advice,
)

# class TestDebugEncouragement:

class TestCelebrateSmallWin:
    def test_returns_string(self):
        result = celebrate_small_win("wrote my first passing test")
        assert isinstance(result, str)

    def test_contains_task_name(self):
        result = celebrate_small_win("fixed a null pointer bug")
        assert "fixed a null pointer bug" in result

    def test_result_is_nonempty(self):
        result = celebrate_small_win("refactored the auth module")
        assert len(result) > 0

    def test_strips_surrounding_whitespace(self):
        result = celebrate_small_win("  wrote a docstring  ")
        assert "wrote a docstring" in result
        assert "  wrote a docstring  " not in result

    def test_raises_on_empty_task(self):
        with pytest.raises(ValueError):
            celebrate_small_win("   ")

    def test_raises_on_non_string_task(self):
        with pytest.raises(TypeError):
            celebrate_small_win(42)


class TestPassiveAggressiveAdvice:
    def test_returns_string_with_topic(self):
        result = passive_aggressive_advice("refactoring")

        assert isinstance(result, str)
        assert "refactoring" in result
        assert len(result) > 40

    def test_strips_surrounding_whitespace(self):
        result = passive_aggressive_advice("   unit tests   ")

        assert "unit tests" in result
        assert "   unit tests   " not in result

    def test_raises_on_empty_topic(self):
        with pytest.raises(ValueError):
            passive_aggressive_advice("   ")

    def test_raises_on_non_string_topic(self):
        with pytest.raises(TypeError):
            passive_aggressive_advice(None)

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