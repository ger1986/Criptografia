from Crypto.Protocol.KDF import HKDF
from Crypto.Hash import SHA512

# El salt nos lo da el propio enunciado, representando que se ha obtenido de un identificador de dispositivo (lo pasamos a binario)
salt = bytes.fromhex("e43bb4067cbcfab3bec54437b84bef4623e345682d89de9948fbb0afedc461a3")
# La clave maestra la obtenemos del keystore, la que corresponde a la etiqueta cifrado-sim-aes-256 (lo pasamos a binario también)
master_secret = bytes.fromhex("E2CFF885901A5449E9C448BA5B948A8C4EE377152B3F1ACFA0148FB3A426DB72")
# Y aplicamos el algoritmo HKDF, generando una sola clave y utilizando el hash SHA512:
key1 = HKDF(master_secret, 32, salt, SHA512, 1) 

print("Clave: ", key1.hex())