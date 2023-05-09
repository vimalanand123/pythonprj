print("hi hello")

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
p1 = Person("John", 36)

x = 300

def myfunc():

  x = 200
  print(x)

myfunc()

print(x)

print(p1)