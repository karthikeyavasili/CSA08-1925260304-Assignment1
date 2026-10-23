from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def money(value):
    """Round a monetary value to the nearest paisa."""
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf):
    """Calculate the price per litre from fat and SNF percentages."""
    fat_steps = ((Decimal(str(fat)) - FAT_REFERENCE) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((Decimal(str(snf)) - SNF_REFERENCE) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    return money(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE)

def payout(litres, fat, snf):
    """Return the rounded payment for one milk entry."""
    return money(Decimal(str(litres)) * rate_per_litre(fat, snf))

def ten_day_total(payments):
    """Return the total of a sequence of payment amounts."""
    return money(sum((Decimal(str(p)) for p in payments), Decimal("0.00")))

if __name__ == "__main__":
    print("Rate:", rate_per_litre("4.2", "8.7"))
    print("Payout:", payout("8.5", "4.2", "8.7"))
    print("Ten-day total:", ten_day_total(["300.00", "283.90", "333.60"]))
