#!/usr/bin/env python3
"""
Created by: Mr. Coxall
Created on: Sept 2020
This program generates all prime numbers up to a user-specified value.
"""


def main() -> None:
    """Gets a number and prints all primes up to that number."""
    try:
        # Input
        user_limit = int(input("Enter a positive integer: "))

        if user_limit < 2:
            print("There are no prime numbers less than 2.")
        else:
            print(f"Prime numbers up to {user_limit}:")
            for current_number in range(2, user_limit + 1):
                is_prime = True
                for test_divisor in range(2, int(current_number ** 0.5) + 1):
                    if current_number % test_divisor == 0:
                        is_prime = False
                        break

                if is_prime:
                    print(current_number, end=" ")

            print()  # newline after listing primes

    except ValueError:
        print("Invalid input! Please enter a number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
    
