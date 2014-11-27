
print("Now in module.py")

module='test'
def func(n):
	a,b=1,1
	while b<n:
		a,b=b,a+b
		print(b,end=' ')
	return b