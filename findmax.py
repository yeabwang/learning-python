from utils import find_max

user_input = list(input("Enter numbers separated by comma: ").split(","))

print(f" Your max value is {find_max(user_input)}")