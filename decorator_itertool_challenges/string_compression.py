# Compress the given string S. If the string contains 
# a character ‘c,’ that occurs X times consecutively. 
# Replace ‘c’ with (X, c) in the string.

from itertools import groupby

def compress_c(string):
    
    compressed_string = ""
    for i, j in groupby(string):
        if i == "c":
            length = str(len(list(j)))
            compressed_string += length + i
        else:
            compressed_string += i * len(list(j))
    
    return compressed_string