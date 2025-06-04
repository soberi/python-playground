# Write a function in Python to check duplicate letters. 
# It must accept a string, i.e., a sentence. The function 
# should return True if the sentence has any word with 
# duplicate letters, else return False.

def check_word_duplicates(sentence):
    """Returns True if any word has duplicate letters, else False."""
    duplicates_found = 0
    word_list = sentence.split()

    if sentence == "":
        print("You have not added anything.")

    for word in word_list:
        if len(word) != len(set(word)):
            duplicates_found += 1

    if duplicates_found >= 1:
        return True
    else:
        return False
