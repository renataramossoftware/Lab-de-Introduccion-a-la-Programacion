usuario_ok = "admin"
contrasena_ok = "Admin2026"

intentos = 0
while intentos < 3:

    usuario = input("Ingresa tu usuario: ")
    contrasena = input("Ingresa tu contraseña: ")

    if usuario == "":
     print("Usuario inválido. No debe estar vacío")
     intentos += 1

    if " " in usuario:
       print("El usuario no debe tener espacios.")
       intentos += 1

    if len(contrasena) < 8:
        print("Contraseña inválida. Mínimo 8 caracteres.")
        intentos += 1

    tiene_letra = False
    tiene_numero = False
    for c in contrasena:
     codigo = ord(c)
     if (65 <= codigo <= 90) or (97 <= codigo <= 122):
        tiene_letra = True

     if 48 <= codigo <= 57:
            tiene_numero = True

    if not tiene_numero or not tiene_letra:
            print("La contraseña debe tener al menos 1 letra y 1 dígito.")
            intentos +=1

    if usuario == usuario_ok and contrasena == contrasena_ok:
        print("Bienvenido.")
        break
    else:
        print("Datos incorrectos.")
        intentos += 1
if intentos == 3:
    print("Número máximo de intentos alcanzados.")