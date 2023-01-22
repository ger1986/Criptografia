# sabemos que la clave fija en código es A1EF2ABFE2BAEEFF (codificación hexadecimal) --> K1
# sabemos también que la clave final F1BA12BA21AABB12 (hexadecimal) --> K
# por tanto, nos falta saber la clave de propiedades. --> K2

def xor_data(binary_data_1, binary_data_2):
    return bytes([b1 ^ b2 for b1, b2 in zip(binary_data_1, binary_data_2)])

# primero pasamos las claves a binario para poder realizar las operaciones XOR necesarias:
K = bytes.fromhex("F1BA12BA21AABB12")
K1 = bytes.fromhex("A1EF2ABFE2BAEEFF")

# teniendo en cuenta las propiedades de XOR, sabemos que K2 = K ^ K1: (resultado después de ejecutar el código: 50553805c31055ed)

K2 = xor_data(K,K1).hex()
print("La clave de propiedades dinámica es = "+ K2)

# en el 2o apartado del ejercicio sabemos que:
# La clave fija sigue siendo la misma: A1EF2ABFE2BAEEFF; la llamaremos ahora K11
# La clave dinámica ahora es B98A15BA31AEBB3F; la llamaremos ahora K22
# Como la clave fija final es el resultado de una disociación en las 2 partes expuestas, deberemos hacer la operación XOR de ambos: la llamaremos KK

# volvemos a pasar las claves que tenemos a binario primeramente:
K11 = bytes.fromhex("A1EF2ABFE2BAEEFF")
K22 = bytes.fromhex("B98A15BA31AEBB3F")

KK = xor_data(K11,K22).hex()   # el resultado, tras la ejecución es: 18653f05d31455c0
print("La clave final será: " + KK)