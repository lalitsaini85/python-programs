t = (0,5,7,0,9,7,4,0)
f=[]
for i in t:
	if t.count(i)>=2 and i not in f:
		print(i)
		f.append(i)

