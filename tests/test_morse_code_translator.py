import challenges.morse_code_translator as mct

# Test data
alpha_numeric_sentence = "I love bagels!"
morse_code_sentence = ".. .-..---...-. -....---...-.....-.-.--"

def test_translate():
    assert mct.print_morse_code(alpha_numeric_sentence) == morse_code_sentence