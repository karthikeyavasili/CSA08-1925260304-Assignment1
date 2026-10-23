"""Rate card and calculation functions for the village milk co-operative."""
from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def _steps(value, reference):
    """Return the nearest whole number of 0.1 percentage-point steps."""
    return ((Decimal(str(value)) - reference) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Return the rate per litre rounded to two decimal places."""
    rate = (BASE_RATE + _steps(fat, FAT_REFERENCE) * FAT_STEP_VALUE
            + _steps(snf, SNF_REFERENCE) * SNF_STEP_VALUE)
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf):
    """Return the payment rounded to two decimal places."""
    return (Decimal(str(litres)) * rate_per_litre(fat, snf)).quantize(
        CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    for litres, fat, snf in [("10", "3.5", "8.5"),
                             ("8.5", "4.2", "8.7"),
                             ("12", "3.1", "8.3")]:
        rate = rate_per_litre(fat, snf)
        pay = payout(litres, fat, snf)
        print(f"{litres:>5} L  fat {fat}  snf {snf}  "
              f"rate {rate:>6.2f}  pay {pay:>8.2f}")
