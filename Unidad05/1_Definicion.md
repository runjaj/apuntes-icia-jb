# Definición de sistema de segundo orden

Un sistema de segundo orden es aquel cuya salida *y(t)* puede ser
descrita por una ecuación diferencial de segundo orden:

$$a_2  \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + a_1  \frac{\mathrm{d}y}{\mathrm{d}t} + a_0 y
   = b f (t)$$

Si $a_0 \neq 0$:

$$\tau^2  \frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + 2 \zeta \tau \frac{\mathrm{d}y}{\mathrm{d}
   t} + y = K_p f (t)$$ 
   
donde $\tau^2 = \frac{a_2}{a_0}$,
$2 \zeta \tau = \frac{a_1}{a_0}$ y $K_p =
\frac{b}{a_0}$. 

Las nuevas constantes son:

-   $\tau$ es la constante de tiempo (o período natural del sistema)

-   $\zeta$ es el coeficiente (o factor) de amortiguamiento

-   $K_p$ es la ganancia del proceso, tiene el mismo significado que
    para los sistemas de primer orden

Tomando variables de desviación y condiciones iniciales iguales a cero,
la función de transferencia queda como:

$$G (s) = \frac{K_p}{\tau^2 s^2 + 2 \zeta \tau s + 1}$$

Los sistemas de segundo orden se pueden clasificar en tres categorías:

1.  Procesos consistentes en dos o más procesos de primer orden, en
    serie o en paralelo, por los que fluye materia o energía.

2.  Sistemas inherentes de segundo orden. No son frecuentes en las
    industria, algunos ejemplos son los manómetros o las válvulas
    neumáticas.

3.  Un proceso con su controlador presenta una dinámica de segundo orden
    o de orden superior.
