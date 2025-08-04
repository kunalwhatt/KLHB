# addition_rule_non_mutually_exclusive.py
# Non-mutually exclusive events: Drawing a heart or king

def addition_rule_non_mutually_exclusive():
    P_heart = 13/52
    P_king = 4/52
    P_heart_and_king = 1/52
    P_heart_or_king = P_heart + P_king - P_heart_and_king

    print("[Addition Rule - Non-Mutually Exclusive]")
    print(f"Probability of drawing a heart or king: {P_heart_or_king:.2f}")
    print()

if __name__ == "__main__":
    addition_rule_non_mutually_exclusive()