import csv

NAME_INDEX = 1
I_NUMBER_LEN = 9

def main():
    i_number = input('Enter student I-Number: ')

    cleaned_i_number = remove_dashes(i_number)
    # alternatively, we can use the replace function
    # cleaned_i_num = i_number.replace("-", "")

    student_dict = read_dictionary('students.csv')

    # Determine if the user input is formatted correctly.
    if not cleaned_i_number.isdigit():
        print("Invalid character in I-Number")
    else:
        if len(cleaned_i_number) < I_NUMBER_LEN:
            print("Invalid I-Number: too few digits")
        elif len(cleaned_i_number) > I_NUMBER_LEN:
            print("Invalid I-Number: too many digits")
        else:
            # The user input is a valid I-Number. Find
            # the I-Number in the list of I-Numbers.
            if cleaned_i_number in student_dict:
                # Retrieve the name that matches the I-Number that the user entered.
                name = student_dict[cleaned_i_number][NAME_INDEX]
                # Print the student name.
                print(name)
                
            else:
                print("No such student")


def read_dictionary(filename, key_column_index=0):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    student_dict = {}

    with open(filename, 'rt') as students_file:
        reader = csv.reader(students_file)

        next(reader)

        for line in reader:
            line_key = line[key_column_index]
            student_dict[line_key] = line 

    return student_dict


def remove_dashes(student_i_num):
    """removes dashes from the string supplied as I-NUmber by students
    returns only a string of digits.
    """
    i_num_list = list(student_i_num)

    for char in i_num_list:
        if char == "-":
            i_num_list.remove(char)

    new_i_num = ''.join(i_num_list)

    return new_i_num



if __name__ == "__main__":
    main()