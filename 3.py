l=list(map(int,input().split(",")))
f=1
for i in l:
	while i!=1:
		f=f*i
		i=i-1
	print(f,end=",")
	f=1
		
