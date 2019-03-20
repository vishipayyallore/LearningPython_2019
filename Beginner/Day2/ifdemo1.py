
def show_banner(value: str, times: int):
    print(value * times)


def validate_loan_eligibility(has_income: bool, credit_report: bool, payment_default: bool) -> str:
    if(has_income and (credit_report and (not payment_default))):
        return "Eligible for loan"
    else:
        return "Not Eligible for loan"


def get_applicants_details(switch: int):
    if(switch == 1):
        return True, True, True
    elif(switch == 2):
        return True, False, True
    elif(switch == 3):
        return True, True, False


def main():

    # Assume we got the parameters from other method
    income, credit, payment_default = get_applicants_details(3)
    results = validate_loan_eligibility(income, credit, payment_default)
    print(results)

    income, credit, payment_default = get_applicants_details(1)
    results = validate_loan_eligibility(income, credit, payment_default)
    print(results)

    income, credit, payment_default = get_applicants_details(3)
    results = validate_loan_eligibility(income, credit, payment_default)
    print(results)

    income, credit, payment_default = get_applicants_details(2)
    results = validate_loan_eligibility(income, credit, payment_default)
    print(results)


main()
