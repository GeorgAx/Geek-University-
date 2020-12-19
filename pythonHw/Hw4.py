from time import sleep
from os import remove
from random import randint
from functools import reduce



# def summa(end_pos):
#     z = 0
#     while z != end_pos:
#         z += 1
#         yield z
#
#
# def preaper(arg):
#     preaper_arg = (x.split(" — ") for x in arg)
#     return preaper_arg
#
#
#
#
# def open_mine():
#     import os
#     file_name = input("Make file name: ")
#     test = open(file=file_name + ".txt", mode='w')
#     test.writelines(input())
#     test.close()
#
#     test = open(file_name + ".txt", "r")
#     content = test.readlines()
#     print(content)
#     test.close()
#     os.remove(file_name + '.txt')
#
# def open_yours():
#     file_obj = open(file="Ne_programmno.txt", mode="r")
#     test2 = file_obj.readlines()
#     n = 0
#     words = 0
#     for x in test2:
#         for y in x:
#             if y == '\n':
#                 n += 1
#             if y == ' ':
#                 words += 1
#     file_obj.close()
#     print(f"Строки - {n + 1}. \nСлова - {words}")

# translate_dict = {"One":"Один", "Two":"Два", "Three":"Три", "Four":"Четыре"}
#
# with open("Ne_programmno.txt") as file_object:
#     test2 = file_object.readlines()
#     out_txt = open("New.txt", "w")
#
#     preaper_list = [x for x in preaper(test2)]
#     out_list = []
#     for preaper_list_x in preaper_list:
#         for translate_dict_x in translate_dict:
#             for el in preaper_list_x:
#                 if el == translate_dict_x:
#                     index = preaper_list_x.index(el)
#                     preaper_list_x.pop(index)
#                     preaper_list_x.insert(index,translate_dict.get(el))
#
#         out_list.append(" — ".join(preaper_list_x))
#
#     out_txt.writelines(out_list)
#
#     out_txt.close()
#
#
#
#
# with open("text.txt", "w") as kek_obj:
#     x = [z for z in range(randint(2,20), randint(2,90))]
#     total = reduce(lambda acc, n: acc + n, x)
#     str_list = list(map(str, x))
#     out_list= " ".join(str_list)
#     content1 = kek_obj.write(out_list)
#     print(f"Summa = {total}")
#     #remove('text.txt')



with open("ed.txt", "r") as kek1_obj:
    """ Извините, не успел допасать, очень сложная задача для меня. Но она и интересна!! 
    Сейчас 19:44. Боюсь, просто, не успеть. Потом доделаю. и обязательно скину"""

    content2 = kek1_obj.readlines()
    list_num = []
    resualt = 0
    for separ_1 in content2:
        separ_1 = separ_1.split(" ")
        for separ_step2 in separ_1:
            p = list(filter(str.isdigit, separ_step2))
            for i in p:
                plek = reduce(lambda acc, n: acc+n, p)
                list_num.append(int(plek))
                resualt = reduce(lambda acc, n: acc + n, list_num)
                break

        print(list_num,resualt)



    print(list_num)















