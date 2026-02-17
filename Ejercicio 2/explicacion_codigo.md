# Explicación del código

Primero se crea una variable llamada numero que guarda lo que se escribe
en el teclado. input recibe texto, por eso se usa int para convertirlo a
número entero.

Lueg empieza el primer bloque:

Se copia el valor de numero dentro de otra variable llamada n, esto se
hace porque n va a cambiar durante el proceso y se necesita conservar el
valor original. Después se crea una cadena vacía llamada binario, ahí se
irán guardando los resultados.

El ciclo while n \> 0 significa que el proceso se repite mientras n sea
mayor a cero.

Dentro del ciclo, residuo = n % 2 calcula el residuo de dividir entre 2,
ese residuo siempre será 0 o 1, luego se convierte a texto con str y se
pega al inicio de la cadena binario. Se pone al inicio porque los
residuos salen al revés. Después n = n // 2 divide el número entre 2 y
elimina decimales. Ese nuevo valor vuelve a entrar al ciclo. Cuando n
llega a cero, el ciclo termina y se "imprime" el resultado guardado.

------------------------------------------------------------------------

El siguiente bloque empieza igual (OCTAL), se vuelve a asignar n =
numero para reiniciar el valor original, se crea otra cadena vacía
llamada octal.

El ciclo funciona igual pero ahora el residuo se calcula con n % 8 y la
división es n // 8. La explicación y lógica es "igual", solo cambia la
base de números. Cada residuo se coloca al inicio de la cadena hasta que
n llega a cero. Luego se imprime.

------------------------------------------------------------------------

El último bloque repite la misma estructura (HEXADECIMAL).

Otra vez n recibe numero y se crea hexadecimal como cadena vacía. El
ciclo divide entre 16 y obtiene el residuo con n % 16. Aquí aparece una
condición. Si el residuo vale del 10 al 15 no se puede escribir
directamente porque en esa base 16 esos valores se representan con
letras a partir del 10 y por eso se revisa cada caso con if y elif. Si
vale 10 se agrega A, si vale 11 se agrega B, y así hasta 15 que
corresponde a F. Si el residuo es menor que 10, entra en el else y
simplemente se convierte el número a texto y se agrega al inicio.
Después se actualiza n dividiéndolo entre 16 sin decimales. El ciclo
termina cuando n llega a cero y se imprime el resultado final
