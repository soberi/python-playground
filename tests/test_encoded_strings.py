import challenges.encoded_strings as es

sample_encoded_string = "John000Doe000123"
sample_decoded_dict = {
                        "first_name": "John", 
                        "last_name": "Doe", 
                        "id": "123" 
                    }

def test_decode_string():
    assert es.decode_string(sample_encoded_string) == sample_decoded_dict