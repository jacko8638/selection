Year = input("enter year")
LeapYear = False
if (mod(Year, 4) == 0):
	LeapYear = True
if (mod(Year,100) == 0):
	LeapYear = False
if (mod (Year,400) == 0):
	LeapYear = True
if LeapYear = True:
	print (, Year," is a leap year")
elif Leapyear = False:
	print (, Year," is not a leap year")
