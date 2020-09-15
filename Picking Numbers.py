#Actually in so many solutions online counter function is used.So I implemented counter function from scratch so that I can understand how it exactly works.
#I created a dictionary starting from 0 to 100
#Next I incremented count of every value in the list to the value of dictionary.
#Finally I got a dictionary count for all 100 numbers
#Now Lets start the solution
#Now i started a for loop of range 99 because if i go till 100 we will get out of range error because it goes to 101 element which is not present in our dictionary
#As we can see the count of the continuation of two numbers will be our expected output . It may be count of number plus next number or number plus previous number.
# I updated the value of max_num so that for every iteration it finds sum of present index number and next index number and updates it if it finds higher value
# The higher value we got is our final answer
##


def pickingNumbers(a):
    # Write your code here
    dicty={}
    max_num=0
    for i in range(100):
        if i in dicty:
            dicty[i]+=1
        else:
            dicty[i]=0
    for i in range(len(a)):
        if a[i] in dicty:
            dicty[a[i]]+=1
    for i in range(len(dicty)-1):
        max_num=max(max_num,dicty[i]+dicty[i+1])
    return max_num
    
