# Write Python code that asks a user for their temperature. If the temperature is 100.4 or more, print “you have a fever”.
# Else print “normal temperature”

temperatura = float (input ("Ce temperatura ai?"))
if temperatura > 100.4:
    print ("Ai temperatura! ")
else:
    print ("Temperatura ta este normala! ")

#Write Python code that asks a user how many degrees is it in the Building.
#  If the temperature is less than or equal to 70, print “feels chilly”.
#Else print “comfy”

grade = int (input ("Cate grade sunt in cladire?"))
if grade <= 70:
    print ("Este rece")
else:
    print ("Este o temperatura potrivita")