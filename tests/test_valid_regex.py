import challenges.valid_regex as vr


original_text = "The rain in Spain"
valid_regex = "^The.*Spain$"
invalid_regex = "[^The.*Spain$"

def test_regex_is_valid():
    assert vr.is_valid_regex(valid_regex, original_text) == True

def test_regex_is_invalid():
    assert vr.is_valid_regex(invalid_regex, original_text) == False