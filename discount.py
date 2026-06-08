def calculate_discount(current_total, order_amount):
    if current_total >= 50000000:
        return 0.1

    if current_total + order_amount >= 50000000:
        return 0.1

    return 0