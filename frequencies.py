"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    duplicates = {}
    frequencies = {}
    # Your code goes here
    n = len(items)
    count = 0
    for i in range(n):
      for j in range(n):
          if str(items[i]) == str(items[j]):
            count = count + 1
      duplicates[str(items[i])] = count
      count = 0
      
    return duplicates
