#I learned the concept of lcm and implemented the code on my own
#Change the range in for loop if needed

def lcm(num1,num2):
    lcm=num1*num2
    for i in range(1,1000):
        multi=num2*i
        if multi%num1==0:
            lcm=multi
            return lcm
print(lcm(49,42))
