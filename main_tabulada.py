import random
tab = 3
min = 0
print("Multiples Game")

while True:
    tab = random.randint(0, 10)
    rnd = random.randint(0, 10)
    true_resp = rnd * tab
    resp = int(input(f"{rnd} * {tab} = "))

    if resp == true_resp:
        min = min + .5
        print( f"right Answer - You have now {min} minutes to play MINECRAFT")

    elif resp == 99:
        print("Bis Bald!")
        print(f"*** you won {min} minutes to play MINECRAFT ****")
        break
    else:
        min = min - 1
        print(f"Wrong Answer - You have now {min} minutes to play MINECRAFT")



