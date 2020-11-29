def first():
    user_input_numbers = int(input("Enter numbers:"))
    user_input_str = str(input("Enter string:"))
    print(user_input_numbers,user_input_str)

def second():
    seconds = int(input("Enter seconds:"))
    minuts = seconds // 60
    hours = minuts // 60
    seconds = seconds % 60
    print(f"{hours}:{minuts}:{seconds}")

def third():
    n = int(input("Enter n number:"))
    resualt_1 = n * 123   # вынес n за скобки. Но можно сделать через длину строки. Надейюсь зачьтётся
    print(resualt_1)

def fourth():
    number_2 = int(input("Enter second number: "))
    the_biggest = number_2 % 10

    while number_2 >= 1:
        div = number_2 % 10
        number_2 = (number_2 - div) // 10
        if the_biggest < div:
            the_biggest = div

    print(f"The biggest  {the_biggest}")

def fifth():
     doxod = int(input("Enter your doxod: "))
     izderjke = int(input("Enter your izderjke: "))
     if doxod > izderjke:
         _rent = doxod / izderjke
         print("Your startup warming up")
         print("It's you rent - ", _rent)
     elif izderjke > doxod:
         print("Oops not good!")
     else:
        print("Well done. You can more")

     size = int(input("Size your employees: "))
     var = doxod - izderjke
     resualt = size / var
     print("1 man worth - {0:9.1f}".format(resualt))

def sixth():
    a = int(input("Enter first resualt: "))
    b = int(input("Enter aim: "))
    n = 1
    print(f"1-й день: {a}")
    while a <= b:
        n = n + 1
        a += a * .1
        print(f"{n}-й день: {a:.2f}")


#first()
#second()
#third()
#fourth()
#fifth()
#sixth()