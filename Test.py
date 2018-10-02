Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Test:
	"This is JavaTpoint"
	a=50
	def func(self)
	
SyntaxError: invalid syntax
>>> class Test:
	"This is the java Point"
	a=40
	def func(self):
		print("hello Function")
		

>>> Test.a
40
>>> Test._doc_
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    Test._doc_
AttributeError: type object 'Test' has no attribute '_doc_'
>>> Test.__doc__
'This is the java Point'
>>> Test.func
<function Test.func at 0x000001D4ADEEF0D0>
>>> ob=Test()
>>> ob.func()
hello Function
>>> class Student:
	def __init
	
SyntaxError: invalid syntax
>>> class Student:
	def __init__(self, rollno, name):
		self.rollno=rollno
		self.name=name
		def displayStu(self):
			print "rollno :" self.rollno, "name:" self.name
			
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("rollno :" self.rollno, "name:" self.name)?
>>> class Student:
	def __init__(self, rollno, name):
		self.rollno=rollno
		self.name=name
		def displayStu(self):
			print "rollno :" self.rollno, "name:", self.name
			
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("rollno :" self.rollno, "name:", self.name)?
>>> class Student:
	def __init__(self, rollno, name):
		self.rollno=rollno
		self.name=name
		def displayStu(self):
			print ("rollno :",self.rollno, "name:",self.name)
			emp1=Student(121,"Ajeet")
			emp2=Student(122, "Sonoo")
			emp1.displayStu()
			emp2.displayStu()
			
