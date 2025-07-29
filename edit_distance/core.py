"""
OneBanc Levenshtein Distance Assignment - Core Implementation
============================================================

Professional implementation of edit distance algorithms with comprehensive
documentation, type hints, and optimization techniques.

Author: Parth Kolhe
Date: 29/07/2025
Assignment: OneBanc Technical Assessment
"""

from typing import List, Tuple, Optional
import time


def standard_levenshtein_distance(s1: str, s2: str) -> int:
    """
    Calculate standard Levenshtein distance using dynamic programming.
    
    Args:
        s1: Source string
        s2: Target string
    
    Returns:
        Minimum edit distance between s1 and s2
    
    Examples:
        >>> standard_levenshtein_distance("kitten", "sitting")
        3
        >>> standard_levenshtein_distance("flaw", "lawn") 
        2
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings")
    
    m, n = len(s1), len(s2)
    
    # Handle edge cases
    if m == 0:
        return n
    if n == 0:
        return m
    
    # Initialize DP matrix
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    # Fill the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(
                    dp[i-1][j-1],  # Substitution
                    dp[i-1][j],    # Deletion
                    dp[i][j-1]     # Insertion
                )
    
    return dp[m][n]


def weighted_levenshtein_distance(s1: str, s2: str, 
                                 ci: int = 1, cd: int = 1, cs: int = 1) -> int:
    """
    Calculate weighted Levenshtein distance with custom operation costs.
    
    Args:
        s1: Source string
        s2: Target string  
        ci: Cost of insertion operation
        cd: Cost of deletion operation
        cs: Cost of substitution operation
    
    Returns:
        Minimum weighted edit distance
    """
    if not all(isinstance(x, int) and x > 0 for x in [ci, cd, cs]):
        raise ValueError("All costs must be positive integers")
    
    m, n = len(s1), len(s2)
    
    if m == 0:
        return n * ci
    if n == 0:
        return m * cd
    
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    
    # Initialize with weighted costs
    for i in range(m + 1):
        dp[i][0] = i * cd
    for j in range(n + 1):
        dp[0][j] = j * ci
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j-1] + cs,  # Substitution
                    dp[i-1][j] + cd,    # Deletion
                    dp[i][j-1] + ci     # Insertion
                )
    
    return dp[m][n]


def optimized_levenshtein_distance(s1: str, s2: str) -> int:
    """
    Space-optimized Levenshtein distance using rolling arrays.
    
    Time Complexity: O(len(s1) * len(s2))
    Space Complexity: O(min(len(s1), len(s2)))
    """
    # Ensure s1 is the shorter string
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    
    m, n = len(s1), len(s2)
    
    if m == 0:
        return n
    
    # Use two 1D arrays instead of 2D matrix
    prev_row = list(range(n + 1))
    curr_row = [0] * (n + 1)
    
    for i in range(1, m + 1):
        curr_row[0] = i
        
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                curr_row[j] = prev_row[j-1]
            else:
                curr_row[j] = 1 + min(
                    prev_row[j-1],  # Substitution
                    prev_row[j],    # Deletion
                    curr_row[j-1]   # Insertion
                )
        
        # Swap rows for next iteration
        prev_row, curr_row = curr_row, prev_row
    
    return prev_row[n]
