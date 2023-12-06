class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def saxeliasaki(self):
      print(f"persons name is {self.name} persons age is {self.age}")

p1 = Person("John", 36)
p1.saxeliasaki()
p1.age = 32
print(p1.age)
