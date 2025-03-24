from itertools import combinations

def enhanced_vesely_beta(M, beta_list):
    N = len(beta_list)
    beta_eff = 0.0

    for k in range(M, N + 1):
        for combo in combinations(range(N), k):
            prob = 1.0
            for i in range(N):
                if i in combo:
                    prob *= beta_list[i]
                else:
                    prob *= (1 - beta_list[i])
            beta_eff += prob

    return beta_eff

def main():
    while True:
        try:
            M = int(input("Enter M (minimum required components): "))
            N = int(input("Enter N (total redundant components): "))

            if M > N:
                print("Error: M must be less than or equal to N.")
                continue

            beta_list = []
            print("\nEnter individual beta values for each channel (e.g., 0.05 for 5%):")
            for i in range(N):
                beta = float(input(f"  Channel {i+1} beta: "))
                if not (0 <= beta <= 1):
                    raise ValueError("Beta must be between 0 and 1.")
                beta_list.append(beta)

            result = enhanced_vesely_beta(M, beta_list)
            print(f"\nSystem-wide effective beta for {M}oo{N} configuration: {result:.6f} ({result*100:.4f}%)\n")

        except Exception as e:
            print(f"Invalid input: {e}")

        choice = input("Do you want to calculate another? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()