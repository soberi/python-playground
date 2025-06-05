# Write a code in Python to find out whether a given string 
# is a valid regex or not.

import re

def is_valid_regex(regex, string):
    try:
        re.search(regex, string)
        return True
    except re.error:
        print("Invalid regex input")
        return False