## check pallindrom
n = int(input())
s = 0
k = n
for n in range(n,0):
	s = s+n%10
	n = n/10 
if(s==k):
	print("is")	
