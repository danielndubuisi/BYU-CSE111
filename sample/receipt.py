"""
A program that reads CSV file and prints to the terminal window a receipt while handling errors. For additional features, I added code to print a reminder of how many days until the New Years Sale begins (Jan 1) and a "return by" date at the bottom of the receipt. 
"""

import csv
import datetime
from datetime import datetime as dt


PRODUCT_NUMBER_INDEX = 0
# for product.csv file
PRODUCT_NAME_INDEX = 1
PRICE_INDEX = 2
# for request.csv file
QUANTITY_INDEX = 1

STORE_NAME = 'Inkom Emporium'


def main():
    # try and except block to handle possible errors
    try:
        # call read_dictionary
        products_dict = read_dictionary("products.csv", PRODUCT_NUMBER_INDEX)

        # open request file
        with open('request.csv', "rt") as request_file:
            requests = csv.reader(request_file)
            # skip column headings
            next(requests)

            # Print the store name at the top of the receipt
            print(STORE_NAME)

            # Set initial values for total_items and subtotal due
            total_items = 0
            subtotal = 0

            # loop to get requested items
            for request in requests:
                product_number = request[PRODUCT_NUMBER_INDEX]
                product_quantity = int(request[QUANTITY_INDEX])
                
                if product_number in products_dict:
                    product = products_dict[product_number]

                    name = product[PRODUCT_NAME_INDEX]
                    price = float(product[PRICE_INDEX])

                    # calculate total per product
                    sum_total = product_quantity * price
                    # Print the list of ordered items
                    print(f'{name}: {product_quantity} @ {price}')
            
                    # sum number of items and subtotal
                    total_items += product_quantity
                    subtotal += sum_total

            # calculate sales tax from 6% subtotal
            sales_tax = 0.06 * subtotal

            # calculate total
            total = subtotal + sales_tax

            # print results
            print(f'Number of Items: {total_items}\nSubtotal: {subtotal:.2f}\nSales Tax: {sales_tax:.2f}\nTotal: {total:.2f}')

        # print thank you message
        print(f'Thank you for shopping at the {STORE_NAME}.')

        # get, format and print the current day and time.
        current_date_and_time = dt.now()
        print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")

        # compute difference from today until new year's day sale 
        new_year_date = dt(current_date_and_time.year + 1, 1, 1)
        days_til_sale = (new_year_date - current_date_and_time).days

        # compute return date (within 30 days)
        return_date = current_date_and_time + datetime.timedelta(days=30)
        print(f'\nReturn by: 09:00 PM, {return_date:%b %d %Y}')

        # print new year sale reminder at bottom of receipt
        print(f"\nYou have {days_til_sale} days until new year's sale.")



    except FileNotFoundError as err:
        print('Error: missing file',err, sep='\n')

    except PermissionError as perm_err:
        print("No permission to file", perm_err)

    except KeyError as key_err:
        print("Error: unknown product ID in the request.csv file", key_err)
        


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # create empty compound dictionary
    compound_dictionary = {}

    # read the csv file and populate compound dictionary
    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)

        # skip header
        next(reader)

        for line in reader:
            line_key = line[key_column_index]
            compound_dictionary[line_key] = line

    return compound_dictionary



if __name__ == "__main__":
    main()