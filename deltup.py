t=[(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
b=[]
for i in t:
	if len(i)!=0:
		b.append(i)	
print(b)
