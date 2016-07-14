import random

print("""+ field +\n+ big six +\n+ big eight +\n+ place win +\n+ buy +\n+ lay +\n+ any 7 +\n+ any 11 +\n+ any craps +\n+ horn +\n+ hardway +\n+ come +\n+ dont come +\n+ pass line +\n+ dont pass line +\n""")
gain = 0
bet = str(input("Bahis giriniz : "))
miktar = int(input("Yatırılacak miktarı giriniz : "))

def field():
    global gain
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

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
        print("Zarların toplamı : {}".format(total))

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
        print("Zarların toplamı : {}".format(total))

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
        print("Zarların toplamı : {}".format(total))

        if total == 4:
            number = 4
        elif total == 5:
            number = 5
        elif total == 6:
            number = 6
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
        print("Zarların toplamı : {}".format(total))

        if total == 4:
            number = 4
        elif total == 5:
            number = 5
        elif total == 6:
            number = 6
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
        print("Zarların toplamı : {}".format(total))

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

def any_seven():
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 7:
        print("{} lira kazandınız. Tebrikler :)".format(miktar*4))
    else:
        print("Kaybettiniz.")

def any_eleven():
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 11:
        print("{} lira kazandınız. Tebrikler :)".format(miktar * 15))
    else:
        print("Kaybettiniz.")

def any_craps():
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 2:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*7))
    elif total == 3:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*7))
    elif total == 12:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*7))
    else:
        print("Kaybettiniz.")

def horn():
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 2:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*30))
    elif total == 12:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*30))
    elif total == 3:
        print("{} lira kazandınız.Tebrikler :)".format(miktar * 15))
    elif total == 11:
        print("{} lira kazandınız.Tebrikler :)".format(miktar * 15))
    else:
        print("Kaybettiniz.")

def hardway():
    number = 0
    while True:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2
        print("1.Zar : {}  2.zar : {}".format(membrane1,membrane2))

        if membrane1 == 2 and membrane2 == 2:
            number = 4
        elif membrane1 == 3 and membrane2 == 3:
            number = 6
        elif membrane1 == 4 and membrane2 == 4:
            number = 8
        elif membrane1 == 5 and membrane2 == 5:
            number = 10

        if total == 7:
            if number == 4:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 7))
                break
            elif number == 10:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 7))
                break
            elif number == 6:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 9))
                break
            elif number == 8:
                print("{} lira kazandınız.Tebrikler :)".format(miktar * 9))
                break
            else:
                print("Kaybettiniz.")
                break

def come():
    number = 0
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 7 or total == 11:
        print("{} lira kazandınız.Tebrikler :)".format(miktar*10))
    elif total == 2 or total == 3 or total == 12:
        print("Kaybettiniz.")
    else:
        number = total
        number2 = 0
        while True:
            membrane1 = random.randint(1, 6)
            membrane2 = random.randint(1, 6)
            total = membrane1 + membrane2
            print("Zarların toplamı : {}".format(total))
            if total == number:
                number2 = number
            if total == 7:
                if number2 == number:
                    print("{} lira kazandınız.Tebrikler :)".format(miktar))
                    break
                else:
                    print("Kaybettiniz.")
                    break

def dont_come():
    number = 0
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 3 or total == 12:
        print("{} lira kazandınız.Tebrikler :)".format(miktar * 10))
    elif total == 7 or total == 11:
        print("Kaybettiniz.")
    elif total == 2:
        print("Berabere bitti.Para iadesi...")
    else:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2
        print("Zarların toplamı : {}".format(total))

        if total == 7:
            print("{} lira kazandınız.Tebrikler :)".format(miktar))
        else:
            print("Kaybettiniz.")

def pass_line():
    number = 0
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 7 or total == 11:
        print("{} lira kazandınız.Tebrikler :)".format(miktar * 10))
    elif total == 2 or total == 3 or total == 12:
        print("Kaybettiniz.")
    else:
        number = total
        number2 = 0
        while True:
            membrane1 = random.randint(1, 6)
            membrane2 = random.randint(1, 6)
            total = membrane1 + membrane2
            print("Zarların toplamı : {}".format(total))
            if total == number:
                number2 = number
            if total == 7:
                if number2 == number:
                    print("{} lira kazandınız.Tebrikler :)".format(miktar))
                    break
                else:
                    print("Kaybettiniz.")
                    break

def dont_passline():
    number = 0
    membrane1 = random.randint(1, 6)
    membrane2 = random.randint(1, 6)
    total = membrane1 + membrane2
    print("Zarların toplamı : {}".format(total))

    if total == 3 or total == 12:
        print("{} lira kazandınız.Tebrikler :)".format(miktar * 10))
    elif total == 7 or total == 11:
        print("Kaybettiniz.")
    elif total == 2:
        print("Berabere bitti.Para iadesi...")
    else:
        membrane1 = random.randint(1, 6)
        membrane2 = random.randint(1, 6)
        total = membrane1 + membrane2
        print("Zarların toplamı : {}".format(total))

        if total == 7:
            print("{} lira kazandınız.Tebrikler :)".format(miktar))
        else:
            print("Kaybettiniz.")

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
elif bet == "any 7":
    any_seven()
elif bet == "any 11":
    any_eleven()
elif bet == "any craps":
    any_craps()
elif bet == "horn":
    horn()
elif bet == "hardway":
    hardway()
elif bet == "come":
    come()
elif bet == "dont come":
    dont_come()
elif bet == "pass line":
    pass_line()
elif bet == "dont pass line":
    dont_passline()
