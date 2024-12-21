"""
Problem Statement -
You work for a retail store that wants to increase sales on Tuesday and Wednesday which are the store’s slowest sales days. On Tuesday and Wednesday, if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""

# from datatime module import the datetime class
from datetime import datetime as dt


# get current date and time from computer O.S
current_date_and_time = dt.now()

# get weekday from this value
current_weekday = current_date_and_time.weekday() #returns int of 0 for monday and 6 for sunday
# current_weekday = 2 #to test on other days

# Get customer input
# subtotal = float(input('Please enter the subtotal: '))

# Customer input loop
user_price = ''
subtotal = 0

while user_price != 0:
    user_price = float(input('What is the item price?(type zero to quit) '))
    if user_price != 0:
        quantity = int(input('What is the quantity? '))
    subtotal += user_price * quantity

print(f'Your subtotal is {subtotal}')

# check subtotal and weekday (tues == 1, wed == 2)
if subtotal >= 50 and (current_weekday == 1 or current_weekday == 2):
    # calculate 10% discount value
    discount = 0.1 * subtotal
    # calculate 6% sales tax
    sales_tax = 0.06 * (subtotal - discount)
    # calculate total amount due
    total_due = sales_tax + (subtotal - discount)

    print(f' Discount amount: {discount:.2f}\n Sales tax amount: {sales_tax:.2f}\n Total: {total_due:.2f}')
elif subtotal < 50 and (current_weekday == 1 or current_weekday == 2):
    # calculate difference
    difference = 50 - subtotal
    # calculate 6% sales tax
    sales_tax = 0.06 * subtotal
    # calculate total amount due
    total_due = sales_tax + subtotal

    print(f' You only need to purchase ${difference:.2f} more to get 10% discount. \n Sales tax amount: {sales_tax:.2f}\n Total: {total_due:.2f}')
else:
    # calculate sales tax and total due
    sales_tax = 0.06 * subtotal
    total_due = sales_tax + subtotal

    print(f' Sales tax amount: {sales_tax:.2f}\n Total: {total_due:.2f}')


