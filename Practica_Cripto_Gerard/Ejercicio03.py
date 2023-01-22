from Crypto.Cipher import ChaCha20
from Crypto.Cipher import ChaCha20_Poly1305
from base64 import b64decode, b64encode
from Crypto.Random import get_random_bytes
import json

# Texto Plano: Este curso es de lo mejor que podemos encontrar en el mercado (UTF8)
# Clave: FF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120 (hexadecimal)
# Nonce: 9Yccn/f5nJJhAt2S (base64)

# Pasamos los datos de entrada que tenemos a binario para poder realizar el cifrado correspondiente:
textoPlano_bytes = bytes('Este curso es de lo mejor que podemos encontrar en el mercado', 'UTF-8')
clave = bytes.fromhex('FF9DF30474898787A45605CCB9B936D33B780D03CABC81719D52383480DC3120')
nonce_mensaje = b64decode('9Yccn/f5nJJhAt2S')
print('nonce  = ', nonce_mensaje.hex())


# Usamos el código siguiente para cifrar los datos de entrada que tenemos ya pasados a binario.
# **** CIFRADO CHACHA20 ****
cipher = ChaCha20.new(key=clave, nonce=nonce_mensaje)
texto_cifrado_bytes = cipher.encrypt(textoPlano_bytes)
print('Mensaje cifrado en HEX = ', texto_cifrado_bytes.hex() )
print('Mensaje cifrado en B64 = ', b64encode(texto_cifrado_bytes).decode())
texto_cifrado_hex = texto_cifrado_bytes.hex()

print("*********************************")
# Para mejorar el sistema, podemos implementar el **** CHACHA20-Poly1305 (que incluye el tag) **** y no dejar el nonce fijo, como en el caso anterior.

# Primeramente generamos un nonce aleatorio
nonce_mensaje1 = get_random_bytes(12)

# Y procedemos al cifrado correspondiente:
datos_asociados = bytes('Datos no cifrados sólo autenticados', 'utf-8')
cipher = ChaCha20_Poly1305.new(key=clave, nonce=nonce_mensaje1)
cipher.update(datos_asociados)
texto_cifrado, tag = cipher.encrypt_and_digest(textoPlano_bytes)
mensaje_enviado = { "nonce": b64encode(nonce_mensaje).decode(),"datos asociados": b64encode(datos_asociados).decode(), "texto cifrado": b64encode(texto_cifrado).decode(), "tag": b64encode(tag).decode()}
json_mensaje = json.dumps(mensaje_enviado)
print("Mensaje: ", json_mensaje)

    
