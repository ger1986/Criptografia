from Crypto.Hash import HMAC, SHA256


def getHMAC(key_bytes,data_bytes):
    hmac256 = HMAC.new(key_bytes, msg=data_bytes, digestmod=SHA256)
    return hmac256.hexdigest()

def validateHMAC(key_bytes,data_bytes,hmac):
    hmac256 = HMAC.new(key_bytes,msg=data_bytes,digestmod=SHA256)
    result = "KO"
    try:
        print("hmac en verificacion: " + hmac256.hexdigest())
        hmac256.hexverify(hmac)
        result = "OK"
    except ValueError:
        result = "KO"
    print("result: " + result)
    return result

# Introducimos los datos de entrada que nos da el enunciado, pasándolos a binario.
clave_bytes = bytes.fromhex('7212A51C997E14B4DF08D55967641B0677CA31E049E672A4B06861AA4D5826EB')
datos = bytes("Siempre existe más de una forma de hacerlo, y más de una solución válida.", "utf8")
# Y sacamos el hmac correspondiente:
hmac = getHMAC(clave_bytes,datos)

print(hmac) #915bf9fbe64f837a0dffbacba6b85a49758c829f2e2970d8471f600dfd250bdc

#cliente (móvil). Verificamos asumiendo que solo ambas partes tienen la clave compartida.
print(validateHMAC(clave_bytes, datos,hmac))