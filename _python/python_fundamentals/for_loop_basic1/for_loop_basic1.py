for x in range (151): 
    print(x)


for y in range (5,1000,5):
    print(y)


for x in range  (1,101,1):
    if x %10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0 :
        print("coding")
    else : print (x)

sum = 0 
for x in range (500000):
    if x%2 !=0:
        sum += x
print ("The sum of all odd numbers is",sum)

for x in range (2018,0,-4):
    print(x)

lowNum = 2
highNum =14 
mult =2

for num in range (lowNum,highNum +1, 1):
    if num % mult == 0 :
        print(num)
