#!/usr/bin/env python3
"""
OneBanc Assignment Professional Demonstration
"""

import time
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from edit_distance.core import (
    standard_levenshtein_distance,
    weighted_levenshtein_distance,
    optimized_levenshtein_distance
)
from edit_distance.spell_checker import spell_checker


def print_header(title: str) -> None:
    """Print formatted section header."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def demonstrate_all_tasks():
    """Demonstrate all assignment tasks."""
    
    print("🚀 OneBanc Levenshtein Distance Assignment")
    print("=" * 50)
    print("Author: Parth Kolhe")
    print("Date: 29/07/2025")
    print("=" * 50)
    
    # Task 1: Standard Levenshtein Distance
    print_header("TASK 1: Standard Levenshtein Distance")
    
    test_cases_1 = [
        ("kitten", "sitting"),
        ("flaw", "lawn"),
        ("algorithm", "logarithm")
    ]
    
    for s1, s2 in test_cases_1:
        start_time = time.time()
        distance = standard_levenshtein_distance(s1, s2)
        exec_time = time.time() - start_time
        
        print(f"✅ EditDistance('{s1}', '{s2}') = {distance} "
              f"(⏱️ {exec_time*1000:.2f}ms)")
    
    # Task 2: Weighted Edit Distance
    print_header("TASK 2: Weighted Edit Distance (Ci=1, Cd=2, Cs=3)")
    
    for s1, s2 in test_cases_1:
        start_time = time.time()
        distance = weighted_levenshtein_distance(s1, s2, 1, 2, 3)
        exec_time = time.time() - start_time
        
        print(f"✅ WeightedDistance('{s1}', '{s2}') = {distance} "
              f"(⏱️ {exec_time*1000:.2f}ms)")
    
    # Task 3: Spell Checker
    print_header("TASK 3: Spell Checker Implementation")
    
    dictionary = ["bet", "shat", "that", "cart", "brat", "data", "date", "cat", "bat"]
    test_word = "dat"
    
    print(f"Dictionary: {dictionary}")
    print(f"Input word: '{test_word}'")
    print(f"Costs: Ci=1, Cd=2, Cs=3\n")
    
    start_time = time.time()
    suggestions, min_dist = spell_checker(test_word, dictionary, 1, 2, 3)
    exec_time = time.time() - start_time
    
    print(f"✅ Suggestions: {suggestions}")
    print(f"✅ Minimum distance: {min_dist}")
    print(f"✅ Execution time: {exec_time*1000:.2f}ms")
    
    # Task 4: Optimization Analysis
    print_header("TASK 4: Space Optimization Analysis")
    
    print("Correctness Verification:")
    for s1, s2 in test_cases_1:
        standard_result = standard_levenshtein_distance(s1, s2)
        optimized_result = optimized_levenshtein_distance(s1, s2)
        
        status = "✅ CORRECT" if standard_result == optimized_result else "❌ ERROR"
        print(f"  {s1} → {s2}: Standard={standard_result}, Optimized={optimized_result} {status}")
    
    print_header("🎉 ASSIGNMENT COMPLETED SUCCESSFULLY!")


if __name__ == "__main__":
    demonstrate_all_tasks()
