# Write a function in Python to check duplicate letters. 
# It must accept a string, i.e., a sentence. The function 
# should return True if the sentence has any word with 
# duplicate letters, else return False.

test_sentence = "I love bagels."
test_sentence_duplicates = "I love pretzels."

def check_word_duplicates(sentence):
    """Returns True if any word has duplicate letters, else False."""
    duplicates_found = 0
    word_list = sentence.split()

    for word in word_list:
        if len(word) != len(set(word)):
            duplicates_found += 1

    if duplicates_found >= 1:
        print("duplicates found")
        return True
    else:
        print("no duplicates found")
        return False

            


check_word_duplicates(test_sentence)
check_word_duplicates(test_sentence_duplicates)