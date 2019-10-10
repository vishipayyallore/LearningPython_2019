def calculate_down_payment(asset_price: float, credit_report: int) -> float:
    down_payment = 0.0

    if(credit_report == 0):
        down_payment = 0.2 * asset_price
    else:
        down_payment = 0.1 * asset_price

    return down_payment


def main():
    asset_price = float(input('Enter Asset Price: '))
    credit_report = int(input('Have good credit report {0=False / 1=True} :'))

    output = calculate_down_payment(asset_price, credit_report)
    print(output)

main()

