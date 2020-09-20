## Taller de programación de un chat TCP en Python

Este es un pequeño taller realizado para los nuevos alumnos de ingeniería informática de la universidad de La Laguna (Tenerife, Canarias) del curso 2020/2021.

El objetivo del propio taller es darles una pincelada de lo que podrán hacer con los estudios que van a cursar y, por supuesto, motivarlos con la carrera.

Las diapositivas del taller se encuentran [aquí](https://docs.google.com/presentation/d/1k2SgG8PVc1xKtqsNj5Zx--CJ15h7R6cH0Yk5OHdFBno/edit?usp=sharing)

## Estructura

Cada carpeta conlleva una serie de pasos que va complicando más el código.

Esto esta hecho así para que el código "final" sea más fácil de entender.

Cualquier duda, pregúntame directamente :)


## Problema en Windows

El código final no funciona bien en Windows. Esto se debe a la api del sistema operativo que se bloquea complemamente en la llamada de la función "conn.recv" y es algo que, para solucionar, habría que hacer unos cuantos hacks.

Esto en linux no ocurre debido a que los sockets que implementa linux en su api, permite hacer lecturas al socket recurrentes, sin tener la obligación de recibir 'algo'.

Dejo links con más información para ambos casos.


# Links:
https://bugs.python.org/issue41437  => Cómo hacer el hack en Windows
https://stackoverflow.com/questions/24512846/python-how-to-stop-a-thread-thats-waiting-for-a-recv => Las soluciones de aquí deberían funcionar en linux.
