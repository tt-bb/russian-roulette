import random
import os
import sys

total_bullets = input("Please enter the number of chambers (default = 6): ")

if not total_bullets:
    total_bullets = 6

elif not total_bullets.isdigit():
    quit("Invalid number of chambers!")

killer_bullet = random.randint(1, int(total_bullets))

for x in range(1, int(total_bullets) + 1):
    input("Press <ENTER> to pull the trigger!")
    if x == killer_bullet:
        print("YOU'RE DEAD !!\nGame Over")
        start_again = input("Do you want to start again? (y/n):(default = yes))")
        if not (start_again and not (start_again.lower()[0] == "y")):
            os.execv(sys.executable, [sys.executable] + sys.argv)
        else:
            break
    print("You're LUCKY\n \n -----")
