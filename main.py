import random
points = {"computer": 0, "player": 0}
def odd_number(number):
    if number % 2 == 0:
        return False
    else:
        return True
while True:
    a = random.randint(10 ,90)
    if odd_number(a) == False:
        continue
    b = random.randint(10 ,90)
    if odd_number(b) == False:
        continue
    op = random.choice(("+","-"))
    if op == "+":
        c = (a+b)
        e = input(f"{a} + {b} =")
    elif op == "-":
        c = (a-b)
        e = input(f"{a} - {b} =")
    if str(c) == e:
        points["player"] += 1
        print("Ура. Вы правильно ответили!")
    elif str(c) != e:
        points["computer"] += 1
        print("Увы.Вы оказались не правы... Очки зачисляются компьютеру!")
    print(f'Счет!{points["player"]}:{points["computer"]}')





