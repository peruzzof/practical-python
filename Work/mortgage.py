# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    if (extra_payment_start_month <= month and extra_payment_end_month > month):
        total_paid = total_paid + extra_payment
        principal = principal - extra_payment
    print(f'{month:3d} {total_paid:10.2f} {principal:10.2f}')

if (principal < 0):
    total_paid = total_paid + principal
    
print(f'Total paid {total_paid:0.2f} after {month} months')
