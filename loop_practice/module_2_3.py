my_list = [42, 13, 322, 13, 0, -9, -5, 9, 8, 7, -6, 5]
i = 0
while i != len(my_list):
    if my_list[i] < 0:
        break
    if my_list[i]  == 0:
        i +=1
        continue
    print(my_list[i])
    i += 1