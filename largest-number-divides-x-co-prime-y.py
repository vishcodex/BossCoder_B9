# Given two positive numbers x and y. Find the maximum valued integer a such that: 
 

# a divides x i.e. x % a = 0
# a and y are co-prime i.e. gcd(a, y) = 1

# Python3 code to find the
# Largest Coprime Divisor

# Recursive function to return
# gcd of a and b
def gcd (a, b):
    if b == 0:
        return a
    else:  
	    return gcd(b, a % b)

# function to find largest
# coprime divisor
def cpFact(x, y):
	while gcd(x, y) != 1:
		x = x / gcd(x, y)
	return int(x)
	
# divisor code
x = 15
y = 3
print(cpFact(x, y))
