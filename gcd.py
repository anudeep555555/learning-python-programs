#num 1 should always be less than num 2 or use minumum number among the two instead of num1 in for loop

def gcd(num1,num2):
    hcf=1
    for i in range(1,num1):
        if num1%i==0 and num2%i==0:
            hcf=i
    return hcf
print(gcd(72,108))
