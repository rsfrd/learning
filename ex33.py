
def f(numbers):
    for i in range(0, 6): 
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i
        f(numbers)

numbers = f([])

for num in numbers:
    print num

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
# 
#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i
#  
# print "The numbers: "
#  
# for car in numbers:
#     print car 
#  
