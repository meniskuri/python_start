class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("waw waw")


class Cat(Mammal):
    def miau(self):
        print("miauu miauu")


x = Dog()
x.walk()
x.bark()

y = Cat()
y.walk()
y.miau()
