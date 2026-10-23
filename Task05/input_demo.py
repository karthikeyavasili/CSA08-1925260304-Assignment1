from decimal import Decimal, InvalidOperation

def read_decimal(prompt):
    text = input(prompt).strip()
    try:
        return Decimal(text)
    except InvalidOperation:
        raise ValueError(f"Invalid number: {text!r}")

def main():
    try:
        litres = read_decimal("Enter litres: ")
        fat = read_decimal("Enter fat percentage: ")
        snf = read_decimal("Enter SNF percentage: ")
        amount = litres * Decimal("30.00")
        print(f"{'Litres':<12}{'Fat':<10}{'SNF':<10}{'Amount (Rs)':>14}")
        print(f"{litres:<12}{fat:<10}{snf:<10}{amount:>14.2f}")
    except ValueError as error:
        print("Input error:", error)

if __name__ == "__main__":
    main()
