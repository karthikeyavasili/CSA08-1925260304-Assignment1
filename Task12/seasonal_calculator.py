from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
STEP_SIZE = Decimal("0.1")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_THRESHOLD = Decimal("500")
BONUS_PER_LITRE = Decimal("0.50")

RATE_CARDS = {
    "standard": {
        "base": Decimal("30.00"),
        "fat_step": Decimal("0.40"),
        "snf_step": SNF_STEP_VALUE,
    },
    "apr_jun": {
        "base": Decimal("32.00"),
        "fat_step": Decimal("0.45"),
        "snf_step": SNF_STEP_VALUE,
    },
}

def steps(value, reference):
    """Return nearest number of 0.1 percentage-point steps."""
    return ((Decimal(str(value)) - reference) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf, season="standard"):
    """Calculate a rate using the selected season's rate card."""
    if season not in RATE_CARDS:
        raise ValueError("Unknown season")
    card = RATE_CARDS[season]
    rate = (card["base"] + steps(fat, FAT_REFERENCE) * card["fat_step"]
            + steps(snf, SNF_REFERENCE) * card["snf_step"])
    return rate.quantize(CENT, rounding=ROUND_HALF_UP)

def bonus(litres):
    """Return bonus amount; bonus applies only above 500 litres."""
    litres = Decimal(str(litres))
    return (litres * BONUS_PER_LITRE if litres > BONUS_THRESHOLD
            else Decimal("0.00")).quantize(CENT, rounding=ROUND_HALF_UP)

def payout(litres, fat, snf, season="standard", include_bonus=False):
    """Calculate base payment and optionally add the ten-day volume bonus."""
    litres = Decimal(str(litres))
    amount = (litres * rate_per_litre(fat, snf, season)).quantize(
        CENT, rounding=ROUND_HALF_UP)
    if include_bonus:
        amount += bonus(litres)
    return amount.quantize(CENT, rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    examples = [
        ("standard", "10", "3.50", "8.50"),
        ("apr_jun", "10", "3.50", "8.50"),
        ("apr_jun", "501", "3.55", "8.52"),
        ("apr_jun", "500", "3.50", "8.50"),
    ]
    for season, litres, fat, snf in examples:
        print(season, litres, fat, snf,
              "rate=", rate_per_litre(fat, snf, season),
              "payment+bonus=", payout(litres, fat, snf, season, True))
