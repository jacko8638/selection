#gets ph
pH = int(input("Enter pH level: "))
#checks what ph means
if pH > -1 AND pH < 7 then
	print("pH is acidic")
elif pH == 7 then
	print("pH is neutral")
elif pH > 7 and pH < 15 then
	print("pH is basic")
else
	print("Error... enter a number from 0 to 14")

