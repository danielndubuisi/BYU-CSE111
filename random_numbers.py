import random

def main():
    """Has no parameters. Creates a list named numbers and prints the numbers list
    Calls the append_random_numbers function with only one argument to add one number to numbers
    Prints the numbers list
    Calls the append_random_numbers function again with two arguments to add three numbers to numbers
    Prints the numbers list
    """    
    words = []

    numbers = [16.2, 75.1, 52.3]
    print(numbers)

    append_random_numbers(numbers)
    print(numbers)

    append_random_numbers(numbers, 3)
    print(numbers)

    append_random_words(words, 6)

def append_random_numbers(numbers_list, quantity=1):
    """Has two parameters: a list named numbers_list and an integer named quantity. 
    The parameter quantity has a default value of 1
    Computes quantity pseudo random numbers by calling the random.uniform function.
    Rounds the quantity pseudo random numbers to one digit after the decimal.
    Appends the quantity pseudo random numbers onto the end of the numbers_list.
    """
    counter = 0
    while counter < quantity:
        random_number = round(random.uniform(1.0,99.9), 1)
        numbers_list.append(random_number)
        counter +=1
    return numbers_list


def append_random_words(words_list, quantity=1):
    """Has two parameters: a list named words_list and an integer named quantity. 
    The parameter quantity has a default value of 1
    Randomly selects quantity words from a list of words and appends the selected words at the end of words_list.
    """

    words = ['join', 'love','create', 'bully', 'black', 'random', 'smile', 'love', 'cloud', 'head', 'furnish', 'abstract', 'run', 'rampage', 'xylophone', 'individual', 'corrupt', 'old']

    counter = 0
    while counter < quantity:
        random_word = random.choice(words)
        words_list.append(random_word)
        counter +=1
    print(words_list)



if __name__ == "__main__":
    main()