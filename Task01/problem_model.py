from dataclasses import dataclass
from decimal import Decimal

BASE_RATE = Decimal("30.00")
FAT_REFERENCE = Decimal("3.5")
SNF_REFERENCE = Decimal("8.5")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
STEP_SIZE = Decimal("0.1")

@dataclass
class MilkEntry:
    farmer_id: str
    litres: Decimal
    fat: Decimal
    snf: Decimal
    shift: str

def validate_entry(entry: MilkEntry) -> None:
    if entry.litres <= 0:
        raise ValueError("Litres must be greater than zero")
    if not Decimal("2.0") <= entry.fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if entry.snf < 0:
        raise ValueError("SNF cannot be negative")
    if entry.shift.upper() not in {"AM", "PM"}:
        raise ValueError("Shift must be AM or PM")
