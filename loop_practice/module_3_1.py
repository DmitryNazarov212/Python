calls = 0
def count_calls():
    return calls
def string_info(my_string):
    global calls
    calls += 1
    return [len(my_string), my_string.upper(), my_string.lower()]
def is_contains(my_string, my_list):
    global calls
    calls += 1
    lower_list = [s.lower() for s in my_list]
   ## new_list = list(map(lambda x: x.lower(), my_list)) :D
    if my_string.lower() in lower_list:
        return True
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)