# Problema 7.1

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

La localización de un cambio de carga en un lazo de control puede afectar a la respuesta del sistema. En el diagrama de bloques adjunto se produce un cambio en escalón unidad en la posición 1 ó 2.La localización de un cambio de carga en un lazo de control puede afectar a la respuesta del sistema. En el diagrama de bloques adjunto se produce un cambio en escalón unidad en la posición 1 ó 2.

![prob701.svg](./img/prob701.svg)

1.  ¿Cuál será la frecuencia del estado transitorio si la variación se produce en la posición 1? ¿Y si es en la 2?

2.  ¿Cuánto valdrá el offset en cada caso? Suponer un escalón unidad.

---

**Solución**

a) Para poder encontrar la frecuencia del estado transitorio será necesario conocer el coeficiente de amortiguamiento de este lazo de control.

_Entrada en $U_1$_

Para poder encontrar $\zeta$ es necesario calcular, en primer lugar, la función de transferencia que describe la dinámica del lazo de control para una entrada de perturbaciones en $U_1$. La función de transferencia será:

$$\frac{C}{U_1} = \frac{\frac{2}{2 s + 1}  \frac{1}{2 s + 1}}{1 + K_c 
   \frac{2}{2 s + 1}  \frac{1}{2 s + 1}}$$

En el numerador aparecen las funciones de transferencia existentes entre la entrada ($U_1$) y la salida ($C$). El denominador es 1 más el producto de las funciones de
transferencia del lazo de control.

Operando se encuentra que:

$$\frac{C}{U_1} = \frac{\frac{2}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s + 1}$$

Es importante resaltar que el término independiente del denominador debe ser 1.

Como era de esperar la función de transferencia es la de un sistema de segundo orden. Por tanto: 

$$\left\{\begin{array}{l}
     \tau^2 = \frac{4}{11}\\
     2 \tau \zeta = \frac{4}{11}
   \end{array}\right.$$
   
Operando se encuentran las siguientes soluciones:

$$\left[ \left[ \tau = - \frac{2 \sqrt{11}}{11}, \zeta = -
   \frac{1}{\sqrt{11}} \right], \left[ \tau = \frac{2 \sqrt{11}}{11}, \zeta =
   \frac{1}{\sqrt{11}} \right] \right]$$
   
La constante de tiempo de un sistema y el coeficiente de amortiguamiento de un sistema deben ser siempre positivos. Por tanto el coeficiente de amortiguamiento toma el valor de $\frac{1}{\sqrt[]{11}}$.

La frecuencia del estado transitorio es:

$$\nu = \frac{\sqrt[]{1 - \zeta^2}}{2 \pi \tau}$$

Sustituyendo se obtiene:

$$\nu = 0.252$$

_Entrada en $U_2$_

En este caso la función de transferencia es:

$$\frac{C}{U_2} = \frac{\frac{1}{2 s + 1}}{1 + K_c  \frac{2}{2 s + 1} 
   \frac{1}{2 s + 1}} = \frac{\frac{2}{11} s + \frac{1}{11}}{\frac{4}{11} s^2
   + \frac{4}{11} s + 1}$$
   
El denominador obtenido es el mismo que en el caso anterior, lo que significa que el coeficiente de amortiguamiento y la frecuencia serán iguales.

Se comprueba que lo que marca la respuesta de un lazo de control es el denominador de la función de transtferencia. El numerador influye principalmente en términos transitorios cuya influencia sobre la dinámica del sistema disminuye rápidamente.

b) En ambos casos el *offset* valdrá:

$$\mathrm{Offset} = \lim_{t \to \infty} [R (t) - C (t)]$$

Realizando la transformada de Laplace y aplicando el teorema del valor final se obtiene:

$$\mathrm{Offset} = \lim_{s \to 0} [s R (s) - s C (s)]$$

En este problema la consgina no cambia, lo que significa que $R (s) = 0$.

_Entrada en $U_1$_

Se realiza un cambio en escalón unidad, la respuesta del lazo de control será:

$$C = \frac{\frac{2}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s + 1} U_1 =
   \frac{\frac{2}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s + 1}  \frac{1}{s}$$
   
El *offset* será:

$$\mathrm{Offset} = \lim_{s \to 0} \left[ 0 - s
   \frac{\frac{2}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s + 1}  \frac{1}{s}
   \right] = - \frac{2}{11}$$

_ Entrada en $U_2$_

La respuesta del lazo de control en este caso es:

$$C = \frac{\frac{2}{11} s + \frac{1}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s
   + 1} U_2 = \frac{\frac{2}{11} s + \frac{1}{11}}{\frac{4}{11} s^2 +
   \frac{4}{11} s + 1}  \frac{1}{s}$$
   
El *offset* es:

$$\mathrm{Offset} = \lim_{s \to 0} \left[ 0 - s
   \frac{\frac{2}{11} s + \frac{1}{11}}{\frac{4}{11} s^2 + \frac{4}{11} s + 1}
   \frac{1}{s} \right] = - \frac{1}{11}$$
