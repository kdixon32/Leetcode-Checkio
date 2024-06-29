# Exercise 1
# To fullfill their romance, they want to meet as much as possible. They share their daily paths among Paris districts to know where they can find each other at the same place.

# As you know there is 20 districts in Paris:

# {"Ⅰ", "Ⅱ", "Ⅲ", "Ⅳ", "Ⅴ", "Ⅵ", "Ⅶ", "Ⅷ", "Ⅸ", "Ⅹ", "ⅩⅠ", "ⅩⅡ", "ⅩⅢ", "ⅩⅣ", "ⅩⅤ", "ⅩⅥ", "ⅩⅦ", "ⅩⅧ", "ⅩⅠⅩ", "ⅩⅩ"}
# Code a function named love_meet taking bob and alice's daily paths as two lists and returning a set of the districts they both visit during the day.

# In [1]: from solution import love_meet

# In [2]: alice = ['Ⅱ', 'Ⅳ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅱ']

# In [3]: bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']

# In [4]: love_meet(bob, alice)
# Out[4]: {'Ⅱ', 'Ⅳ'}

# Exercise 2
# Time goes on, and love goes by...

# Alice is bored and get a crush for the strong and handsome Silvester. In order to have an affair with Silvester she must find out where both Silvester and her go during the day. But to avoid an unfortunate encounter with Bob, she must be sure Bob doesn't go there also.

# For the sake of her new love, provide Alice the function affair_meet that takes Bob, Alice and Silvester daily path in Paris, and returns a set of all places where Alice and Silvester can meet and be sure Bob won't be.

# In [1]: from solution import affair_meet

# In [2]: alice = ['Ⅱ', 'Ⅳ', 'Ⅱ', 'ⅩⅠⅩ', 'ⅩⅤ', 'Ⅳ', 'Ⅲ']

# In [3]: bob = ['Ⅳ', 'Ⅲ', 'Ⅱ', 'ⅩⅩ', 'Ⅱ', 'ⅩⅩ']

# In [4]: silvester = ['ⅩVⅢ', 'ⅩⅠⅩ', 'Ⅲ', 'Ⅰ', 'Ⅲ', 'ⅩVⅢ']

# In [5]: affair_meet(bob, alice, silvester)
# Out[5]: {'ⅩⅠⅩ'}

def love_meet(bob, alice):  
    bobset = set(bob)
    aliceset = set(alice)
    intersect = bobset.intersection(aliceset)
    return intersect
    
def affair_meet(bob, alice, silvester):
    bobset = set(bob)
    aliceset = set(alice)
    silvesterset = set(silvester)
    
    intersect = aliceset.intersection(silvesterset)
    difference = intersect.difference(bobset)
    return difference