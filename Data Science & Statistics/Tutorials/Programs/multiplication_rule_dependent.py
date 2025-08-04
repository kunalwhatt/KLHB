# multiplication_rule_dependent.py
# Dependent events: Drawing 2 aces in a row

def multiplication_rule_dependent():
    P_first_ace = 4/52
    P_second_ace_given_first = 3/51
    P_two_aces = P_first_ace * P_second_ace_given_first

    print("[Multiplication Rule - Dependent Events]")
    print(f"Probability of drawing 2 aces in a row: {P_two_aces:.4f}")
    print()

if __name__ == "__main__":
    multiplication_rule_dependent()