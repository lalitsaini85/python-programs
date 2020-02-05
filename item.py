l = []
while 1:
	item=input('enter the item: ')
	l.append(item)
	if item==' ': 
		n=input('do you want to continue y/n:')
		if n.lower()=='n':
			break
print(l)
l.sort(reverse=True,key=len)
print(l)


