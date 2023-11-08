
# def countDown(n):
#     for x in range (n,-1,-1) :
#         print(x)
# countDown(5)

# def print_and_return(n1,n2) :
#     print(n1)
#     return n2
# print(print_and_return(1,2))


# def first_plus_length(list):
#     x=(list[0]+len(list))
#     print(x)
# first_plus_length([1,2,3,4,5])


# arr=[]
# def greater_than_secound(arrayy):
#     for x in range (0, len(arrayy) ,1):
#         if arrayy[x]> arrayy[1] and len(arrayy)>2:
#             arr.append(arrayy[x])
#         elif len(arrayy) < 3 :
#             return False
#     y= len(arr)
#     print(y)
#     return arr
# print(greater_than_secound([5,2,3,2,1,4]))


def length_and_value(size,value):
    list = []
    for i in range(size):
        list.append(value)
    return list
print(length_and_value(6,2))


