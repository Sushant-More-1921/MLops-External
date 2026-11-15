"""
Python Program to Accept Two Numbers and Display Addition
Can be executed in interactive mode or with command line arguments.

Usage:
    Interactive: python addition_cli.py
    Direct args: python addition_cli.py 15 25
"""
import sys
from app.main import addition


def main():
    print("=" * 50)
    print("       Python Addition Program (FastAPI / MLOps)       ")
    print("=" * 50)

    # Argument mode
    if len(sys.argv) == 3:
        try:
            num1 = float(sys.argv[1])
            num2 = float(sys.argv[2])
            res = addition(num1, num2)
            print(f"First number : {num1}")
            print(f"Second number: {num2}")
            print(f"Addition Result: {res}")
            print("=" * 50)
            return
        except ValueError:
            print("[ERROR] Arguments must be numeric values (e.g., python addition_cli.py 10 20)")
            sys.exit(1)

    # Interactive input mode
    try:
        raw1 = input("Enter first number : ")
        num1 = float(raw1.strip())

        raw2 = input("Enter second number: ")
        num2 = float(raw2.strip())

        result = addition(num1, num2)

        print("-" * 50)
        print(f"Addition Result: {num1} + {num2} = {result}")
        print("=" * 50)
    except ValueError:
        print("\n[ERROR] Invalid input! Please enter valid numeric values.")
        sys.exit(1)


if __name__ == "__main__":
    main()

