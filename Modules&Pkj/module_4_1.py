# import fake_math as fake
# import true_math as tr

# result1 = fake.divide(69, 3)
# result2 = fake.divide(3, 0)
# result3 = tr.devide(49, 7)
# result4 = tr.devide(15, 0)

# print(result1)
# print(result2)
# print(result3)
# print(result4)
from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69, 3)
result2 = fake_divide(3, 0)
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)

print(result1)
print(result2)
print(result3)
print(result4)