def is_anagram(left, right):
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters