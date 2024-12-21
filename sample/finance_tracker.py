import pandas as pd
import matplotlib.pyplot as plt
import csv
from datetime import datetime as dt


# constants
CSV_FILE = 'finance_data.csv'
CSV_FILE_COLUMNS = ["date","amount","category","description"]
CSV_DATE_FORMAT = "%d-%m-%Y"


def main():
    print('\nHELLO THERE!👋 WELCOME TO YOUR FINANCE TRACKER!📖')
    print('TRACK YOUR INCOME📈 AND EXPENSES📉 AND TAKE CONTROL OF YOUR FINANCES TODAY!')

    # initialize the csv file(database) to prepare for user action
    initialize_csv()

    while True:
        # looping help commands
        print('\n1. Add a new transaction')
        print('2. View all transactions summary within a date range')
        print('3. Exit')

        # get user choice 
        choice = int(input('Select an option (1-3): '))

        # if user choice is 1, add a new transaction
        if choice == 1:
            # get date, amount, category and description from user
            date = get_date(input("Type Transaction date (dd-mm-yyyy) or press Enter for today: "))
            # check and make recursive until valid response
            while date == None:
                date = get_date(input("Invalid date format. Please enter correct format (Example: 01-01-2001): "))

            amount = get_amount(input('Enter amount: '))
            # check and make recursive until valid response
            while amount == None:
                amount = get_amount(input("Amount must be greater than zero: "))

            category = get_category(input("Enter the category ('I' for Income or 'E' for Expense): ").upper())
            # check and make recursive until valid response
            while category == None:
                category = get_category(input("Invalid category, Please enter 'I' for Income or 'E' for Expense: ").upper())

            # no checks for description as it is optional
            description = get_description(input('Enter a description for transaction (optional): '))

            # add new user transaction
            add_entry(date, amount, category, description)
            print("Transaction added successfully!")


        # if user choice is 2, show all transactions within specified range
        elif choice == 2:
            start_date = input('Enter start date (dd-mm-yyyy): ')
            end_date = input('Enter end date (dd-mm-yyyy): ')
            
            # get all transactions in this period
            filtered_df = get_transactions(start_date, end_date)

            # # check if filtered dataframe is empty
            if filtered_df.empty:
                print('No transactions found in the given range')
            else:
                print(f'Transactions from {start_date} to {end_date}')
                print(filtered_df.to_string(index=False, formatters={"date": lambda x: x.strftime(CSV_DATE_FORMAT)}))

                print('\nYour transaction Summary:')
                total_income = get_total_income(filtered_df)
                print(f'Total Income: ${total_income:.2f}')

                total_expense = get_total_expense(filtered_df)
                print(f'Total Expense: ${total_expense:.2f}')

                print(f'Net savings: ${(total_income - total_expense):.2f}')

                # show plot to user
                show_plot = input('Do you want to see a graph (y/n)? ').lower()

                if show_plot == "y":
                    plot_transactions(filtered_df)


        # if user choice is 3, end program
        elif choice == 3:
            print('Exiting...')
            break

        # if user enters anything else
        else:
            print('Invalid choice. Enter 1, 2 or 3...')
    
    print('\nThank you for using FINANCE TRACKER...🤗')


def initialize_csv():
    """This function creates a csv file if not found
    and reads it into a pandas dataframe with the specified columns
    headers of date,amount,category,description
    """
    try:
        pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(
            columns=CSV_FILE_COLUMNS
        )
        df.to_csv(CSV_FILE, index=False)


def add_entry(date, amount, category, description):
    """The add_entry function adds user's transaction date, amount, category and description
    to the csv file
    returns: None, prints a success message if no errors encountered
    """
    # create a new entry dictionary
    new_entry = {
        "date": date,
        "amount": amount,
        "category": category,
        "description": description,
    }
    # open csv file and add entry
    with open(CSV_FILE, mode="at", newline="") as csv_file:
        # take the dictionary and write it into the csv file
        writer = csv.DictWriter(csv_file, fieldnames=CSV_FILE_COLUMNS)
        writer.writerow(new_entry)


def get_date(date_str, allow_default=False):
    """This function that returns a valid datetime in this format (dd-mm-yyyy)
    Args:
        date_str (str): a date string
        allow_default (bool, optional): If false, and no date string provided, use current day. Defaults to False.
    Returns:
        datetime: returns a date in the specified format or None
    """
    if not allow_default and not date_str:
        today = dt.today()
        return f'{today.strftime(CSV_DATE_FORMAT)}'
    
    try:
        valid_date = dt.strptime(date_str, CSV_DATE_FORMAT)
        return f'{valid_date.strftime(CSV_DATE_FORMAT)}'

    except  ValueError:
        return None


def get_amount(amt):
    """This function returns an amount as a floating point value and checks value is greater than zero
    Args:
        amt (str): str, int or floating point value
    Returns:
        float: Returns a float value greater than zero and not alphanuremic or None
    """
    try:
        amount = float(amt)
        # check that amount is greater than zero
        if amount <= 0:
            raise ValueError
        return f'{amount:.2f}'

    except ValueError:
        return None


def get_category(category):
    """This function checks if transaction category is Invoice or Expense and returns value
    returns None if neither 'I' nor 'E' supplied
    Args:
        category (str): value must be 'I' for Income or 'E' for Expense
    Returns:
        str : Returns a string of Income , Expense or None 
    """
    CATEGORIES = {"I": "Income", "E": "Expense"}

    if category in CATEGORIES:
        return CATEGORIES[category]
    else:
        return None


def get_description(desc):
    """returns description as string
    """
    return desc


def get_transactions(start_date, end_date):
    """This function takes two args as start and end dates using these to
    filter transactions between the specified range
    Args:
        start_date (str): start date in format dd-mm-yyyy
        end_date (str): end date in format dd-mm-yyyy
    Returns:
        dataframe (Any): returns a filtered object of transactions between specified range
    """
    # read data from csv file with pandas
    df = pd.read_csv(CSV_FILE)

    # access all data in date column, format to datetime object
    df["date"] = pd.to_datetime(df["date"], format=CSV_DATE_FORMAT, dayfirst=True)

    # format start and end date to datetime object
    start_date = dt.strptime(start_date, CSV_DATE_FORMAT)
    end_date = dt.strptime(end_date, CSV_DATE_FORMAT)

    # compare and filter based on dates with mask
    mask = (df["date"] >= start_date) & (df["date"] <= end_date)

    # filter the dataframe with only rows that return true to mask
    # filtered_df = df.loc(mask)
    filtered_df = df[mask]

    # return filtered data
    return filtered_df


def get_total_income(fltrd_df):
    """This function calculates the total income in a filtered dataframe from
    a specified range of transactions
    Args:
        fltrd_df (dataframe): a filtered dataframe with values in a specified range
    Returns:
        float: returns a sum of all income transactions from filtered dataframe
    """
    total_income = fltrd_df[fltrd_df["category"] == "Income"]["amount"].sum()
    return float(total_income)


def get_total_expense(fltrd_df):
    """This function calculates the total expense in a filtered dataframe from
    a specified range of transactions
    Args:
        fltrd_df (dataframe): a filtered dataframe with values in a specified range
    Returns:
        float: returns a sum of all expense transactions from filtered dataframe
    """
    total_expense = fltrd_df[fltrd_df["category"] == "Expense"]["amount"].sum()
    return float(total_expense)


def plot_transactions(df):
    """This function uses matplotlib to plot the transaction amount over a specified date range on a graph for the user to see. 
    It takes one argument which is the filtered dataframe of the transactions in a specific date range
    Args:
        df (dataframe): A dataframe object that contains select data from a specified date range.
    """
    # find date row from dataframe with set_index
    df.set_index("date", inplace=True)

    # Sort DataFrame by date (ascending order)
    df = df.sort_index(ascending=True)

    # take only income data from dataframe, fill empty day rows in data to have a value of zero with resample, sum and reindex
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        )
    
    # take only expense data from dataframe, fill empty day rows in data to have a value of zero with resample, sum and reindex
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
        )

    # plot the graph
    plt.figure(figsize=(10, 5))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.title("Income - Expense Chart")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    main()