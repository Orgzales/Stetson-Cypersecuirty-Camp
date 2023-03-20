import sys
import random
import pickle
import os.path
import getpass
from Crypto import Random
from Crypto.Hash import SHA256
from Crypto.Cipher import AES

def decrypt(s_enc, key_hash):
    iv = s_enc[0:AES.block_size]
    s_enc = s_enc[AES.block_size:]
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    return cipher.decrypt(s_enc)

def encrypt(s, key_hash):
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key_hash, AES.MODE_CBC, iv)
    extra = len(s) % 16
    if extra > 0:
        s = s + (b' ' * (16 - extra))
    s_enc = iv + cipher.encrypt(s) # prepend IV
    return s_enc

# a dictionary is a "key-value" pair: like, word & definition

passwords = {}

def savePasswords(key_hash):
	with open("passwords.pkl", "wb") as f:
		pkldata = pickle.dumps(passwords)
		pklencrypted = encrypt(pkldata, key_hash)
		f.write(pklencrypted)

def newPassword():
	url = input("URL: ")
	username = input("Username: ")
	password = ""
	for i in range(16):
		ascii = random.randint(33, 126)
		password += chr(ascii)
	print(password)
	print()
	passwords[url] = (username, password)

def loadPasswords(key_hash):
	global passwords
	if os.path.exists("passwords.pkl"):
		with open("passwords.pkl", "rb") as f:
			pklencrypted = f.read()
			pkldata = decrypt(pklencrypted, key_hash)
			passwords = pickle.loads(pkldata)

def listPasswords():
	for url, usernamepass in passwords.items():
		print("-----------")
		print("URL: {}".format(url))
		print("username: {} |  password: {}".format(usernamepass[0], usernamepass[1]))
		print("------------")
		print()

password = getpass.getpass("Enter password: ")
sha256 = SHA256.new()
sha256.update(str.encode(password))
key_hash = sha256.digest()

loadPasswords(key_hash)

while True:
	print("PASSMAN")
	print("-------")
	print("1) List")
	print("2) New")
	print("3) Quit")

	choice = input(">>> ")

	if choice == "1":
		listPasswords()
	elif choice == "2":
		newPassword()
	elif choice == "3":
		savePasswords(key_hash)
		sys.exit()



