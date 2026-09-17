pin = input("Please enter your PIN: ")

if len(pin) == 6 and pin.isdigit():
    print("Valid PIN: ", pin)
if len(pin) != 6 and pin.isdigit():
    print("Invalid PIN: Enter exactly 6 digits")
