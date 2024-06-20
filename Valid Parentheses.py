# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(self, s):
    past = []
    left = ['(', '{', '[']
    right = [')', '}', ']']
    for elem in range(0, len(s)):
        if s[elem] in left:
            past.append(s[elem])
        if s[elem] in right:
            if not past:
                return False
            if right.index(s[elem]) == left.index(past[-1]):
                past.pop()
            else: 
                return False
    if not past:
        return True
    return False