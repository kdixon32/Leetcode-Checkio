FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]
def sorbets(FLAVORS):
    for i in range(0, len(FLAVORS)):
        
        for j in range(i+1,len(FLAVORS)):
            print(FLAVORS[i] + ", " + FLAVORS[j])
            
sorbets(FLAVORS)