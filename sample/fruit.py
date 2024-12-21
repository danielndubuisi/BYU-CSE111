def main():
    # Create and print a list named fruit.
    fruit_list = ["pear", "banana", "apple", "mango"]
    print(f"original: {fruit_list}")
    # reverse fruit_list
    fruit_list.reverse()
    print(f'reversed: {fruit_list}')
    # append orange to list
    fruit_list.append("orange")
    print(f"append orange: {fruit_list}")
    # find apple and insert cherry before it to list
    i = fruit_list.index("apple")
    fruit_list.insert(i, "cherry")
    print(fruit_list)
    # remove banana
    fruit_list.remove('banana')
    print(f'remove banana: {fruit_list}')
    # pop last element from list
    last = fruit_list.pop()
    print(f'Popped item: {last}, fruit_list: {fruit_list}')
    # sort list
    fruit_list.sort()
    print(fruit_list)
    # clear list
    fruit_list.clear()
    print(fruit_list)


if __name__ == "__main__":
    main()