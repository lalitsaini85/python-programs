t = ()
n = int(input())
for i in range(n):
	d = input()
	if d.isalpha():
		t+=(d,)
	else:
		t+=(eval(d),)
print(t)
x1,x2,x3,x4=t
print(x1,x2,x3,x4)
print(x2)
print(x3)
print(x4)
