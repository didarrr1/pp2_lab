#task1
def grams_to_ounces(grams):
    return grams / 28.3495231

#task2
def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

#task3
def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    if x >= 0 and y >= 0 and (2 * x + 4 * y == numlegs):
        return f"Chickens: {x}, Rabbits: {y}"
    else:
        return "No valid solution"

#task4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

#task5
from itertools import permutations
def print_permutations(s):
    perm_list = [''.join(p) for p in permutations(s)]
    for perm in perm_list:
        print(perm)

#task6
def reverse_words(sentence):
    return ' '.join(sentence.split()[::-1])

#task7
def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

#task8
def spy_game(nums):
    code = [0, 0, 7]  
    for num in nums:
        if num == code[0]: 
            code.pop(0)
        if not code: 
            return True
    return False 

#task9
import math
def sphere_volume(radius):
    return (4/3) * math.pi * radius**3

#task10
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:  
            unique_list.append(item)
    return unique_list

#task11
def is_palindrome(s):
    cleaned_s = ''.join(s.lower().split())
    return cleaned_s == cleaned_s[::-1]

#task12
def histogram(lst):
    for num in lst:
        print('*' * num)

#task13
import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()
    number_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    attempts = 0

    while True:
        print("Take a guess.")
        try:
            guess = int(input())
            attempts += 1
            if guess < number_to_guess:
                print("Your guess is too low.")
            elif guess > number_to_guess:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break



