# programme which removes every third number in the list until it is empty 
list=[1,2,3,4,5,6,7,8,9]
print("Original list is ",list)
while len(list)>2:
   print("Number removed from the list is ",list[2])
   list.remove(list[2])
   if(len(list)>2):
     print("List of numbers left are",list)
 

