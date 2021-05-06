# Métodos de criterio único

En este caso se trata de seleccionar uno de los múltiples parámetros que describen el comportamiento de un lazo de control retroalimentado y utilizarlo para el diseño del controlador. Se elegirán los parámetros del controlador en función del rendimiento deseado para ese parámetro.

Es posible tomar como parámetro el *offset*, de manera que el resultado será que se desean eliminar errores que permanezcan durante periodos largos de tiempo. Este es un criterio de estado estacionario.

También se puede seleccionar un criterio dinámico, como puede ser la frecuencia de oscilación  de la parte transitoria de la respuesta. También se pueden tomar parámetros como puede ser el *overshoot*, el tiempo necesario para alcanzar el $\pm 5\%$ de un cierto valor, el *rise time*, etc. Es frecuente que la selección de un cierto criterio haga imposible que se cumpla otro. Por ejemplo, si se trata de reducir el *overshoot* reduciendo la ganancia proporcional, se aumenta el *rise time*.

Uno de los criterios más frecuentes es seleccionar los parámetros del controlador para que la razón de disminución tome el valor de $\frac{1}{4}$.

