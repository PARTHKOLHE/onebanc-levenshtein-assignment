"""
Spell Checker Implementation using Edit Distance
"""

from typing import List, Tuple
from .core import weighted_levenshtein_distance


def spell_checker(
    input_word: str, dictionary: List[str], ci: int = 1, cd: int = 1, cs: int = 1
) -> Tuple[List[str], int]:
    """
    Find dictionary words with minimum edit distance to input word.

    Args:
        input_word: The potentially misspelled word
        dictionary: List of correctly spelled words
        ci: Cost of insertion operation
        cd: Cost of deletion operation
        cs: Cost of substitution operation

    Returns:
        Tuple of (list of suggested words, minimum distance found)
    """
    if not input_word:
        raise ValueError("Input word cannot be empty")

    if not dictionary:
        return [], float("inf")

    min_distance = float("inf")
    suggestions = []

    # Find minimum distance across all dictionary words
    for word in dictionary:
        distance = weighted_levenshtein_distance(input_word, word, ci, cd, cs)

        if distance < min_distance:
            min_distance = distance
            suggestions = [word]
        elif distance == min_distance:
            suggestions.append(word)

    return suggestions, min_distance
