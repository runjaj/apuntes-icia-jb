# Acción de control proporcional

En este caso se considera que $G_m = 1$, $G_f = 1$ y $G_c = K_c$, de manera que la respuesta del lazo de control será:

$$y = \frac{K_c G_p}{1 + K_c G_p} y_{sp} + \frac{G_d}{1 + K_c G_p} d$$ (salida_bucle)

## Procesos de primer orden

Para un proceso de primer orden sin sistema de control (lazo abierto, *open loop*):

$$\tau_p  \frac{\mathrm{d}y (t)}{\mathrm{d}t} + y (t) = K_p f (t) + K_d d (t)$$

con $y (0) = f (0) = d (0) = 0$, ya que se trata de variables de desviación. Realizando la transformada de Laplace de la ecuación diferencial anterior y operando se encuentra:

$$y (s) = \frac{K_p}{\tau_p s + 1} f (s) + \frac{K_d}{\tau_p s + 1} d (s)$$

Es decir: 

$$\begin{aligned}
 \text{Para un cambio en la consigna: } &
  G_p = \frac{K_p}{\tau_p s + 1} & \\
  \text{Para un cambio en la carga: } & G_d
  = \frac{K_d}{\tau_p s + 1} & \end{aligned}$$

Sustituyendo en la {eq}`salida_bucle`, salida de un bucle de retroalimentación (lazo cerrado, *closed loop*) y ordenando términos:

$$y = \frac{K_p'}{\tau'_p s + 1} y_{sp} + \frac{K_d'}{\tau'_p s + 1} d$$

donde $\tau'_p = \frac{\tau_p}{1 + K_p K_c}$, $K'_p = \frac{K_p K_c}{1 + K_p
K_c}$ y $K'_d = \frac{K_d}{1 + K_p K_c}$.

Se observa que:

1.  El lazo de control es un sistema de primer orden, al igual que el proceso

2.  La respuesta del lazo de control es más rápida que la del proceso ($\tau'_p < \tau_p$)

3.  El sistema formado por el proceso y el bucle de retroalimentación es menos sensible a los cambios que el sistema formado solamente por el proceso en sí ya que $K'_p < K_p$ y $K'_d < K_d$

Si se considera un cambio en la consigna según un escalón unidad y no se produce perturbación alguna ($d = 0$), se puede apreciar mejor el efecto del controlador proporcional. En este caso se observa que la respuesta final obtenida por el lazo de control no es la exigida por la consigna. Esta discrepancia es el *offset*

a\) b)

. Se define el *offset* como la diferencia entre el valor final de la consigna y el valor final de la respuesta:

$$\textit{Offset} = \lim_{t \to \infty} (y_{sp}-y)$$


Aplicando el Teorema del valor final ({eq}`valor_final`):

$$\textit{Offset} = \lim_{s \to 0} (s y_{sp}- s y)$$

En este caso:

$$\textit{Offset} = \lim_{s \to 0} \left(
   s \frac{1}{s} - s \frac{K'_p}{\tau'_p s + 1}  \frac{1}{s} \right) = 1 -
   \frac{K_p K_c}{1 + K_p K_c} = \frac{1}{1 + K_p K_c}$$

Para el problema de la regulación ($d = \frac{1}{s}$ y $y_{sp} = 0$):

$$\textit{Offset} = - \frac{K_d}{1 + K_p K_c}$$

Se observa en los dos caso que para eliminar el *offset* ($\textit{offset} \to 0$), la ganancia del controlador debe hacerse muy elevada ($K_c \to \infty$). Por razones de estabilidad, que se verán más adelante, no es conveniente utilizar valores elevados de $K_c$ para eliminar el *offset*.

Si el proceso es un integrador puro $\left( G_c = \frac{K_p}{s} \right)$, como por ejemplo la dinámica del nivel de un depósito, se comprueba que un sistema de control P es capaz de mantener el nivel de líquido en en el valor deseado dentro de un cierto margen. Si se calcula el *offset* de este tipo de sistemas (proceso más lazo de control) para una entrada en escalón, se obtiene el valor $- \frac{1}{K_c}$. Este valor puede ser aceptable para valores suficientemente elevados de $K_c$.

## Procesos de 2º orden

Se considera un lazo de control como el del caso anterior pero en el que se ha sustituido el proceso por un sistema de segundo orden. Si se realiza un cambio en la consigna, la respuesta queda como:

$$y = \frac{K'_p}{\tau^{\prime 2} s^2 + 2 \zeta' \tau' s + 1} y_{sp}$$

donde $\tau' = \frac{\tau}{\sqrt{1 + K_p K_c}}$, $\zeta' = \frac{\zeta}{\sqrt{1 + K_p K_c}}$ y $K_p = \frac{K_p K_c}{1 + K_p K_c}$.

Se cumple que:

1.  El lazo de control continua siendo un sistema de segundo orden.

2.  $K'_p < K_p$, $\tau' < \tau'$ y $\zeta' < \zeta$.

3.  Para una entrada en escalón unidad, *offset*$= \frac{1}{1 + K_p K_c}$. De nuevo, el *offset* tiende a 0, cuando la ganancia proporcional del controlador tiende a infinito.

4.  Dependiendo de $\zeta$, $\zeta'$ puede ser menor, mayor o igual a 1. Si la respuesta es sobreamortiguada, la velocidad de la respuesta es más lenta. Por tanto es preferible aumentar $K_c$ para lograr una respuesta subamortiguada. De esta manera se logra una respuesta más rápida y con un *offset* menor. El problema es que al aumentar $K_c$ aumenta el *overshoot*---lo que implica un aumento en la razón de disminución---y decrece el periodo de oscilación.
