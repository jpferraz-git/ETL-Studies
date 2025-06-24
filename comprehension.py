from setuptools.command.build_ext import if_dl


def setComprehension():
    squares = {i ** 2 for i in range(10)}
    print(squares)

def listComprehension():
    pars = [i % 2 == 0 for i in range(10)]
    print(pars)

def tupleComprehension():
    no_pars = ([i % 2 != 0 for i in range(10)])
    print(no_pars)

def dictionaryComprehension():
    banana = "banana"
    vogals_in_banana = {i: banana[i] for i in range(len(banana)) if banana[i] == "a"}
    print(vogals_in_banana)

def comprehensionExercises():
    fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

    numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

    # Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]
    exercise1 = [fruits[uppercased_fruits].upper() for uppercased_fruits in range(len(fruits))]
    print(exercise1)

    # Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]
    exercise2 = [fruits[capitalized_fruits][0].upper() + fruits[capitalized_fruits][1:] for capitalized_fruits in range(len(fruits))]
    print(exercise2)

    # Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.
    vowels = "aeiouAEIOU"
    exercise3 = [fruits_with_more_than_two_vowels for fruits_with_more_than_two_vowels in range(len(fruits)) if any(letter in vowels for letter in fruits)]

    print(exercise3)

    # Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']
    exercise4 = [fruits_with_only_two_vowels for fruits_with_only_two_vowels in range(len(fruits)) if any(letter in vowels for letter in fruits)]
    print(exercise4)

    # Exercise 5 - make a list that contains each fruit with more than 5 characters
    exercise5 = [fruits[i] for i in range(len(fruits)) if len(fruits[i]) > 5]
    print(exercise5)

    # Exercise 6 - make a list that contains each fruit with exactly 5 characters
    exercise6 = [fruits[i] for i in range(len(fruits)) if len(fruits[i]) == 5]
    print(exercise6)

    # Exercise 7 - Make a list that contains fruits that have less than 5 characters
    exercise7 = [fruits[i] for i in range(len(fruits)) if len(fruits[i]) < 5]
    print(exercise7)

    # Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]
    exercise8 = [len(fruits[i]) for i in range(len(fruits)) ]
    print(exercise8)

    # Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"
    exercise9 = [fruits[i] for i in range(len(fruits)) if any(letter in fruits[i] for letter in fruits[i] if letter == "a")]
    print(exercise9)

    # Exercise 10 - Make a variable named even_numbers that holds only the even numbers
    exercise10 = [len(fruits[i]) for i in range(len(fruits)) for j in range(len(fruits)) if len(fruits[i]) == len(fruits[j])]
    print(exercise10)

    # Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
    exercise11 = [i for i in range(1, 11) for j in range(1, 11) if i == j]
    print(exercise11)

    # Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers
    exercise12 = [i for i in range(-10, 11) if i >= 0]
    print(exercise12)

    # Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers
    exercise13 = [i for i in range(-10, 11) if i < 0]
    print(exercise13)

    # Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals
    exercise14 = [i for i in range(1, 101) if i >= 10]
    print(exercise14)

    # Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]
    exercise15 = [i * i for i in range(1, 11)]
    print(exercise15)

    # Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.
    exercise16 = [i for i in range(-20, 10) if i % 2 == 0 and i < 0]
    print(exercise16)

    # Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five.
    exercise17 = [i + 5 for i in range(0, 11)]
    print(exercise17)

    # BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
    bonus = [i for i in range(0, 11) if prime(i) == 1]
    print(bonus)

def prime(prime_number):
    true_prime_number = 1
    for i in prime_number:
        if prime_number / true_prime_number == true_prime_number:
            true_prime_number = prime_number
        if true_prime_number != 1:
            break


# setComprehension()
# listComprehension()
# tupleComprehension()
# dictionaryComprehension()

comprehensionExercises()
