from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256
import os

my_path = os.path.abspath(os.getcwd())
pubKey = my_path + "/clave-rsa-oaep-publ.pem"
keyPair = my_path + "/clave-rsa-oaep-priv.pem"

key = RSA.importKey(open(keyPair).read())
msg = bytes('El equipo está preparado para seguir con el proceso','utf8')
hash = SHA256.new(msg)
signer = PKCS115_SigScheme(key)
signature = signer.sign(hash)
print(signature)
# Imprimimos la clave en hexadecimal
print("Firma:", signature.hex())