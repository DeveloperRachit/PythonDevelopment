class Animal:
 def eat(self):
  print ("Eating")
class Dog(Animal):
 def bark(self):
   print("barking")
class Testing(Dog):
  def testt(self):
    print("Tested")
d=Testing()
d.eat()
d.bark()
d.testt();
   