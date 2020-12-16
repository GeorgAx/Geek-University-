from sys import argv
import functools
from itertools import count,cycle
from functools import reduce
from time import sleep

# def schet(time,stavke,prem):                                              #1 - задание
#     res = (int(time) * int(stavke)) + int(prem)
#     return res
#first, second, third = argv[1:]
#print(f"You are wealthy: {schet(first,second,third)}")


# dd = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]                       #2 - задание
# dd1 = []
# def as1(z):
#     n = 0
#     while n != len(z):
#         n += 1
#         if z[n] < z[n+1]:
#             p = z[n+1]
#             dd1.append(p)
#             print(p)
#
# p = [dd[x] for x in range(1,len(dd)) if dd[x] > dd[x -1]]
# print(p)





# dd = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]                     #4 - задание
# generator = (x for x in dd if dd.count(x) == 1)
# lo =[el for el in generator]
# print(lo)



#skip = (print(x) for x in range(20,240) if x % 20 == 0 or x % 21 == 0)      #3 - задание

# def my_func(prev_el, el):                                                  #5 - задание
#     return prev_el + el
#skip = ( x * 1 for x in range(100,1000) if x % 2 == 0)
#print(reduce(my_func,skip))

# def iter():
#     count()
#     yield

# num, step1, kek = argv[1:]                                                    #6 - задание
# for el in count(int(num), int(step1)):
#     if el > int(num) + int(kek):
#         break
#     else:
#         print(el)
# progr_lang = [10,111,20, 32,]
# iter = cycle(progr_lang)
#
# for el in iter:
#     sleep(.7)
#     print(el, "Sleep")
#----------------






def fact(n):
    z = 0
    while z != n:
        z += 1

fact(5)
list2 = int()
# for el in fact(5):
#     print(el)
