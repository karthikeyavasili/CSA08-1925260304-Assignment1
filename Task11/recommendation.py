from decimal import Decimal
from milk_functions import payout, ten_day_total

entries = [
    ("F001", "10", "3.5", "8.5"),
    ("F002", "8.5", "4.2", "8.7"),
    ("F003", "12", "3.1", "8.3"),
]
payments = []
for farmer_id, litres, fat, snf in entries:
    amount = payout(litres, fat, snf)
    payments.append(amount)
    print(f"{farmer_id}: Rs {amount:.2f}")
print(f"Ten-day total: Rs {ten_day_total(payments):.2f}")
