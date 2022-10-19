Seconds = int(input("Enter amount of seconds: "))
Seconds = Seconds % (24 * 3600)
Days = Seconds / 86400
Hours =  Seconds / 3600
Minutes = Seconds / 60

print ("Days: ", Days)
print ("Hours: ", Hours)
print ("Minutes: ", Minutes)
print ("Seconds: ", Seconds)