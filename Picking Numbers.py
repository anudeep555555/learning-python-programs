
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
#print(dicty)
print(max_num)
