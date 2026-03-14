

"""
if num in L:
    print("Your number is in the list")

else:
    print("Your number is not in the list")
"""

#Linear Search
#=============

L = [1,3,68,145,4,698,1000,0]
num = int(input("Pick a random number: "))

found = False
for i in range(len(L)):
    if L[i] == num:
        found = True

if found == True:
        print("Your number is in the list")
else:
        print("Your number is NOT in the list")


#Binary search
#=============

Sorted_L = [1,2,3,4,5,6,7,8,9,10]
num = int(input("Choose a random Number from 1-10: "))

start = 0
end = 9
found = False

while start <= end:
      mid = (start + end) // 2
      if num == Sorted_L[mid]:
            found = True
            break
      elif num < Sorted_L[mid]:
            end = mid - 1 
           
      elif num > Sorted_L[mid]:
            start = mid + 1
                         

if found == True:
    print("Your number is in the list")
    
else:
    print("Your number is NOT in the list")
            
            