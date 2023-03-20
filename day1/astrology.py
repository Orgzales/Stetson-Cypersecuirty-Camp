print ("Now i will give you your horo")
month = int(input("what month were you born? 1-12: "))
day = int(input("what day were you born? 1-31: "))

if month == 3 and day >= 21 or month == 4 and day <= 19:
        sign = "Aries"
if month == 4 and day >= 20 or month == 5 and day <= 20:
        sign = "Taurus"
if month == 5 and day >= 21 or month == 6 and day <= 20:
        sign = "Gemini"
if month == 6 and day >= 21 or month == 7 and day <= 22:
        sign = "Cancer"
if month == 7 and day >= 23 or month == 8 and day <= 22:
        sign = "Leo"
if month == 8 and day >= 23 or month == 9 and day <= 22:
        sign = "Virgo"
if month == 9 and day >= 23 or month == 10 and day <= 22:
        sign = "Libra"
if month == 10 and day >= 23 or month == 11 and day <= 21:
        sign = "SCorpio"
if month == 11 and day >= 22 or month == 12 and day <= 21:
        sign = "Sagittarius"
if month == 12 and day >= 22 or month == 1 and day <= 19:
        sign = "Capricorn"
if month == 1 and day >= 20 or month == 2 and day <= 18:
        sign = "Aquarius"
if month == 2 and day >= 19 or month == 3 and day <= 20:
        sign = "Pisces"
else:
	sign = "fuck if i know"
print ("your sign is {}".format(sign))
