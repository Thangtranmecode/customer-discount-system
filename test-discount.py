from discount import calculate_discount

def test_vip_customer():

    assert(calculate_discount(60000000) == 0.1)

def test_normal_customer():

    assert(calculate_discount(30000000) == 0.1)

def test_become_vip_after_order():
    assert calculate_discount(49000000, 2000000) == 0.1

def test_reach_exactly_50m():
    assert calculate_discount(48000000, 2000000) == 0.1

def test_still_not_vip():
    assert calculate_discount(30000000, 2000000) == 0

def test_already_vip():
    assert calculate_discount(60000000, 2000000) == 0.1