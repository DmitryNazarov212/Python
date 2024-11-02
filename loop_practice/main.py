first = int(input())
second = int(input())
third = int(input())
if first == second and first == third:
    count = 3
elif first == second or first == third or second == third or second == first:
    count = 2
else :
    count = 0
print(count)
