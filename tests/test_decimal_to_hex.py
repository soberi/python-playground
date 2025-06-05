import challenges.decimal_to_hex as dh

small_dec = "264"
small_hex = "0x108"
medium_dec = "1234567890"
medium_hex = "0x499602 d2"
big_dec = "1234567890098765432112345678900987654321"
big_hex = "0x3a0c92 0757113b d850b853 db55a777 0b1"

def test_hex_contains_only_integers():
    assert dh.convert_to_hex(small_dec) == small_hex

def test_hex_is_alphanumeric():
    assert dh.convert_to_hex(medium_dec) == medium_hex

def test_hex_requires_spaces():
    assert dh.convert_to_hex(big_dec) == big_hex