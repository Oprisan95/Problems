#anul se divide la 4 se divide la 100 se divide la 400 = an bisect
an = 1996
if an % 4 == 0:
    if an % 100 == 0:
        if an % 400 == 0:
            print("Anul este bisect")
        else:
            print ("Anul nu este bisect")
    else:
        print ("Anul este bisect")
else:
    print ("Anul nu este bisect")
        