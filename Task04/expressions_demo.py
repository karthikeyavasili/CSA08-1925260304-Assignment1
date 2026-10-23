from decimal import Decimal, ROUND_HALF_UP
import math

BASE_RATE = Decimal("30.00")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")

def steps(value, reference):
    return ((value - reference) / STEP_SIZE).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP
    )

def rate_per_litre(fat, snf):
    fat_steps = steps(Decimal(str(fat)), FAT_REFERENCE)
    snf_steps = steps(Decimal(str(snf)), SNF_REFERENCE)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return rate.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

if __name__ == "__main__":
    print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
    print("0.1 + 0.2 =", 0.1 + 0.2)
    print("round(-1.5) =", round(-1.5))
    print("int(-1.5) =", int(-1.5))
    print("floor(-1.5) =", math.floor(-1.5))
    for fat in ("4.2", "3.1"):
        print("fat =", fat,
              "round steps =", steps(Decimal(fat), FAT_REFERENCE),
              "rate with standard SNF =", rate_per_litre(fat, "8.5"))
