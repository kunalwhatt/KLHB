# addition_rule_mutually_exclusive.py
# Mutually exclusive events: Rolling 2 or 5

def addition_rule_mutually_exclusive():
    P_2 = 1/6
    P_5 = 1/6
    P_2_or_5 = P_2 + P_5

    print("[Addition Rule - Mutually Exclusive]")
    print(f"Probability of rolling a 2 or 5 on a die: {P_2_or_5:.2f}")
    print()

if __name__ == "__main__":
    addition_rule_mutually_exclusive()