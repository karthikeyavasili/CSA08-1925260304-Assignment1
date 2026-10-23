from decimal import Decimal
from time import perf_counter

PAYMENT = "33.40"
SIZES = (300, 6000, 150000)

def measure_float(n):
    start = perf_counter()
    total = 0.0
    for _ in range(n):
        total += float(PAYMENT)
    return total, perf_counter() - start

def measure_decimal(n):
    start = perf_counter()
    amount = Decimal(PAYMENT)
    total = Decimal("0.00")
    for _ in range(n):
        total += amount
    return total, perf_counter() - start

if __name__ == "__main__":
    for n in SIZES:
        f_total, f_seconds = measure_float(n)
        d_total, d_seconds = measure_decimal(n)
        print(f"n={n:,}")
        print(f"  float  total={f_total:.12f}, time={f_seconds:.6f}s")
        print(f"  Decimal total={d_total:.2f}, time={d_seconds:.6f}s")
        print(f"  difference (float - Decimal)={Decimal(str(f_total)) - d_total}")
