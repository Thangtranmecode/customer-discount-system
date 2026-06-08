from discount import calculate_discount
def test_vip_customer():
    assert calculate_discount(6000000) == 0.1
def test_normal_customer():
    assert calculate_discount(3000000) == 0.0