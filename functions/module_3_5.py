def get_multiplied_digits(number):
    string_number = str(number)
    first = int(string_number[0])
    if len(string_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(string_number[1:]))

print(get_multiplied_digits(40203))