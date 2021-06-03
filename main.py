try:
    x = int(input("Please enter a number: "))
except ZeroDivisionError:
    print("You cannot divide by Zero")
except ValueError:
    print("Please enter a valid Integer")