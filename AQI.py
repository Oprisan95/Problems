#Write Python code that asks a user what the AQI is today. If the user enters, 50 or less,
# print “Air Quality is Good”. Else print, “Air Quality is Moderate or Unhealthy”.

aqi = int (input ("Care este AQI azi?"))
if aqi <=50:
    print ("Calitatea aerului este buna!")
else:
    print ("Aerul este poluat!")