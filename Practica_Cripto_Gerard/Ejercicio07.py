import hashlib

m = hashlib.sha1()
m.update(bytes("Hola2", "utf8"))
print("SHA1:   " + m.digest().hex())

print(len('e732a5960409d15345011e737b4c5b9e21768ff9'))  #20bytes