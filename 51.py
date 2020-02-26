s=input()
sb=input()
c=0
fo i in range(0,len(s)-len(sb)):
	if sb==s[i:i+len(sb)]:
		c+=1
print(c)
