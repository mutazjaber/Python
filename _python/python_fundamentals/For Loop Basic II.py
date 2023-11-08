import random
def x(min="",max=""):
    if min =="" and max == "":
        print (round(random.random()*100))
    if max !="" and min =="" :
        print (round(random.random()*max))
    if min !="" and max== "":
        print(round(random.random()*(100-min)+min))
    if min!=""and max !="":
        print (round(random.random()*(max - min) -1 +min +1 ))


x(min=20,max=70)

# x(min=5)
# x(max)
# x(min,max)