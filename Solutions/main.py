from DPSolution import DPS
from RecursiveSolution import RecFib

def main():
    print("Welcome to our 428 - Fibonacci Sequence Project")
    solution = 0

    while solution != -1:
        print("\nPlease choose which sequence you want to visualize:")
        print("1. Recursive")
        print("2. Dynamic Programming")
        print("Type -1 to exit.")

        # Get user choice
        try:
            solution = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if solution == -1:
            break

        if solution not in [1, 2]:
            print("Not a valid number, please enter 1 or 2.")
            continue
        
        # Get Fibonacci number to compute
        try:
            n = int(input("Enter the Fibonacci number to compute: "))
        except ValueError:
            print("Invalid input, defaulting n = 3")
            n = 3

        print("\n--- Visualization Output ---\n")

        if solution == 1:
            result = RecFib.fib_recursive(n)
            print(f"\nFinal result (Recursive): {result}")

        elif solution == 2:
            result = DPS.fib_dp(n)
            print(f"\nFinal result (Dynamic Programming): {result}")

        print("\n-------------------------------------")
        print("Enter -1 to exit or any other number to continue.")

        try:
            solution = int(input("Your choice: "))
        except ValueError:
            solution = 0  # Continue loop

    print("Thank you for using our program!")

if __name__ == "__main__":
    main()
