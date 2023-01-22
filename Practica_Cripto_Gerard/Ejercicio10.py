from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Hash import SHA256
import hashlib
import os

# Recuperamos primeramente la clave privada, que es con la que vamos a descifrar la clave.
my_path = os.path.abspath(os.getcwd())
path_file_priv = my_path + "/clave-rsa-oaep-priv.pem"

key_priv = RSA.importKey(open(path_file_priv).read())

msg = bytes.fromhex("7edee3ec0b808c440078d63ee65b17e85f0c1adbc0da1b7fa842f24fb06b332c156038062d9daa8ccfe83bace1dca475cfb7757f1f6446840044fe698a631fe882e1a6fc00a2de30025e9dcc76e74f9d9d721e9664a6319eaa59dc9011bfc624d2a63eb0e449ed4471ff06c9a303465d0a50ae0a8e5418a1d12e9392faaaf9d4046aa16e424ae1e26844bcf4abc4f8413961396f2ef9ffcd432928d428c2a23fb85b497d89190e3cfa496b6016cd32e816336cad7784989af89ff853a3acd796813eade65ca3a10bbf58c6215fdf26ce061d19b39670481d03b51bb0eecc926c9d6e9cb05ba56082a899f9aa72f94c158e56335c5594fcc7f8f301ac1e15a938")

# y procedemos a descifrar con el bloque de código siguiente, obtenido así la e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72
decryptor = PKCS1_OAEP.new(key_priv,SHA256)
decrypted = decryptor.decrypt(msg)
print('Descifrado:', decrypted.hex())


# Ahora procedemos a volver a cifrar la clave:

my_path = os.path.abspath(os.getcwd())
path_file_publ = my_path + "/clave-rsa-oaep-publ.pem"

#Clave publica del servidor (es decir el destino del mensaje)
key_publ = RSA.importKey(open(path_file_publ).read())

#Cifrado 
msg = bytes.fromhex("e2cff885901a5449e9c448ba5b948a8c4ee377152b3f1acfa0148fb3a426db72")
encryptor = PKCS1_OAEP.new(key_publ, SHA256)
encrypted = encryptor.encrypt(msg)

print("Cifrado:", encrypted.hex())




