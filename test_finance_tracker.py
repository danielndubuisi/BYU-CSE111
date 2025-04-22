from finance_tracker import get_date, get_category, \
        get_amount, get_total_expense, \
        get_total_income, get_transactions, \
        CSV_DATE_FORMAT

from datetime import datetime
import pytest
import pandas as pd


def test_get_date():
    """Tests if get_date returns a valid datetime object
    """
    date_str = "25-10-2024"
    valid_date = datetime.strptime(date_str, CSV_DATE_FORMAT)
    assert get_date(date_str) == valid_date.strftime(CSV_DATE_FORMAT)

    """Tests if get_date returns today's date with allow_default=True
    """
    today = f'{datetime.now():%d-%m-%Y}'
    if get_date("", allow_default=True):
        valid_todays_date = datetime.strptime(today, CSV_DATE_FORMAT)
        assert get_date(today, allow_default=True) == valid_todays_date.strftime(CSV_DATE_FORMAT)


def test_get_amount():
    """Tests if get_amount returns a float for a valid number and
    None for an invalid number, zero value and or negative values

    """
    assert get_amount(100.50) == "100.50"
    assert get_amount("abc") is None
    assert get_amount(0) is None
    assert get_amount(-10) is None


def test_get_category():
    """Tests if get_category returns 'Income' for 'I' and 'Expense' for 'E'
    and None for any other alphanumeric text
    """
    assert get_category("I") == "Income"
    assert get_category("E") == "Expense"
    assert get_category("X") is None
    assert get_category("Invalid Input") is None
    assert get_category("123") is None
    assert get_category("") is None


def test_get_total_income():
    """Tests get_total_income function
    """
    test_df1 = {
        'category': ['Income', 'Expense', 'Income'], 
        'amount': [100, 50, 200]
    }
    test_df2 = {
        'category': ['Expense', 'Expense', 'Expense'], 
        'amount': [20, 10, 83.11]
    }

    mock_df = pd.DataFrame(test_df1)
    mock_df2 = pd.DataFrame(test_df2)
    total_income = get_total_income(mock_df)
    total_income2 = get_total_income(mock_df2)

    assert total_income == 300
    assert total_income2 == 0



def test_get_total_expense():
    """Tests get_total_expense function
    """
    test_df = {
        'category': ['Income', 'Expense', 'Income'], 
        'amount': [100, 50, 200]
    }

    test_df2 = {
        'category': ['Income', 'Income', 'Income'], 
        'amount': [20, 10, 83.11]
    }

    mock_df = pd.DataFrame(test_df)
    mock_df2 = pd.DataFrame(test_df2)
    total_expense = get_total_expense(mock_df)
    total_expense2 = get_total_expense(mock_df2)

    assert total_expense == 50
    assert total_expense2 == 0


def test_get_transactions(mocker):
    """Tests get_transactions function
    """
    df = {
        'date': ['22-11-2023', '01-12-2023', '15-12-2023'],
        'amount': [100, 50, 200],
        'category': ['Income', 'Expense', 'Income'],
        'description': ['Salary', 'Groceries', 'Bonus'],
    }
    mock_df = pd.DataFrame(df)

    start_date = datetime(2023, 11, 25)
    end_date = datetime(2023, 12, 10)

    mocker.patch('pandas.read_csv', return_value=mock_df)
    filtered_df = get_transactions(start_date.strftime("%d-%m-%Y"), end_date.strftime("%d-%m-%Y"))
    filtered_df2 = get_transactions("01-12-2023", "15-12-2023")

    assert len(filtered_df) == 1
    assert len(filtered_df2) == 2
    assert f"{(filtered_df.iloc[0]['date']):%d-%m-%Y}" == "01-12-2023"



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
