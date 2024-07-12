class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def name(self):
        return f"{self.first} {self.last}"
    
# Original Problem that this fixes:  
#   >>> john = Person("John", "Doe")
#   >>> john.name
# 'John Doe'
#   >>> john.last = "Smith"
#   >>> john.name
# # ?