import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import jks
import os


# Vamos a sacar la clave directamente del Keystore utilizando las siguientes líneas de código:
path = os.path.dirname(__file__)
keystore = path + "/KeyStorePracticas"
ks = jks.KeyStore.load(keystore, "123456")
for alias, sk in ks.secret_keys.items():
    if sk.alias == "cifrado-sim-aes-256":
        clave = sk.key
print("La clave es:", clave.hex())
# Pasamos todos los datos de entrada a binario para poder realizar la operación de descifrado:
iv_desc_bytes = bytes.fromhex('00000000000000000000000000000000')
texto_cifrado_bytes = b64decode('zcFJxR1fzaBj+gVWFRAah1N2wv+G2P01ifrKejICaGpQkPnZMiexn3WXlGYX5WnNgpZs3h0N4jLXi2xlV02D1g==')


# Ejecutamos el código siguiente para descifrar el "texto_cifrado_bytes"
try:
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="pkcs7")
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print(mensaje_des_bytes.hex())

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error) 

# Obtenemos los siguientes resultados (en utf-8 y hexadecimal respectivamente):
# Esto es un cifrado en bloque típico. Recuerda el padding...
# 4573746f20657320756e206369667261646f20656e20626c6f7175652074c3ad7069636f2e20526563756572646120656c2070616464696e672e2e2e

print("*********************************")
# Vamos a probar de cambiar el padding --> de PKCS7 a x923:

try:
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = unpad(cipher.decrypt(texto_cifrado_bytes), AES.block_size, style="x923")
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print(mensaje_des_bytes.hex())

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error)
# Obtenemos error en el descifrado puesto que estamos intentando hacerlo con otro padding diferente al que se utilizó para cifrar.

print("*********************************")

# ahora vamos a quitar el padding, suprimiendo la parte del código en la que especificamos qué padding estamos usando:

try:
    cipher = AES.new(clave, AES.MODE_CBC, iv_desc_bytes)
    mensaje_des_bytes = cipher.decrypt(texto_cifrado_bytes)
    print("El texto en claro es: ", mensaje_des_bytes.decode("utf-8"))
    print(mensaje_des_bytes.hex())
    print("*********************************")

except (ValueError, KeyError) as error:
    print('Problemas para descifrar....')
    print("El motivo del error es: ", error)

