from math import sqrt
class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def __str__(self):
		return "this is a string method"
	def __add__(self,other):
		return (self.x+other.x,self.y+other.y)


p1=point(5,4)
p2=point(0,0)
print(p1.__add__(p2))
print(p1.__str__())
