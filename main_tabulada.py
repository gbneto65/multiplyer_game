import random
import winsound
import time

tab = 3
min = 0
herz_correct = 3000
msec_correct = 300
herz_incorrect = 500
msec_incorrect = 1000

print(" Multiplizieren Spielen")

while True:
    print('\n' * 20)
    tab = random.randint(0, 10)
    rnd = random.randint(0, 10)
    true_resp = rnd * tab
    print('Was ist die korrekte Antwort?\n')
    resp = int(input(f"  {rnd} * {tab} = "))

    if resp == true_resp:
        min = min + .5
        winsound.Beep(herz_correct, msec_correct)
        print(f"{rnd} * {tab} =  {true_resp}")
        print(f"richtige Antwort - Du hast jetzt {min} Minuten Zeit, um MINECRAFT zu spielen ")
        time.sleep(2)  # Sleep for 1 seconds

    elif resp == 99:
        print("Bis Bald!")
        print(f"*** Du hast {min} Minuten gewonnen, um MINECRAFT zu spielen ****")
        break
    else:
        min = min - 1
        winsound.Beep(herz_incorrect, msec_incorrect)
        print(f'\nNein, das ist nicht richtig!\nDas Richtige ist: {rnd} * {tab} =  {true_resp}\n')
        print(f"Lieder du hast jetzt {min} Minuten Zeit, um MINECRAFT zu spielen")
