
# Definición de sistema lineal de primer orden

Un sistema de primer orden es aquel cuya salida $y(t)$ puede ser modelada por una ecuación diferencial de primer orden como:

```{math}
:label: ode1
a_1  \frac{\mathrm{d}y (t)}{\mathrm{d}t} + a_0 y (t) = b f (t)
```

donde $f(t)$ es la entrada al sistema.

Si $a_0 \neq 0$:

$$\frac{a_1}{a_0}  \frac{\mathrm{d}y (t)}{\mathrm{d}t} + y (t) = \frac{b}{a_0} f(t)$$

Si se define $\frac{a_1}{a_0} = \tau_p$ y $\frac{b}{a_0} = K_p$ y se sustituye en la ecuación anterior se obtiene:

```{math}
:label: ode_primer_orden
\tau_p  \frac{\mathrm{d}y (t)}{\mathrm{d}t} + y (t) = K_p f (t)
```

donde:

-   $\tau_p$ es la constante de tiempo del proceso

-   $K_p$ es la ganancia del proceso

Si $y(t)$ y $f(t)$ están definidos mediante la utilización de variables de desviación alrededor del estado estacionario, las condiciones iniciales son $y(0)=0$ y $f(0)=0$.

Operando se encuentra la función de transferencia de un proceso de primer orden: 

$$G (s) = \frac{K_p}{\tau_p s + 1}$$

Los sistemas de primer orden son los más frecuentes en los procesos de la industria alimentaria, por ello su estudio es de gran importancia. Estos sistemas se caracterizan por:

1.  Su capacidad de almacenar materia, energía o cantidad de movimiento. Esta capacidad está directamente relacionada con la ganancia del proceso.

2.  Una resistencia asociada con el caudal de materia, energía o cantidad de movimiento. Esta resistencia o inercia viene dada por la constante de tiempo.

En el caso particular de que $a_0 = 0$:

 $$G (s) = \frac{K_p}{\tau_p s}$$

Se trata de aquellos sistemas de primer orden denominados integradores puros y se hablará de ellos más adelante.
