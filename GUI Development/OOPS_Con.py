class Chair():
 def __init__(self, name, legs=4):
  self.name = name
  self.legs = legs
 def display(self):
     print(self.name, "\t", self.legs) 
chair1=Chair("Barcelona")
chair1.display()
chair2=Chair("Bar Stool", 1)
chair2.display()