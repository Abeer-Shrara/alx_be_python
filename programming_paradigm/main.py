# main.py
import sys
from robust_division_calculator import safe_divide

def main():
    # Check if user provided exactly 2 arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        sys.exit(1)  # Exit with error code

    numerator = sys.argv[1]      # first input after filename
    denominator = sys.argv[2]    # second input after filename

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()
