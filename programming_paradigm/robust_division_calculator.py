# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Try converting inputs to float
        num = float(numerator)
        den = float(denominator)

        # Try performing division
        result = num / den
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle when denominator is zero
        return "Error: Cannot divide by zero."

    except ValueError:
        # Handle when input is not a number
        return "Error: Please enter numeric values only."
