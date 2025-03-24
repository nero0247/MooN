from math import comb

def calculate_beta(M, N, beta_base):
    if M > N:
        return "Error: M must be less than or equal to N."
    return sum(comb(N, k) * (beta_base ** k) * ((1 - beta_base) ** (N - k)) for k in range(M, N + 1))

def main():
    while True:
        try:
            M = int(input("Enter M (minimum required components): "))
            N = int(input("Enter N (total redundant components): "))
            beta = float(input("Enter base beta (e.g., 0.05 for 5%): "))

            result = calculate_beta(M, N, beta)
            print(f"\nSystem wide beta for {M}oo{N} system with base β = {beta:.2f}: {result:.6f}\n")
        except Exception as e:
            print("Invalid input. Try again.")

        choice = input("Do you want to calculate another? (y/n): ").lower()
        if choice != 'y':
            break

if __name__ == "__main__":
    main()