def find_missing_number(nums):
  n = len(nums) + 1
  expected_sum = n * (n + 1) // 2
  actual_sum = sum(nums)
  return expected_sum - actual_sum

def is_balanced_parentheses(s):
  stack = []
  mapping = {')': '(', '}': '{', ']': '['}
  for char in s:
    if char in mapping.values():
      stack.append(char)
    elif char in mapping:
      if not stack or stack[-1] != mapping[char]:
        return False
      stack.pop()
  return not stack


def longest_word(sentence):
  words = sentence.split()
  if not words:
    return ''
  return max(words, key=len)


def count_words(sentence):
  return len(sentence.split())


def is_pythagorean_triplet(a, b, c):
  sides = sorted([a, b, c])
  return sides[0]**2 + sides[1]**2 == sides[2]**2


print(find_missing_number([1,2,4,5]))
print(is_balanced_parentheses("({[]})"))
print(longest_word("Find the longest word here"))
print(count_words("Count the number of words"))
print(is_pythagorean_triplet(3, 4, 5))