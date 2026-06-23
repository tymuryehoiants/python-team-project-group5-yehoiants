


def get_user_input() -> tuple[float, str, str]:
    
    print("=== Console Currency Converter ===")
    try:
        amount = float(input("Enter the amount to exchange: "))
        if amount < 0:
            print("Error: Amount cannot be negative!")
            return 0.0, "", ""
    except ValueError:
        print("Error: Invalid number entered!")
        return 0.0, "", ""

    from_currency = (
        input("Enter source currency (USD, EUR, RUB): ").strip().upper()
    )
    to_currency = (
        input("Enter target currency (USD, EUR, RUB): ").strip().upper()
    )

    return amount, from_currency, to_currency


def print_result(amount: float, from_curr: str, result: float, to_curr: str):
    """Prints the conversion result to the console.

    :param amount: Original amount
    :param from_curr: Source currency
    :param result: Converted amount
    :param to_curr: Target currency
    """
    if result > 0:
        print(f"\n[Success] {amount} {from_curr} = {result:.2f} {to_curr}\n")
    else:
        print("\n[Error] Conversion could not be completed.\n")