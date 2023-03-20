import random

n = random.randint(1,1000)

while True:
	guess = int( input("guess number: "))
	if guess != n and guess >= n:
		print("too high")
	if guess != n and guess <= n:
		print("too low")
	if guess == n:
		print("the number was {}".format(n))
		break
