# Code 1:
mylist=[1,2,2,3,3,4,5,6,6,7]
for x in range(len(mylist)):
    if((mylist.count(x)>1)): 
     print(x,'is duplicate')

