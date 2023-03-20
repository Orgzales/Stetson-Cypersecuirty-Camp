from Crypto.Hash import MD5, SHA, SHA256, SHA512

msg = input("Enter a message: ")

md5 = MD5.new()
md5.update(msg.encode())

print("     ")
print("-----")
print("     ")

print("MDS hash: {}".format(md5.hexdigest()))

print("     ")
print("-----")
print("     ")

sha512 = SHA512.new()
sha512.update(msg.encode())
print("SHA512 hash: {}".format(sha512.hexdigest()))

print("     ")
print("-----")
print("     ")
