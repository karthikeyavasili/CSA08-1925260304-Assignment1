from milkrate import rate_per_litre, payout

if __name__ == "__main__":
    for litres, fat, snf in [("10", "3.5", "8.5"),
                             ("8.5", "4.2", "8.7"),
                             ("12", "3.1", "8.3")]:
        print(rate_per_litre(fat, snf), payout(litres, fat, snf))
