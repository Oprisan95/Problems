# angajata la o pizza, cat costa o pizza? stim ca 3 criterii : marime = small , medium , large
# pt small = pizza = 15 lei
# medium = pizza = 20 lei
# large = pizza = 25 de lei
#daca ptr pizza mica se adaga pepperoni + 2 lei
# daca se adauga ptr pizza medie si mare pepperoni + 3 lei
# extra cheese + 1leu pentru toate tipurile de pizza
s = 15
m = 20
l = 25

pizza = input ("Ce pizza doresti? ")
pepperoni = input ("Doresti pepperoni? ")
cheese = input ("Doresti cascaval? ")
if pizza == "s":
    pizza = 15
    print (f"Pizza  mica costa {pizza} lei")
    if pepperoni == "da":
        pizza = pizza + 2
    else:
        print (f"Nu doresc pepperoni si pizza costa {pizza} lei")
    if cheese == "da":
        pizza = pizza + 1
        print (f"Pizza costa {pizza}lei")
    else:
        print (f"Nu doresc cheese si pizza costa {pizza} lei")
elif pizza == "m":
    pizza = 20
    print (f"Pizza medie costa {pizza} lei")
    if pepperoni == "da":
        pizza = pizza + 2
        print (f"Pizza cu pepperoni costa {pizza} lei")
    else:
        print (f"Nu doresc pepperoni si pizza costa {pizza} lei")
    if cheese == "da":
        pizza = pizza + 1
        print (f"Pizza cu cascaval costa {pizza}lei")
    else:
        print (f"Nu doresc cheese si pizza costa {pizza} lei")
else:
    pizza = 25 
    print (f"Pizza mare costa {pizza} lei")
    if pepperoni == "da":
        pizza = pizza + 2
        print (f"Pizza  cu pepperoni costa {pizza}lei")
    else:
        print (f"Nu doresc pepperoni si pizza costa {pizza} lei")
    if cheese == "da":
        pizza = pizza + 1
        print (f"Pizza  cu cascaval costa {pizza}lei")
    else:
        print (f"Nu doresc cheese si pizza costa {pizza} lei")

