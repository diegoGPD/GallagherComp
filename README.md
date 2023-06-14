
# Gallagher Compiler 2.0

Compilador realizado por Diego Garza Macias A01231795 para la clase de Diseño de Compiladores en el Tecnologico de Monterrey para el Semestre de Verano 2023.


El compilador fue desarollado completamente con el lenguage de programacion Python y esta enfocado en operaciones matematicas para poder en un futuro agregar funcionalidades las cuales puedan estar enfocadas en estadistica.




## Installation

Para poder hacer uso de Gallagher es necesario tener una version de Python 3 en el computador deseado. Ademas de que para su primer uso es necesario instalar las variables
    


## Como Funciona?

Para empezar a programar en Gallagher es necesario comenzar con un archivo vacio de .txt

Para empzar tu progama necesita empezar con el nombre de tu programa y una variabla declarada de la siguiente forma

```
Programa FindVal;
let int a;
```

Como podemos ver para declarar una variable es con el formato let luego el tipo y al final el nombre de la variable.

Despues de esto podemos comenzar a declarar funciones, la forma de delcar una funcion es la siguiente:

```
func fib(int n): int :{ Variable despues tu codigo }
```

Podemos ver que empezamos con la palabra reservada func la cual le sirve a Gallagher para saber que hay una funcion. Despuesde esto ponemos el nombre de la funcion seguido de un (, declaramos los parametros con su tipo y nombre, despues ponemos :  y el tipo de regreso que tendra la funcion para finalizar la iniciacion con :

Dentro de la funcion podemos declarar variables de diferentes tipo como lo son int, float, o hasta arrays de N dimensiones!

Para mandar a llamar una funcion es de la siguiente forma

```
    @fib(3);

```

Es necesario poner el caracter @ seguido del nombre de la funcion!

Para declarar un array es de la siguiente forma:

```
let int dos [1 10, 1 10];
```

Empezamos con la palabra reservada let para despues el tipo y nombre esto igual que con una variable normal, la diferencia radica es que despues declaramos el array con [incio de dimencion final, segunda dimencion final segunda diencion ...] y asi desde una hasta las dienciones que necesite.

Depsues para acceder a estos es necesario hacerlo de la siguiente forma

```
    dos[b, 8] = 3;
```

Como podemos ver solo ponemos el valor de cada dimension que queremos acceder, podemos acceder con variables, funciones, sumas restas o numeros planos!

Gallagher es capaz de realizar if, y else sin ningun problema la forma de realizar esto es la siguiente:

```
if(n <= 1){
        value = n;
}else{
    value = @fib(n - 1)  + @fib(n - 2);
}
```

Podemos anidar mas if declarando if en lugar de else.

Gallagher es capaz de tambien trabajar con while de la siguiente forma:


```
while(contador < 9){
    dos[1, contador] = contador + 2;
    contador = contador + 1;
}
```

Es necesario que tomes en cuenta que la variable condicional tiene que terminar para evitar ciclos infinitos.

Gallagher tiene la capacidad de imprimir variables en consola de la siguiente forma 

```
    printG(@fib(@fib(6)));
```

Con la palabra reservada printG para despues el valor que quieras imprimir, notaste que hizimoos una llamada recursiva sin problemas?


Para que Gallagher corra es necesario que tengas un main de la siguiente forma:

```
func main(): int : {
    let int b;
    TU CODIGO
```

Main sera lo que se ejecute en tu programa, aqui puedes tener sumas restas, llamadas a funciones impresiones condicionales lo que gustes sin problema

Disfruta de Gallagher!

LINK A DEMO https://youtu.be/wT_WjcPhBSA