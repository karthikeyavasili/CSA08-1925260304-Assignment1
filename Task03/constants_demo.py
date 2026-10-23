BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
FAT_REFERENCE = 3.5
SNF_REFERENCE = 8.5
STEP_SIZE = 0.1

RATE_CARD = {
    "base": BASE_RATE,
    "fat": FAT_STEP_VALUE,
    "snf": SNF_STEP_VALUE,
}

def show_rate_card():
    print("Named constants:")
    print(BASE_RATE, FAT_STEP_VALUE, SNF_STEP_VALUE)
    print("Dictionary rate card:", RATE_CARD)

if __name__ == "__main__":
    show_rate_card()
    value = 10
    print("Initially:", value, type(value).__name__)
    value = "ten"
    print("Later:", value, type(value).__name__)
    a, b = 1, 2
    a, b = b, a
    print("After swap:", a, b)
