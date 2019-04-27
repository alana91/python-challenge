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
            if (number % i) is 0:
                return False
        else:
            return True
    else:
        return False

def number_search(ordered_list, number):
    low = 0
    high = len(ordered_list) - 1
    position = bisect_left(ordered_list, number, low, high)
    if(ordered_list[position] is number):
        print("The number is at position {}".format(position))
    else:
        print("The number isn't in the list")

def compare_lists():
    smaller_list = generate_unordered_list(500)
    bigger_list = generate_unordered_list(5000)
    smaller_list_set = set(smaller_list)
    intersection = smaller_list_set.intersection(bigger_list)
    if bool(intersection) is False:
        print("There's nothing in common between the lists")
    else:
        print("Common elements: {}".format(intersection))

def find_prime_numbers(number):
    for n1 in range(2, number + 1):
        for n2 in range(2, n1):
            if n1 % n2 is 0:
                break
        else:
            print(n1)

def is_word_prime(word, letter_dict):
    letter_list = list(word)
    sum = 0
    for letter in letter_list:
        try:
            sum = sum + letter_dict[letter]
        except KeyError:
            print("That's not a valid word.")
            return
    feedback = {True: "It's a prime word", False: "Not a prime word"}
    print(feedback.get(is_prime(sum), ""))

list_ = generate_ordered_list(300)
alphabet_dict = generate_alphabet_dict()

answer = None
while answer is not 5:
    print("""
    1. Find out if a number is in a random 300 number ordered list
    2. Compare two random unordered number lists
    3. Find all prime numbers up to a specified number
    4. Verify if a word is a "prime word"
    5. Quit
    """)
    answer = input("Please, choose an option: ")
    if answer is 1:
        try:
            number = int(input("Choose a number: "))
            number_search(list_, number)
        except ValueError:
            print("That's not a valid number")
    elif answer is 2:
        compare_lists()
    elif answer is 3:
        try:
            number = int(input("Choose a number: "))
            find_prime_numbers(number)
        except ValueError:
            print("That's not a valid number.")
    elif answer is 4:
        word = input("Choose a word: ")
        is_word_prime(word, alphabet_dict)
    elif answer is 5:
        print("\n Bye!") 
    else:
       print("\n Not a valid option. Try again.")


