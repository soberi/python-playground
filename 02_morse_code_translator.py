# Write a code in Python to create a Morse code translator. 
# You can take a string with alphanumeric characters in lower 
# or upper case. The string can also have any special characters 
# as a part of the Morse code. Special characters can include 
# commas, colons, apostrophes, exclamation marks, periods, and 
# question marks. The code should return the Morse code that 
# is equivalent to the string.

# Morse code dictionary
morse_code_dict = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.-", "Z": "--..", "!": "-.-.--", "?": "..--"
}

# Test data
alpha_numeric_sentence = "I love bagels!"
morse_code_sentence = ".. .-..---...-. -....---...-.....-.-.--"

def print_morse_code(sentence):
    """Translates sentence into morse code."""
    morse_translation = ""
    
    for letter in sentence:
        if letter == " ":
            morse_translation += letter
        else: 
            char = morse_code_dict.get(letter.upper())
            morse_translation += char
        
    print(morse_translation)

    # for letter in sentence:
    #     if letter.upper() in key
    #     print(letter.upper())

print_morse_code(alpha_numeric_sentence)