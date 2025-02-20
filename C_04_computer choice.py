import random

rps_list = ["rock","paper","scissor", "xxx"]

for item in range (0, 30):
    comp_choice = random.choice(rps_list[:-1])
    print(comp_choice, end="\t")
