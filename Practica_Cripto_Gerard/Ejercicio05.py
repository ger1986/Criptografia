import hashlib

s = hashlib.sha3_256()

# Para ver que Hash se ha utilizado, tenemos la siguiente línea de código:
print(s.name)

# Y ahora generamos el Hash del texto que nos da el enunciado:
s.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía","UTF-8"))
print(s.hexdigest())

# Ahora utilizamos un SHA512, el cual nos genera un Hash con el doble de bytes.
m = hashlib.sha512()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía", "utf8"))
print(m.name)
print(m.digest().hex())

# Ahora generamos un SHA3 Keccak de 256 bits con el siguiente texto: “En KeepCoding aprendemos cómo protegernos con criptografía.”
# Comprobaremos también la propiedad de difusión (y el efecto avalancha correspondiente) ya que hemos añadido un punto final al texto en claro inicial.
m = hashlib.sha3_256()
m.update(bytes("En KeepCoding aprendemos cómo protegernos con criptografía.", "utf8"))
print("SHA3-256: " + m.digest().hex())