# def Biggie_Size(list):
#     # array = []
#     for x in range(len(list)):
#         if list[x]>0 :
#             list[x]= "big"
#     return list
# print(Biggie_Size([-1, 3, 5, -5]))

# def count_positives(list):
#     count = 0 
#     for i in range (len(list)):
#         if list[i] > 0 :
#             count += 1 
#     list[len(list)-1]= count
#     # return list
#     print(list)
# count_positives(([1,6,-4,-2,-7,-2]))

# def sum_total(list):
#     sum =0
#     for i in range (len(list)):
#         sum +=list[i]
#     return sum
# print(sum_total([6,3,-2]))


# def average(list):
#     sum =0
#     avg=0
#     for i in range (len(list)):
#         sum += list[i]
#     avg =sum/len(list)
#     return avg
# print(average([1,2,3,4]))

# def length(list):
#     return len(list)
# print(length([37,2,1,-9]))



# def minimum(list): 
#     temp = list[0]
#     for i in range (len(list)-1):
#             if list[i]<temp:
#                 temp = list[i]
#     return temp            
# print (minimum([37,-2050,1,-99999,2,-10,2,2,2,2]))

# def Maximum(list): 
#     temp = list[0]
#     for i in range (len(list)-1):
#             if list[i]>temp:
#                 temp = list[i]
#     return temp            
# print (Maximum([37,-2050,1,-99999,2,-10,2,2,2,2]))

# def ultimateAnalysis(list):
#     dictionary={"sumTotal":sum_total(list),"average" :average(list), "minimum" : minimum (list), "maximum":Maximum (list), "length":length(list)}
#     return(dictionary)
# print(ultimateAnalysis([1,2,2,2,2,2,2,2]))


def reverseList(list):
    reversedList=[]
    for x in range(len(list)-1,-1,-1):
        reversedList.append(list[x])
    return reversedList
print(reverseList([37,2,1,-9]))