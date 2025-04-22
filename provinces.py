"""
Write a Python program named provinces.py that reads the contents of provinces.txt into a list and then modifies the list. Your program must do the following:

Open the provinces.txt file for reading.
Read the contents of the file into a list where each line of text in the file is stored in a separate element in the list.
Print the entire list.
Remove the first element from the list.
Remove the last element from the list.
Replace all occurrences of "AB" in the list with "Alberta".
Count the number of elements that are "Alberta" and print that number.
"""
def main():
    # call function to read the file
    provinces_list = read_list('provinces.txt')
    # print list
    print(provinces_list)

    # remove first element from the list
    provinces_list.pop(0)
    # remove last element from the list
    provinces_list.pop()

    # Replace all occurrences of "AB" in the list with "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] == 'AB':
            provinces_list[i] = "Alberta"

    # Count the number of elements that are "Alberta" and print that number.
    alberta_count = provinces_list.count('Alberta')        

    print(f'Alberta occurs {alberta_count} times in the modified list')


def read_list(filename):
    with open(filename, 'rt') as provinces_file:
        all_provinces = []
        for line in provinces_file:
            clean_line = line.strip()
            all_provinces.append(clean_line)

    return all_provinces



if __name__ == "__main__":
    main()