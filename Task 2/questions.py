def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1): 
        if n % i == 0:
            return False
    return True

print("Is 17 prime?", is_prime(17))  

def sum_of_digits(n):
    return sum(int(digit) for digit in str(abs(n)))

print("Sum of digits in 1234:", sum_of_digits(1234))

import math

def lcm_and_gcd(a, b):
    gcd_val = math.gcd(a, b)
    lcm_val = abs(a * b) // gcd_val
    return lcm_val, gcd_val

a, b = 12, 18
lcm, gcd = lcm_and_gcd(a, b)
print(f"LCM: {lcm}, GCD: {gcd}")

def reverse_list(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1
    return lst

print("Reversed List:", reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

def sort_list(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

print("Sorted List:", sort_list([5, 2, 8, 1, 3]))  # Output: [1, 2, 3, 5, 8]

def remove_duplicates(lst):
    return list(set(lst))

print("Without Duplicates:", remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # Output: [1, 2, 3, 4, 5]

def string_length(s):
    count = 0
    for _ in s:
        count += 1
    return count

print("Length of 'hello':", string_length("hello"))  # Output: 5

def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    vowel_count = consonant_count = 0

    for ch in s:
        if ch.isalpha():  # Only count letters
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Example
vowels, consonants = count_vowels_consonants("Hello World!")
print("Vowels:", vowels)        # Output: 3
print("Consonants:", consonants)  # Output: 7

