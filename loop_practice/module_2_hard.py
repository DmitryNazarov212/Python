from random import random, randrange

rand_number = randrange(3, 20)
password = []
cell_counter = 0
for i in range(1, rand_number):
    for j in range(i, rand_number):
        if  rand_number % (i + j) == 0 and i != j:
            password.append([])
            password[cell_counter].append(i)
            password[cell_counter].append(j)
            cell_counter += 1
print("Число на первом табло:", rand_number, "\nПароль к нему:", password)