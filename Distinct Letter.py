import string
def letter_pair():
    letters = string.ascii_lowercase
    for i in range(0, len(letters)):
        for j in range(0, len(letters)):
            if letters[i] != letters[j]:
                print(letters[i]+letters[j])
    
letter_pair()