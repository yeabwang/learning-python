# pound to kg == 1 lb = 0.4 kg
# kg to pound == 1 kg == 2.2 lbs

def main():
    weight = float(input("Weight: "))
    unit = input("(L)bs or (K)g: ").lower()
    
    if(unit == 'l'):
        lbtokh(weight)
    elif (unit == 'k'):
        kgtolb(weight)
    else:
        print("Wrong measurement.")
        
def lbtokh(weight):
    print(f"You are {weight*0.453} kilos")
def kgtolb(weight):
    print(f"You are {weight/0.45} pounds")
    
main()