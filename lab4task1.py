from string import punctuation
from string import whitespace
file=open('98-0.txt')
def traverse(f):
	word=[]
	for i in f:
		a=''
		for w in i.split():
			alpha=w
			for k in alpha:
				l=low(k)
				p=punch(l)
				w=white(p)
				a=a+w
		if a!='':
			print(a)
def low(a):
	return a.lower()
def punch(a):
	return a.strip(punctuation)
def white(a):
	return a.strip(whitespace)

traverse (file)
