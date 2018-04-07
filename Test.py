class Student:
	def __init__(self,name,*marks):
		self.name=name
		self.marks = marks
	def prints(self):
		print("The name of the student is ",self.name " and his marks are" [] [] []",format(self.marks[0],self.marks[1],self.marks[2]))
name = input("Enter the name of the student")
marks = []
print("Enter marks in the three subjects")
i = 0
for i in range(3):
	marks.append(int(input()))

h = Student(name,*marks)        
h.prints()
