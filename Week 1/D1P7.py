#Unit Converter
cunit=input("Enter the unit system your currently using (m,mm,cm,km): ")
length=float(input("Enter the length: "))
tunit=input("Enter the unit system in which you want to convert the length (m,mm,cm,km): ")
if cunit=="m" and tunit=="mm":
    print(length," meters is equal to ",length*1000," millimeters")
elif cunit=="m" and tunit=="cm":
    print(length," meters is equal to ",length*100," centimeters")
elif cunit=="m" and tunit=="km":
    print(length," meters is equal to ",length/1000," kilometers" )
elif cunit=="mm" and tunit=="m":
    print(length," millimeters is equal to ",length/1000," meters")
elif cunit=="mm" and tunit=="cm":
    print(length," millimeters is equal to ",length/10," centimeters" )
elif cunit=="mm" and tunit=="km":
    print(length," millimeters is equal to ",length/1000000," kilometers" )
elif cunit=="cm" and tunit=="mm":
    print(length," centimeters is equal to ",length*10," millimeters")
elif cunit=="cm" and tunit=="m":
    print(length," centimeters is equal to ",length/100," meters")
elif cunit=="cm" and tunit=="km":
    print(length," centimeters is equal to ",length/100000," kilometers")
elif cunit=="km" and tunit=="m":
    print(length," kilometers is equal to ",length*1000," meters")
elif cunit=="km" and tunit=="cm":
    print(length," kilometers is equal to ",length*100000," centimeters")
else:
    print(length," kilometers is equal to ",length*1000000," millimeters")