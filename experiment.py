class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(f'My name if {p1.name} and I am {p1.age:.5f} old')