

from datetime import datetime

# Define sample exchange rates relative to USD (1 USD = X currency)
# Base rates: USD=1.0, EUR=0.92, UAH=41.5
EXCHANGE_RATES = {"USD": 1.0, "EUR": 0.92, "UAH": 41.5}


def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
  
    if from_curr not in EXCHANGE_RATES or to_curr not in EXCHANGE_RATES:
        print(f"Error: Unsupported currency! Supported: {list(EXCHANGE_RATES.keys())}")
        return 0.0

    # Convert source currency to USD base, then to target currency
    amount_in_usd = amount / EXCHANGE_RATES[from_curr]
    converted_amount = amount_in_usd * EXCHANGE_RATES[to_curr]

    return converted_amount


def log_transaction(
    amount: float, from_curr: str, result: float, to_curr: str
) -> None:
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = (
        f"[{timestamp}] Exchanged: {amount} {from_curr} -> "
        f"{result:.2f} {to_curr}\n"
    )

    try:
        with open("data/log.txt", "a", encoding="utf-8") as f:
            f.write(log_message)
    except FileNotFoundError:
        print("Error: Log directory or file not found!")