# Write a function in Python to parse a string such that 
# it accepts a parameter- an encoded string. This encoded 
# string will contain a first name, last name, and an id. 
# You can separate the values in the string by any number 
# of zeros. The id will not contain any zeros. The function 
# should return a Python dictionary with the first name, last 
# name, and id values. For example, if the input would be 
# “John000Doe000123”. Then the function should return: 
# { “first_name”: “John”, “last_name”: “Doe”, “id”: “123” }

def decode_string(encoded_string):
    
    seperated_string = encoded_string.split("0")
    string_list = list(filter(None, seperated_string))
    print(string_list)

    info_dict = {
                    "first_name": string_list[0],
                    "last_name": string_list[1],
                    "id": string_list[2]
                }
    
    return info_dict