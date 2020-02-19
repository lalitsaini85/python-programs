t=()
n = int(input())
for i in range(n):
	d=input()
	if d.isalpha():
		t+=(d,)
	else:
		t+=(eval(d),)
print(t)
if(n>3):
	print(t[3],t[-4])
else:
	print("element of tuple is less than required element")
