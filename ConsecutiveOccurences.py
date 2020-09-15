#Python program to find the count of consecutive occurances in a string.
#In this program we took the length of the string first and that length is going to be the range in the for loop.
#Next we have added '#' to our string so that we do not get index out of range error and also we can get correct output as by adding '#' length of the string gets increased
# For each iteration we are checking the count and if previous string does'nt match with new string count stops incrementing and adds the count with a specified character.
# If it doesnot match then we get the count of present string c[i] with its character. Also count value changes to 1.So that our condition starts checking count of next character



c='AABCCA'
n=len(c)
c=c+'#'
count=1
length=''
for i in range(n):
    if c[i]==c[i+1]:
        count=count+1
    else:
        length=length+str(count)+c[i]
        count=1
print(length)

