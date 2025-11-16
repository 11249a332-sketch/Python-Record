try:
    x = int("str")  # This will cause ValueError
    inv = 1 / x  # Inverse calculation

except ValueError:
    print("Not Valid! Give only integer input")

except ZeroDivisionError:
    print("Zero has no inverse!")
