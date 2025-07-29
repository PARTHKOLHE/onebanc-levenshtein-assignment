"""
Comprehensive Test Suite for OneBanc Assignment
"""

import pytest
import time
from edit_distance.core import (
    standard_levenshtein_distance,
    weighted_levenshtein_distance,
    optimized_levenshtein_distance,
)
from edit_distance.spell_checker import spell_checker


class TestStandardLevenshteinDistance:
    """Test standard Levenshtein distance implementation."""

    def test_assignment_examples(self):
        """Test with exact examples from assignment."""
        assert standard_levenshtein_distance("kitten", "sitting") == 3
        assert standard_levenshtein_distance("flaw", "lawn") == 2
        assert standard_levenshtein_distance("algorithm", "logarithm") == 3

    def test_edge_cases(self):
        """Test edge cases."""
        assert standard_levenshtein_distance("", "") == 0
        assert standard_levenshtein_distance("", "abc") == 3
        assert standard_levenshtein_distance("abc", "") == 3
        assert standard_levenshtein_distance("abc", "abc") == 0


class TestWeightedLevenshteinDistance:
    """Test weighted edit distance."""

    def test_weighted_examples(self):
        """Test weighted examples."""
        result1 = weighted_levenshtein_distance("kitten", "sitting", 1, 2, 3)
        result2 = weighted_levenshtein_distance("flaw", "lawn", 1, 2, 3)

        assert result1 > 3  # Should be higher than standard
        assert result2 > 2


class TestSpellChecker:
    """Test spell checker functionality."""

    def test_spell_check_example(self):
        """Test spell checker."""
        dictionary = ["bet", "shat", "that", "cart", "brat", "data", "date"]
        input_word = "dat"

        suggestions, min_dist = spell_checker(input_word, dictionary, 1, 2, 3)

        assert len(suggestions) > 0
        assert min_dist >= 0


class TestOptimization:
    """Test space optimization."""

    def test_optimization_correctness(self):
        """Verify optimized version matches standard results."""
        test_cases = [
            ("kitten", "sitting"),
            ("flaw", "lawn"),
            ("algorithm", "logarithm"),
        ]

        for s1, s2 in test_cases:
            standard = standard_levenshtein_distance(s1, s2)
            optimized = optimized_levenshtein_distance(s1, s2)
            assert standard == optimized


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
