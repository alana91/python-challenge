from random import randint
from bisect import bisect_left
from string import ascii_letters

def generate_alphabet_dict():
    alphabet_list = list(ascii_letters)
    alphabet_values = list(range(1, 53))
    alphabet_dict = dict(zip(alphabet_list, alphabet_values))
    return alphabet_dict

def generate_ordered_list(range_value):
    ordered_list = [randint(0, 1000) for x in range(range_value)]
    ordered_list.sort()
    return ordered_list

def generate_unordered_list(range_value):
    unordered_list = [randint(0, 5000000) for x in range(range_value)]
    return unordered_list

def is_prime(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                return "Not a prime word"
        else:
            return "It's a prime word"
    else:
        return "Not a prime word"

def number_search(ordered_list, number):
    low = 0
    high = len(ordered_list) - 1
    position = bisect_left(ordered_list, number, low, high)
    if(ordered_list[position] == number):
        print("The number is at position {}".format(position))
    else:
        print("The number isn't in the list")

def compare_lists():
    smaller_list = generate_unordered_list(500)
    bigger_list = generate_unordered_list(5000)
    smaller_list_set = set(smaller_list)
    intersection = smaller_list_set.intersection(bigger_list)
    if bool(intersection) == False:
        print("There's nothing in common between the lists")
    else:
        print("Common elements: {}".format(intersection))

def find_prime_numbers(number):
    for n1 in range(2, number + 1):
        for n2 in range(2, n1):
            if n1 % n2 == 0:
                break
        else:
            print(n1)

def is_word_prime(word):
    alphabet_dict = generate_alphabet_dict()
    letter_list = list(word)
    sum = 0
    for letter in letter_list:
        try:
            sum = sum + alphabet_dict[letter]
        except KeyError:
            print("That's not a valid word.")
            return
    print(is_prime(sum))

list_ = generate_ordered_list(300)

answer = None
while answer != "5":
    print("""
    1. Find out if a number is in a random 300 number ordered list
    2. Compare two random unordered number lists
    3. Find all prime numbers up to a specified number
    4. Verify if a word is a "prime word"
    5. Quit
    """)
    answer = input("Please, choose an option: ")
    if answer == "1":
        try:
            number = int(input("Choose a number: "))
            number_search(list_, number)
        except ValueError:
            print("That's not a valid number")
    elif answer == "2":
        compare_lists()
    elif answer == "3":
        try:
            number = int(input("Choose a number: "))
            find_prime_numbers(number)
        except ValueError:
            print("That's not a valid number.")
    elif answer == "4":
        word = input("Choose a word: ")
        is_word_prime(word)
    elif answer == "5":
        print("\n Bye!") 
    else:
       print("\n Not a valid option. Try again.")


