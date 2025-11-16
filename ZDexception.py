try:
    numerator = int(input("Enter a numerator: "))
    denominator = int(input("Enter a denominator: "))
    result = numerator / denominator
except ValueError:
    # Handles invalid input (e.g., non-integer)
    print("Invalid input. Please enter an integer.")
except ZeroDivisionError:
    # Handles division by zero
    print("Error: Cannot divide by zero.")
except Exception as e:
    # Catches any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
else:
    # Executed if no exception occurred in the try block
    print(f"The result of the division is: {result}")
finally:
    # Always executed, regardless of exceptions
    print("Program execution completed.")
