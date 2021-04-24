import random
import winsound
tab = 3
min = 0
herz_correct = 3000
msec_correct = 300
herz_incorrect = 500
msec_incorrect = 1000

print("Multiples Game")

while True:
    tab = random.randint(0, 10)
    rnd = random.randint(0, 10)
    true_resp = rnd * tab
    resp = int(input(f"{rnd} * {tab} = "))

    if resp == true_resp:
        min = min + .5
        winsound.Beep(herz_correct,msec_correct)
        print( f"right Answer - You have now {min} minutes to play MINECRAFT")

    elif resp == 99:
        print("Bis Bald!")
        print(f"*** you won {min} minutes to play MINECRAFT ****")
        break
    else:
        min = min - 1
        winsound.Beep(herz_incorrect, msec_incorrect)
        print(f"Wrong Answer - You have now {min} minutes to play MINECRAFT")



