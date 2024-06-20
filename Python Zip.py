#Create a dictionary with zip
#You can create dictionaries in Python by feeding key-value pairs to the dict function, 
#which means zip is a prime way of creating dictionaries when you have all the keys in an iterator and all the values in another iterator

def zippy():
    firsts = ["Anna", "Bob", "Charles"]
    lasts = ["Smith", "Doe", "Evans"]
    combined = dict(zip(firsts, lasts))
    return combined
print(zippy())
    # {'Anna': 'Smith', 'Bob': 'Doe', 'Charles': 'Evans'}