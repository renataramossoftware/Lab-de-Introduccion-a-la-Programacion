def ejercicio_1():
    print("EJERCICIO 1")
    palabra = input("Escribe una palabra: ")
    for i in range(10):
        print(palabra)

def ejercicio_2():
    print("EJERCICIO 2")
    edad = int(input("Escribe tu edad: "))
    print("Has cumplido todos estos años: ")
    for año in range(1, edad + 1):
        print(año)

def ejercicio_3():
    print("EJERCICIO 3")
    numero = int(input("Escribe un número entero positivo: "))
    print("Todos los números impares desde 1 hasta tu número:", end=" ")
    for i in range(1, numero + 1):
        if i % 2!=0:
            print(i, end= ", ")

def ejercicio_4():
    print("EJERCICIO 4")
    num = int(input("Escribe un número entero positivo: "))
    for i in range(num, -1, -1):
        print(i, end=", ")

def ejercicio_5():
    print("EJERCICIO 5")
    cantidad = float(input("Ingresa una cantidad a invertir: "))
    interes = float(input("Interés anual (en porcentaje): "))
    años = int(input("Número de años: "))
    interes2 = interes / 100
    interes3 = cantidad * interes2 
    for año in range(1, años + 1):
        capital = cantidad + interes3

def ejercicio_6():
    print("EJERCICIO 6")
    altura = int(input("Ingresa un número entero: "))
    for i in range(1, altura+1):
        print("*" * i)

def ejercicio_7():
    print("EJERCICIO 7")
    for i in range(1, 11):
        for j in range(1, 11):
            print(i, "x", j, "=", i*j)
        print()

def ejercicio_8():
    print("EJERCICIO 8")
    n = int(input("Ingresa un número entero: "))
    for x in range(1, n+1):
        imparm = 2 * x - 1
        for num in range(imparm, 0, -2):
            print(num, end=" ")
            print()

def ejercicio_9():
    print("EJERCICIO 9")
    contrasena = "contraseña"
    while True:
        contrasena_pot = str(input("Contraseña: "))
        if contrasena_pot == contrasena:
            print("Contraseña correcta")
            break
        else:
            print("Contraseña incorrecta, intente de nuevo")

def ejercicio_10():
    print("EJERCICIO 10")
    num10 = int(input("Introduce un número: "))
    if num10 > 1:
     for i in range(2, num10):
        if num10 % i == 0:
            print("No es primo")
            break
    else:
        print("Es primo")

def ejercicio_11():
    print("EJERCICIO 11")
    palabra = input("Ingresa una palabra: ")
    largo = len(palabra)
    ind = largo - 1
    while ind >= 0:
        print(palabra[ind])
        ind = ind - 1

def ejercicio_12():
    print("EJERCICIO 12")
    frase = str(input("Frase: "))
    letra = str(input("Letra: "))
    cuenta = 0
    for V in frase:
        if V == letra:
         cuenta += 1
    print("La letra", letra, "aparece", cuenta, "veces en la frase")

def ejercicio_13():
    print("EJERCICIO 13")
    while True:
        palabra = str(input("Introduce algún texto (escribe -salir- para terminar): "))
        if palabra == "salir":
            print("Saliendo...")
            break
        else:
            print(palabra)



while True:
            print("\n --- MENÚ DE EJERCICIOS DISPONIBLES ---")
            print("1. Repetir palabra 10 veces")
            print("2. Tus años cumplidos hasta ahorita")
            print("3. Números impares desde 1 hasta tu número")
            print("4. Cuenta hacia atrás hasta 0")
            print("5. Calculadora de inversiones")
            print("6. Triángulo de asteriscos")
            print("7. Tabla de multiplicar")
            print("8. Triángulo de números impares")
            print("9. Contraseña correcta")
            print("10. ¿Es un número primo o no?")
            print("11. Letras de la palabra")
            print("12. Contador de veces que aparece letra en frase")
            print("13. Eco de lo escrito")
            
            seleccion = input("Selecciona el número del ejercicio: ")

            match seleccion:
                case "1":
                    ejercicio_1()
                case "2":
                    ejercicio_2()
                case "3":
                    ejercicio_3()
                case "4":
                    ejercicio_4()
                case "5":
                    ejercicio_5()
                case "6":
                    ejercicio_6()
                case "7":
                    ejercicio_7()
                case "8":
                    ejercicio_8()
                case "9":
                    ejercicio_9()
                case "10":
                    ejercicio_10()
                case "11":
                    ejercicio_11()
                case "12":
                    ejercicio_12()
                case "13":
                    ejercicio_13()