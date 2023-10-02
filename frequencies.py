"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    n = len(items)
    count = 0
    for i in range(n):
      for j in range(0, n - i - 1):
          if string(items[i]) == string(items[j]):
            count = count + 1
      frequencies[i] = count
    return frequencies
