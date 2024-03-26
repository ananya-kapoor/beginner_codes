#Code to find the unique triplets whose three elements gives the sum zero
def find_triplets(input):
    print("input is ",input)
    input.sort()
    print("Input is sorted",input)
    triplets =set()
    for x in range(len(input)-2):
      if x>0 and input[x]==input[x-1]:
         # check for empty list and sorted is [-3,0,0,0,1,2,4,5,6,7,8]
         # len is 11-2 = 9 
         #checking is next number is not same as previous number
         print("checking number in first loop ",input[x]) 
         continue 
      
      checked_set= set()
      for y in range(x+1,len(input)):
          print("checking two numbers are ",input[x],input[y])
          sum = input[x]+ input[y]
       
          complement_num= -sum
          print("checking the third  number should be ",complement_num)
          if complement_num in checked_set:
             triplets.add((input[x],complement_num,input[y]))
             print(complement_num, "Number  found")
          else: 
             checked_set.add(nums[y])
             print("Number not found")
    return[list(z) for z in triplets]

#run 
nums=[1,2,4,-3,5,6,7,8,0,0,0]
result = find_triplets(nums)
print(result)

     
 
