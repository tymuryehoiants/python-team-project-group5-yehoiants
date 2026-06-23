import os
import sys


sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter import convert_currency, log_transaction
from io_utils import get_user_input, print_result
42
def main():
    amount, from_curr, to_curr = get_user_input()
    if amount == 0.0 or from_curr == "" or to_curr == "":
        return
    result = convert_currency(amount, from_curr, to_curr)
    print_result(amount, from_curr, result, to_curr)
    if result > 0:
        log_transaction(amount, from_curr, result, to_curr)

if __name__ == "__main__":
    main()