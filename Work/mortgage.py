# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
payment = 2684.11

month = 0
while principal > 0:
    month = month + 1
    if extra_payment_start_month <= month <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment

    if current_payment <= principal:
        principal = principal * (1 + rate / 12) - current_payment
        total_paid = total_paid + payment
    else:
        total_paid = total_paid + principal
        principal = 0

    print(f"{month:3d} {round(total_paid, ndigits=2):10.2f} {round(principal, ndigits=2):10.2f}")

print("Total paid", round(total_paid, ndigits=2))
print("Months", month)
