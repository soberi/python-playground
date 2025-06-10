# Print all possible size k replacement combinations of 
# the given string S in lexicographically (alphabetical) 
# sorted order.

from itertools import combinations

def print_combos(k, string):
    for i in combinations(string, k):
        print(i)