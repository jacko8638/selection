#gets year
Year = input("enter year")
#defines variable
LeapYear = False
#chack is it is a leap year
if (mod(Year, 4) == 0):
	LeapYear = True
if (mod(Year,100) == 0):
	LeapYear = False
if (mod (Year,400) == 0):
	LeapYear = True
#checks result and prints it
if LeapYear = True:
	print (, Year," is a leap year")
elif Leapyear = False:
	print (, Year," is not a leap year")
