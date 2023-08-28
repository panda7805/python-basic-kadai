class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def print_info(self):
        print(self.name)
        print(self.age)

person = Human("nishio", 30)
person.print_info()
