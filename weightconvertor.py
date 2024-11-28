# pound to kg == 1 lb = 0.4 kg
# kg to pound == 1 kg == 2.2 lbs

weight = float(input("Weight: "))
unit = input("(L)bs or (K)g: ").lower()

if(unit == 'l'):
    print(f"You are {weight*0.453} kilos")
elif (unit == 'k'):
    print(f"You are {weight/0.45} pounds")
else:
    print("Wrong measurement.")