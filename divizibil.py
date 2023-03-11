#Write Python code asks the user for a number. If the number is divisible by 5,
#print the number if it is divisible by 5. Else print the number is not divisible by 5.

n = int(input("Indroduceti un nr: "))
if n % 5 == 0:
    print (n)
else:
    print (f"Numarul {n} nu este divizibil cu 5")


