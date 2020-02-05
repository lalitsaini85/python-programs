## perfect number
for n in range(1,101):
	s = 0
	for i in range(1,n):
		t = n%i
		if(t==0):
			s+=i
	if(s==n):
		print(n,"number is perfect")
					
