a = int(input())
b = int(input())
c = int(input())
d = b**2-4*a*c
print("d=",d)
if(d>=0):
	print("roots are exist")
	p = (-b+(d**1/2))/2*a
	q = (-b-(d**1/2))/2*a
	print(p,"and",q)
else:
	print("roots are not exist")	
