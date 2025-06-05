import challenges.get_ip_address as gia

test_ip_address = '8.8.8.8'
test_domain_name = "dns.google"

def test_get_domain_name():
    assert gia.get_domain_name(test_ip_address) == test_domain_name