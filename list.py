l = list(map(int,input("\nEnter the numbers : ").split(" ")))
print(l)
r = []
for i in l:
	if i not in r:
		r.append(i)

print(*r,sep="*")

