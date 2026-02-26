usuario_ok = "admin"
contrasena_ok = "Admin2026"

intentos = 0
login_correcto = False
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
        login_correcto = True
        
    elif usuario != usuario_ok or contrasena != contrasena_ok:
        print("Datos incorrectos.")
        intentos += 1

    if intentos == 3:
     print("Número máximo de intentos alcanzados.")
     break 


    while login_correcto == True:
     print("1. Clasificar número")
     print("2. Categoría de edad y permisos")
     print("3. Calcular tarifa final")
     print("4. Cerrar sesión")
     print("5. Salir")
     seleccion = input("Selecciona una opción: ")

     if seleccion == "1":
         numero = int(input("Escribe un número: "))
         type(numero) == int
         if numero == 0:
             print("El número es cero.")
         elif numero > 0:
             print("El número es positivo.")
         elif numero < 0:
             print("El número es negativo.") 
         if numero %2 == 0:
             print("El número es par.")
         elif numero == 0:
             print("El 0 no es par ni impar.")
         else:
             print("El número es impar") 

     elif seleccion == "2":
         edad = int(input("Escribe tu edad: "))
         type(edad) == int
         id_oficial = str(input("¿Cuenta con identificación oficial? (S/N): "))
         licencia = str(input("¿Cuenta con licencia para conducir? (S/N): "))
         if edad < 0 or edad > 120:
             print("Edad inválida.")
         if 0 <= edad <= 12:
             print("Estás en la niñez.")
         elif 13 <= edad <=17:
             print("Estás  en la adolescencia.")
         elif 18 <= edad <= 64:
             print("Estás en la adultez.")
         else:
             print("Eres un adulto mayor.")
         if edad >= 13:
             print("Puedes registrarte.")
         elif edad >= 18:
             print("Puedes comprar sin tutor")
         else: 
             print("Requieres un tutor para registrarte.") 
         if edad >= 18 and licencia == "S":
             print("Puedes conducir.")
         else:
             print("No puedes conducir.")
         if edad >= 21 and id_oficial == "S":
             print("Tienes acceso al servicio premium.")
         else: 
             print("No tienes acceso al servicio premium.")

 
     elif seleccion == "3":
         print("Calculando la tarifa final...")

     elif seleccion == "4":
         print("Cerrando sesión...")
         break
     elif seleccion == "5":
         break
    break
