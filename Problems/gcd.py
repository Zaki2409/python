
def hcfnaive(a, b):
	if b == 0:
		return abs(a)
	else:
		return hcfnaive(b, a % b)

 
print("The gcd of a and b is : ", end="")
print(hcfnaive( 10 , 38))
