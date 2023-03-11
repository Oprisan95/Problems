#Write Python code that asks a user do you have a ShopRite card? Next, ask how many Apple or Pumpkin pies do they want to buy.
#If the user enters “yes”, print "2.99 per pie". Else, print "4.99 per pie".
#Print the total price.



card = input ("Ai card ShopRide ")
placinta = int ( input (" Cate placinte cu mere sau cu dovleac doresti?"))
if card == "yes":
    placinta = placinta * 2.99
    print (f" O sa platesti {placinta} dolari pentru placinta cu mere sau cu dovleac!")
else:
    placinta = placinta *4.99
    print (f"O sa platesti {placinta} dolari pentru placinta cu mere sau cu dovleac!")