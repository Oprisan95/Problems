# un program care sa imi dea data cand voi muri la 90 de ani
# You have x days, y weeks, and z months left
data = int (input ("Varsta actuala: "))
nr_ani_ramasi = 90 - data
zile_ramase = nr_ani_ramasi * 365
saptamani_ramase = nr_ani_ramasi * 52 
luni_ramase = nr_ani_ramasi * 12 
print (f"you have {zile_ramase} days, {saptamani_ramase} weeks, and {luni_ramase} months left.")
