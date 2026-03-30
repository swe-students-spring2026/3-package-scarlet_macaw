import pytest

from devmood import (
    ascii_hug,
    celebrate_small_win,
    debug_encouragement,
    passive_aggressive_advice,
)

# class TestDebugEncouragement:

# class TestCelebrateSmallWin:

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

# class TestAsciiHug:
