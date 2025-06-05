# Write a function in Python to convert a decimal to a hex. 
# It must accept a string of ASCII characters as input. 
# The function should return the value of each character 
# as a hexadecimal string. You have to separate each byte 
# by a space and return all alpha hexadecimal characters as 
# lowercase.

def convert_to_hex(decimal):
    hexidecimal = hex(int(decimal))

    separated_hex = " ".join([hexidecimal[i:i+8] for i in range(0, len(hexidecimal), 8)])

    return separated_hex
