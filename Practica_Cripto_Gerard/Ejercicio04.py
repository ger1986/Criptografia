import jwt

# Clave: Con KeepCoding aprendemos

encoded_jwt = jwt.encode({"usuario":"Don Miguel Feroz","rol":"isNormal","iat":1667933533}, "Con KeepCoding aprendemos", algorithm="HS256")
encoded_jwt_hackeado = jwt.encode({"usuario": "Don Miguel Feroz", "rol": "isAdmin", "iat": 1667933533}, "Con KeepCoding aprendemos", algorithm="HS256") #El segundo KeepCoding es el secreto para generar la firma ZZZ
print("Codigo normal: " + encoded_jwt)
print("Codigo modificado: " + encoded_jwt_hackeado)

#Vamos a suponer 3 casos distintos:
# 1) Verificación del propio servidor de autenticación (o delegado) es correcto
decode_jwt = jwt.decode(encoded_jwt,"Con KeepCoding aprendemos", algorithms="HS256")
# 2) Verificación correcta con el "cuerpo" o "Payload" cambiado, suponiendo que el hacker hubiera interceptado la contraseña:
decode_jwt_hackeado_con_contrasenya = jwt.decode(encoded_jwt_hackeado,"Con KeepCoding aprendemos", algorithms="HS256")
# 3) Verificación INcorrecta suponiendo que el hacker no tenga la contraseña (este sería el supuesto habitual en caso de que alguien intentara cambiarnos algo):
decode_jwt_hackeado_sin_contrasenya = jwt.decode(encoded_jwt_hackeado,"123456", algorithms="HS256")

print(decode_jwt)
print("*********************************")
print(decode_jwt_hackeado_con_contrasenya)
print("*********************************")
print(decode_jwt_hackeado_sin_contrasenya)