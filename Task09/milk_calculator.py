from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")
CENT = Decimal("0.01")

def rate_per_litre(fat, snf):
    """Return the milk rate per litre."""
    fat = Decimal(str(fat)); snf = Decimal(str(snf))
    fat_steps = ((fat - FAT_REFERENCE) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - SNF_REFERENCE) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    return (BASE_RATE + fat_steps * FAT_STEP_VALUE
            + snf_steps * SNF_STEP_VALUE).quantize(CENT)

def payout(litres, fat, snf):
    """Validate an entry and return its payment."""
    litres = Decimal(str(litres)); fat = Decimal(str(fat)); snf = Decimal(str(snf))
    if litres <= 0:
        raise ValueError("Litres must be greater than zero")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf < 0:
        raise ValueError("SNF cannot be negative")
    return (litres * rate_per_litre(fat, snf)).quantize(CENT)

def main():
    try:
        farmer_id = input("Farmer ID: ").strip()
        litres = input("Litres: ").strip()
        fat = input("Fat %: ").strip()
        snf = input("SNF %: ").strip()
        shift = input("Shift (AM/PM): ").strip().upper()
        if not farmer_id:
            raise ValueError("Farmer ID cannot be empty")
        if shift not in {"AM", "PM"}:
            raise ValueError("Shift must be AM or PM")
        rate = rate_per_litre(fat, snf)
        amount = payout(litres, fat, snf)
        print(f"Farmer {farmer_id}: rate Rs {rate:.2f}, payment Rs {amount:.2f}")
    except Exception as error:
        print("Invalid entry:", error)

if __name__ == "__main__":
    main()
