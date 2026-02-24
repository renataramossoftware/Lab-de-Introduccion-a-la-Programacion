## Explicación del código

El código inicia definiendo quién es el usuario correcto para el login y
cuál es la contraseña correcta (para lo mismo, que se efectúe
correctamente el login). Luego se definen los intentos actuales y se
abre un while, aquí se ejecuta primero el input para pedirle información
al usuario y que pueda ingresar las credenciales, luego va la primera
condicional, el if, aquí si el usuario no pone nada en esa parte no es
válido según los requerimientos del ejercicio así que es inválido y
cuenta como un intento. El segundo if es porque no debe contener
espacios el usuario y de igual manera aumenta un intento, el tercero es
la longitud de la contraseña que tiene que ser \>8 o sea que mínimo debe
tener 8 caracteres y luego se ponen variables "tiene_letra" y
"tiene_numero" para ver que la contraseña tenga ambas cosas ya que así
lo piden. Se usa el for c y se utilizan "los codigos" o no sé cómo se
llaman exactamente pero esa seria de caracteres ASCII que definen si
tiene letra o numero. Ya ahí se valida y si no tiene uno de ellos lanza
el error y cuenta como un intento más. Si las credenciales son las
correctas (admin y Admin2026) entonces se va a imprimir Bienvenido. Si
esto no pasa serán datos incorrectos y aumentará un intento. Al final si
los intentos son iguales a 3 se imprime que fue numero máximo de
intentos alcanzados.
