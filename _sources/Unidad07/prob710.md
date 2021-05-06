---
**Solución**

a) En este problema se propone el siguiente lazo de control:

La respuesta de este sistema en el dominio de Laplace para un cambio en la consigna es:

$$y = \frac{G_c G_f G_p}{1 + G_c G_f G_p} y_{sp}$$

Sustituyendo se encuentra:

$$y = \frac{\frac{10}{11}}{\frac{3}{11} s^2 + \frac{4}{11} s + 1} 
   \frac{2}{s}$$

b) A partir del conocimiento de las ecuaciones de la respuesta de un proceso de segundo orden para una entrada en escalón se puede obtener la respuesta en tiempo real fácilmente. En función del coeficiente de amortiguamiento se elije una de las ecuaciones. Se puede calcular el coeficiente de amortiguamiento sabiendo:

$$\left\{\begin{array}{l}
     \tau^2 = \frac{3}{11}\\
     2 \tau \zeta = \frac{4}{11}
   \end{array}\right.$$
   
Resolviendo la ecuación anterior se encuentra:

$$\left\{\begin{array}{l}
     \tau = 0.5222\\
     \zeta = 0.3482
   \end{array}\right.$$
   
El coeficiente de amortiguamiento es menor que la unidad, lo que significa que se trata de un sistema subamortiguado. La respuesta será:

$$y (t) = K_p M \left[ 1 - \frac{1}{\sqrt[]{1 - \zeta^2}} e^{- \zeta
   \frac{t}{\tau}} \sin \left( \frac{1}{\sqrt[]{1 - \zeta^2}} 
   \frac{t}{\tau} + \ensuremath{\operatorname{atan}} \frac{\sqrt[]{1 - \zeta^2}}{\zeta} \right)
   \right]$$ donde:

-   $K_p$ es la ganancia del proceso. En este caso
    $K_p = \frac{10}{11}$.

-   *M* es la altura del escalón ($M = 2$).

Por tanto la respuesta en tiempo real es:

$$y (t) = 1.818 [1 - 1.067 \mathrm{e}^{- 0.6667 t} \sin (2.043 t + 1.215)]$$

c) Si se representa la función anterior se obtiene:

::: {.center}
:::

En la gráfica se puede observar claramente que el valor máximo de la
respuesta tiene el valor de $A + B$. El valor de $B$ es el valor
estacionario que alcanza el lazo de control, es decir:

$$B = \lim_{t \to \infty} y (t) = \lim_{s \to 0} s y (s)$$

Para poder calcular el valor de $A$ sólo hay que recordar la definición de *overshoot*:

$$\mathrm{Overshoot = \frac{A}{B}$$

Por tanto el valor máximo de $y (t)$ es:

$$y_{\max} = A + B = (\mathrm{overshoot + 1) B$$

El *overshoot* es:

$$\mathrm{Overshoot = \exp \left( \frac{- \pi \zeta}{\sqrt[]{1 - \zeta^2}}
   \right) = 0.3113$$
   
El valor de _B_ es:

$$B = lim_{s \to 0} s \frac{\frac{10}{11}}{\frac{3}{11}
   s^2 + \frac{4}{11} s + 1}  \frac{2}{s} = \frac{20}{11}$$
   
Por tanto el valor máximo de la respuesta es:

$$y_{\max} = (0.3113 + 1)  \frac{10}{11} = 2.384$$

Para encontrar en que instante se produce este valor máximo de respuesta hay que resolver la siguiente ecuación:

$$y_{\max} = 2.384 = 1.818 [1 - 1.067 \mathrm{e}^{- 0.6667 t_{\max}} \sin
   (2.043 t_{\max} + 1.215)]$$
   
El resultado es: $$t_{\max} = 1.82$$

d) El periodo de osiclación es:

$$T = \frac{2 \pi \tau}{\sqrt[]{1 - \zeta^2}}$$

Sustituyendo se obtiene:

$$T = 3.50$$

e) La respuesta en tiempo real está dibujada más arriba.
