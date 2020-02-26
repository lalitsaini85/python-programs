from math import sqrt
d=list(map(int,input().split(',')))
for i in d:
	c=50
	h=30
	q=sqrt((2*c*i)/h)
	print(int(q),end=",")	
