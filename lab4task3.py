from string import punctuation
from string import whitespace
file=open('word.txt')
def traverse(f):
	word=[]
	total=0
	d=dict()
	for i in f:
		a=''
		for w in i.split():
			alpha=w
			total+=1
			dl=low(alpha)
			if dl not in d:
				d[dl]=1
			else:
				d[dl]+=1
			for k in alpha:
				l=low(k)
				p=punch(l)
				w=white(p)
				a=a+w
		if a!='':
			print(a)
	print(total)
	mosr_frequent(d)
	print(d)
def mosr_frequent(l):
	inverse=dict()
	for key in l:
		val=l[key]
		if val not in inverse:
			inverse[val]=[key]
		else:
			inverse[val].append(key)
	t=inverse.items()
	t=sorted( t, reverse=True)
	for i in range(20):
		print (t[i])

def low(a):
	return a.lower()
def punch(a):
	return a.strip(punctuation)
def white(a):
	return a.strip(whitespace)

traverse (file)
