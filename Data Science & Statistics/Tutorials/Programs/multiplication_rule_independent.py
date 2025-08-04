# multiplication_rule_independent.py
# Independent events: Flipping heads and rolling a 6

def multiplication_rule_independent():
    P_heads = 0.5
    P_six = 1/6
    P_heads_and_six = P_heads * P_six

    print("[Multiplication Rule - Independent Events]")
    print(f"Probability of flipping heads and rolling a 6: {P_heads_and_six:.3f}")
    print()

if __name__ == "__main__":
    multiplication_rule_independent()