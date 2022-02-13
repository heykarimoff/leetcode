# Task 1
# A solution to the problem is following:
# - Split the sentence into words.
# - If the length of the words is less than or equal to the length, return the sentence.
# - Otherwise, truncate the words, join them back together and return the result.

# It requires splitting the sentence into words, which takes O(n) time.
# Then it requires concatenating the words back together, which takes O(n) time.
# Time complexity is O(n^2) where n is the length of the sentence.


def solution(sentence, length):
    words = sentence.split()
    if len(words) <= length:
        return sentence
    else:
        return " ".join(words[:length])


# This is more efficient solution which is:
# - Count the number of words in the sentence starting from 0
# - Append each word to the result
# - For each character in the sentence
#     - If the character is a space
#         - Increase the word counter
#     - If the word counter is equal to the length
#         - Break
#     - Append the character to the result
# - Return the result

# It only requires to loop through the characters in the sentence, which takes O(n) time.


def solution(sentence, length):
    counter = 0
    result = ""
    for char in sentence:
        if char == " ":
            counter += 1
        if counter == length:
            break
        result += char
    return result


# Task 2
# Basic solution for the task is following:
# - Calculate the total number of people
# - Count filled cars from 0
# - Sort cars from highest to lowest seat count
# - For each car
#   - Check if there are people left to be seated
#       - If not then break
#   - Reduce the total number of people by the number of people in the car
#   - Increase the number of cars
# - Return the number of cars

# It requires to O(P) time to calculate the total number of people.
# Then it requires to O(SLogS) time to sort the cars from highest to lowest seat count.
# Then it requires to O(S) time to loop through the cars.
# Time complexity is O(P + SLogS + S) where P is the total number of people, S is the number of cars.


def solution(P, S):
    # Calculate the total number of people
    people = sum(P)
    # Count filled cars from 0
    cars = 0
    # Sort cars from highest to lowest seat count
    # For each car
    for seat in sorted(S, reverse=True):
        # Check if there are people left to be seated, if not then break
        if people <= 0:
            break
        # Reduce the total number of people by the number of people in the car
        people -= seat
        # Increase the number of cars
        cars += 1

    return cars


# Task 3
# Basic sollution derived from the problem statement is following:
# We want to have desired total pollution to be less than or equal to
# half of the total pollution of the factories.
# - Calculate the desired pollution target
# - Count filters from zero
# - While the pollution is higher than the target
#   - Find the factory with the highest pollution
#   - Find the index of the factory with the highest pollution
#   - Reduce the pollution of the factory by half
#   - Increase the number of filters
# - Return the number of filters

# There are two ways to implement:
# 1. Using a while loop.
# 2. Using a recursive function.

# It takes O(A) time to calculate the desired pollution target.
# Then it takes O(A) time to find the factory with the highest pollution.
# Time complexity: O(A^2) where A is the number of factories.


def solution(A):
    # Calculate the desired pollution target
    target = sum(A) * 0.5
    # Count filters from zero
    filters = 0
    # While the pollution is higher than the target
    while target < sum(A):
        # Find the factory with the highest pollution
        m = max(A)
        # Find the index of the factory with the highest pollution
        i = A.index(m)
        # Reduce the pollution of the factory by half
        A[i] = m * 0.5
        # Increase the number of filters
        filters += 1

    return filters


# It requires to O(A) time to calculate the desired pollution target.
# Then it requires to O(A) time to find the factory with the highest pollution.
# Time complexity: O(A^2) where A is the number of factories.


def solution(A):
    return calculate_filters(A, sum(A) * 0.5)


def calculate_filters(filters, target):
    # Check if the pollution is higher than the target
    # If not then no filters needed, return 0
    if sum(filters) <= target:
        return 0

    # Find the factory with the highest pollution
    m = max(filters)
    # Find the index of the factory with the highest pollution
    i = filters.index(m)
    # Reduce the pollution of the factory by half
    filters[i] = m * 0.5
    # Add one to the number of filters and keep going
    return 1 + factory_filters_recursive(filters, target)
