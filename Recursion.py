
#def mustafa():
#    for i in range(5):
#        print("mustafa")


#mustafa()

#Recursion function (Prints numbers in condensending order)
def mustafa(n):
    if n == 0:
        return
    else:
        mustafa(n-1)
        print(n)
        
mustafa(10)



#finding sum of 10 numbers
def sum(n):
    if n == 0:
        return 0
    else:
         return  n+sum(n-1)
    
    
result = sum(10)   
print(result)


#Finding product of 10 numbers
def product(n):
    if n == 1:
        return 1
    else:
        return n*product(n-1)
    
    
result = product(10)
print(result)


#Converting base10 number into binary






#Accept a string and accept if it is palindrome string
def pal(s):
    if s == "":
        return True 
    elif s[0] != s[-1]:
        return False
    else:
        return pal(s[1:-1])

print(pal("hey"))
    


