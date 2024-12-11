from utils import find_max as maxi

user_input = list(input("Enter numbers separated by comma: ").split(","))

print(f" Your max value is {maxi(user_input)}")