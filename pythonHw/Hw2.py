
a = ["adf", 0, 2, 1, 3.2, "@"]
b = ("kek", "pek", "coopek")
#pp = list(input("Enter something what you want without space: "))
some_list = [7, 5, 3, 3, 2]

def type_in_list(e_list):
    l = list()
    print(e_list)
    for x in e_list:
        l.append(type(x))
    print(l)

def change_index(shuffel_list,i = 0):
    """ 'change_list' list it's list which we wanna to change.  'i' it's start element from list """

    if len(shuffel_list) == 0 or len(shuffel_list) == 1:
        print("Need more objects in list")
    else:
        while i < len(shuffel_list):
            save = shuffel_list[i]
            if len(shuffel_list) % 2 and save == shuffel_list[-1]:
                print(shuffel_list)
                break

            shuffel_list[i] = shuffel_list[i + 1]
            shuffel_list[i + 1] = save
            i += 2

def months():
    n = 0
    lisq2 = []
    q = int(input("Enter month: "))
    while len(lisq2) <= 11:
        s = ("Winter", "Autumn", "Summer", "Spring")
        lisq2.append(s[n])
        if lisq2.count(s[n]) == 3:
            n += 1
    lisq2.pop(1)
    lisq2.append(s[0])

    print(lisq2[q - 1])


word = input("Enter a word: ")
awas = word.split()
for x in enumerate(awas):
    if len(x[1]) >= 10:
        z = list(x[1])
        x = ''.join(z[0:10])
    print(x)


def for_lazzy_guy_fuuuu():
    some_list.append(int(input()))
    some_list.sort()
    some_list.reverse()
    print(some_list)


def for_lazzy_girl():
    i = 0
    entered = int(input())
    while some_list[i] > entered:
        i += 1
    some_list.insert(i,entered)
    print(some_list)

#type_in_list(a)
#change_index(pp)
#months()
#for_lazzy_guy_fuuuu()
#for_lazzy_girl()