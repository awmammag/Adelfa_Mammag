#Payment checker

valid_payment_methods = ["cash", "gcash", "card"]

payment_method = input("Please enter your payment method: ").lower()

if payment_method in valid_payment_methods:
    print("Your payment method is valid.")
else:
    print("Your payment method is not valid.")