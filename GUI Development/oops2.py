class Rectangle(object):
 def __init__(self, width, height):
  self.width = width
  self.height = height
 def getWidth(self):
  return self.width
 def setWidth(self, width):
  self.width = width
 def getHeight(self):
  return self.height
 def setHeight(self, height):
  self.height = height
 def area(self):
  return self.getWidth() * self.getHeight()
rect = Rectangle(50, 10)
print (rect.area()) # Prints "500"
rect.setWidth(20)