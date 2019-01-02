num1 = 42
num2 = 14
a=num1
b=num2

remains = 1

while remains > 0 :
    remains = a % b
    a = b
    b = remains
    
gcd = a

lcm = num1*num2/gcd

print(gcd)
print(lcm)