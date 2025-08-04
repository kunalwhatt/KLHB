# bayes_theorem_example.py
# Bayes Theorem Example: Medical diagnosis

def bayes_theorem_example():
    P_D = 0.005
    P_not_D = 0.995
    P_T_given_D = 0.99
    P_T_given_not_D = 0.05

    P_T = P_T_given_D * P_D + P_T_given_not_D * P_not_D
    P_D_given_T = (P_T_given_D * P_D) / P_T

    print("[Bayes Theorem]")
    print(f"Probability of having the disease after positive test: {P_D_given_T:.2%}")
    print()

if __name__ == "__main__":
    bayes_theorem_example()