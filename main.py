#!/usr/bin/env python3
"""
Created by: Mr. Coxall
Created on: Sept 2020
This program generates all prime numbers up to a user-specified value.
"""


def main() -> None:
    """The main() function gets a number and prints all primes up to that number."""
    try:
        # Input
        limit = int(input("Enter a positive integer: "))

        if limit < 2:
            print("There are no prime numbers less than 2.")
        else:
            print(f"Prime numbers up to {limit}:")
            for num in range(2, limit + 1):
                is_prime = True
                for i in range(2, int(num**0.5) + 1):
                    if num % i == 0:
                        is_prime = False
                        break
                if is_prime:
                    print(num, end=" ")
            print()  # newline after listing primes

    except ValueError:
        print("Invalid input! Please enter a number.")

    print("\nDone.")


if __name__ == "__main__":
    main()
