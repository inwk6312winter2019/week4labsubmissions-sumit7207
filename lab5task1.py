from math import sqrt
class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
	def dist(self,other):
		d=sqrt(((self.x-other.x)**2)+((self.y-other.y)**2))
		return d
p1=point(5,4)
p2=point(0,0)
print(p1.dist(p2))
