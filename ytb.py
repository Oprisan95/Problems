
#Write Python code that asks a user how many Youtube videos they watch per day. The average video is 7 minutes. If the user enters 5 or more, print “you watch a lot of videos”.
#Else print “good job!”.
#Print the total number of minutes the user watches videos.



numar_video = int (input ("Cate video urmaresti pe YTB pe zi?"))
if numar_video >= 5:
    numar_video = numar_video * 7
    print ("Te uiti destul de mult pe YTB!")
else:
    print ("Buna treaba")