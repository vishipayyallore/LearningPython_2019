
def calculate_down_payment(asset_price: float, credit_report: bool) -> float:
    down_payment = 0.0

    if(credit_report):
        down_payment = 0.1 * asset_price
    else:
        down_payment = 0.2 * asset_price

    return down_payment


def main():
    asset_price = 1000000
    credit_report = True

    payment = calculate_down_payment(asset_price, credit_report)
    print(f'Your Down Payment: {payment}')

    asset_price = 2000000
    credit_report = False

    payment = calculate_down_payment(asset_price, credit_report)
    print(f'Your Down Payment: {payment}')

# invoking the main method
main()

