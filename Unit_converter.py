#Unit converter

##Volume


def GPM(unit,a):
    if unit.lower() == "gpm":
        print ("No conversion, same unit!")
    elif unit.lower() == "m3/hr":
        y = float(a)*1000/3.785/60
        print (str(y)+" "+"GPM")
    elif unit.lower() == "lph":
        y = float(a)/3.785/60
        print (str(y)+ " "+"GPM")
    elif unit.lower() == "lpm":
        y = float(a)/3.785
        print(str(y)+ " "+ "GPM")
    else:
        print ("Please check your unit entered.")

print ("Please enter value and unit with comma (,)")
x = input()
z = x.split(",")
unit = str(z[1])
number = float(z[0])

GPM (unit,number)
