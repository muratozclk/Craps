import os
import random

print("""+ field +\n+ big six +\n+ big eight +\n+ place win +\n+ buy +\n+ lay +\n+ any 7 +\n+ any 11 +\n+ any craps +\n+ horn +\n+ hardway +\n+ come +\n+ dont come +\n+ pass line +\n+ dont pise line +\n""")
gain = 0
bet = str(input("Bahis giriniz : "))
miktar = int(input("Yatırılacak miktarı giriniz : "))

def field():
    global gain
    membrane1 = random.randint(1,6)
    membrane2 = random.randint(1,6)
    total = membrane1 + membrane2
    if total == 2:
        gain = miktar*2
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 3:
        gain = miktar
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 4:
        gain = miktar
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 9:
        gain = miktar
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 10:
        gain = miktar
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 11:
        gain = miktar
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    elif total == 12:
        gain = miktar*2
        print("{} lira kazandınız.Tebrikler :)".format(gain))
    else:
        print("Kaybettiniz.")

def big_six():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2

        if total == 6:
            number = 6

        if total == 7:
            if number == 6:
                print("{} lira kazandınız.Tebrikler :)".format(miktar*6))
                break
            else:
                print("Kaybettiniz.")
                break

def big_eight():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2

        if total == 8:
            number = 8

        if total == 7:
            if number == 8:
                print("{} lira kazandınız.Tebrikler :)".format(miktar*8))
                break
            else:
                print("Kaybettiniz.")
                break

def place_win():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2

        if total == 4:
            number = 4
        elif total == 5:
            number = 5
        elif total == 6:
            number == 6
        elif total == 8:
            number = 8
        elif total == 9:
            number = 9
        elif total == 10:
            number = 10

        if total == 7:
            if number == 4:
                print("{} lira kazandınız.Tebrikler :)".format(miktar*1.8))
                break
            elif number == 10:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 1.8))
                break
            elif number == 5:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 1.4))
                break
            elif number == 9:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 1.4))
                break
            elif number == 6:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 1.16))
                break
            elif number == 8:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 1.16))
                break
            else:
                print("Kaybettiniz.")
                break

def buy():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2

        if total == 4:
            number = 4
        elif total == 5:
            number == 5
        elif total == 6:
            number == 6
        elif total == 8:
            number = 8
        elif total == 9:
            number = 9
        elif total == 10:
            number = 10

        if total == 7:
            if number == 4:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.85))
                break
            elif number == 10:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.85))
                break
            elif number == 5:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.38))
                break
            elif number == 9:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.38))
                break
            elif number == 6:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.09))
                break
            elif number == 8:
                print("{} lira kazandınız.Tebrikler :)".format((miktar-(miktar*0.05))* 1.09))
                break
            else:
                print("Kaybettiniz.")
                break

def lay():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2
        print(total)
        if total == 7:
            number = 7
        if total == 4:
            if number ==7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar-(miktar*0.05)*1.85))
                break


        elif total == 10:
            if number == 7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar - (miktar * 0.05) * 1.85))
                break


        elif total == 5:
            if number == 7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar - (miktar * 0.05) * 1.63))
                break


        elif total == 9:
            if number == 7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar - (miktar * 0.05) * 1.63))
                break


        elif total == 6:
            if number == 7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar - (miktar * 0.05) * 1.31))
                break


        elif total == 8:
            if number == 7:
                print("{} lira kazandınız.Tebrikler :)".format(miktar - (miktar * 0.05) * 1.31))
                break



if bet == "field":
    field()
elif bet == "big six":
    big_six()
elif bet == "big eight":
    big_eight()
elif bet == "place win":
    place_win()
elif bet == "buy":
    buy()
elif bet == "lay":
    lay()