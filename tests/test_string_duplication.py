import challenges.string_duplication as sd

test_sentence = "I love bagels."
test_duplicates = "I love pretzels."
test_no_input = "" 

def test_no_duplicates():
    assert sd.check_word_duplicates(test_sentence) == False

def test_has_duplicates():
    assert sd.check_word_duplicates(test_duplicates) == True

def test_has_no_input():
    assert sd.check_word_duplicates(test_no_input) == False