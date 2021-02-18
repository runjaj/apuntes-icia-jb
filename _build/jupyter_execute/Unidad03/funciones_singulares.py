# Transformadas de algunas funciones singulares

A continuación se muestran las transformadas de algunas funciones con
las que se trabajará frecuentemente más adelante ya que pueden ser
asimiladas como las perturbaciones más frecuentes.

Si no se dice lo contrario todas estas funciones se definen para que su
valor sea nulo a tiempo menor que cero.

## Función escalón

Es una función cuyo valor para tiempos menores que cero es nulo y que
alcanza el valor $M$ para tiempo mayores que 0:

```{figure} ./img/0.png
---
figclass: margin
align: left
---
Función escalón de altura $M$.

Se puede modificar el valor de $M$ utilizando el deslizador (solo cuando se visualiza el *notebook*).
```

from ipywidgets import interact

from sympy import Heaviside, plot, Symbol

t = Symbol('t')

def f(M):
    plot(M*Heaviside(t), (t, -1,5), line_color='red')

interact(f, M=(-3, 5, 0.5), continuous_update=False);

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M & t > 0
   \end{array}\right.$$

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \frac{M}{s}$$

Si $M$ es igual a 1 se habla de la función escalón unidad, $U(t)$, o de la función de Heaviside, $\theta(t)$.

Encontrar la transformada inversa de Laplace es muy sencillo utilizando *Sympy*:

# Cargamos las funciones necesarias para el ejemplo
from sympy import Heaviside, laplace_transform, symbols

# Definición de las variables que vamos a utilizar
M, t, s = symbols('M t s')

# Definimos un escalón unidad de altura M
f = M*Heaviside(t)

# Calculamos la trasnformada inversa de Laplace
laplace_transform(f, t, s, noconds=True)

En el cálculo anterior, se ha utilizado la función de ```Heaviside``` como función escalón unidad. También se puede realizar el cálculo definiendo la función escalón como una constante $M$ y asumiendo de manera implicita que ese valor es solo para $t > 0$:

# Cargamos las funciones necesarias para el ejemplo
from sympy import Heaviside, symbols

# Definición de las variables que vamos a utilizar
M, t, s = symbols('M t s')

# Definimos un escalón unidad de altura M
f = M

# Calculamos la trasnformada inversa de Laplace
laplace_transform(f, t, s, noconds=True)

Aunque la mayor parte de las veces las funciones de entrada sucende a tiempo 0, no es raro que aparezcan desplazadas en el tiempo, que sufran un retraso $t_0$.

```{figure} ./img/0.png
---
figclass: margin
align: left
---
Función pulso unidad retrasada en el tiempo un valor $t_0$.

Se puede modificar el valor del retraso utilizando el deslizador.
```

from ipywidgets import FloatSlider, interactive_output

from sympy import Heaviside, plot, Symbol

t = Symbol('t')

to = FloatSlider(value=0, min=0, max=5, step=.2, description=r"$t_0$", continuous_update=False)

def f(to):
    plot(Heaviside(t-to), (t, -1,5), line_color='red')

display(to)
interactive_output(f, {'to':to})

En el caso de que la función tenga un retraso $t_0$:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < t_0\\
     M & t > t_0
   \end{array}\right.$$

O lo que es lo mismo:

$$f (t - t_0) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M & t > 0
   \end{array}\right.$$

Por tanto, aplicando la propiedad de la transformada de Laplace, [translación de la transformada](transformada) (ecuación {eq}`translacion`), la transformada de Laplace será:

$$\mathcal{L} [f (t - t_0)] = \frac{M}{s} \mathrm{e}^{- s t_0}$$

## Función pulso

Se trata de una función pulso con área $A = M t_0$. A continuación, en la figura de la derecha se muestra un pulso de altura unidad, $M=1$. El pulso (línea roja) es la suma de un pulso unidad (línea verde) al que se le suma un pulso de altura -1 retrasado un tiempo igual a la anchura del pulso, es decir, $t_0$:

```{figure} ./img/0.png
---
figclass: margin
align: left
---
Un pulso, figura de la derecha, es la resta de dos funciones escalón de igual altura. El escalón negativo (azul) anula al escalón verde y forma el pulso.

Se puede modificar la anchura del pulso $t_0$ utilizando el deslizador (solo cuando se visualiza el *notebook*).
```

from ipywidgets import interact

from sympy import Heaviside, plot, Symbol
from sympy.plotting import PlotGrid

t = Symbol('t')

def f(to):
    p1 = plot(Heaviside(t), -Heaviside(t-to), (t, -1,6), show=False)
    p2 = plot(Heaviside(t)-Heaviside(t-to), (t, -1,6), line_color = 'red', show=False)
    p1[0].line_color = 'green'
    p1[1].line_color = 'blue'
    PlotGrid(1, 2 , p1, p2, size=[12,4]);
    
interact(f, to=(0, 5, 0.5), continuous_update=False);

La función pulso se define como:

$$f (t) = \left\{\begin{array}{cc}
     0 & t < 0\\
     M & 0 < t < t_0\\
     0 & t > t_0
   \end{array}\right.$$

Utilizando la definición del escalón unidad también se puede escribir
como:

$$f (t) = M [U (t) - U (t - t_0)]$$

Por tanto, la transformada de Laplace será:

$$\mathcal{L} [f (t)] = \bar{f} (s) = M \left( \frac{1}{s} - \frac{\mathrm{e}^{-
   s t_0}}{s} \right) = \frac{M}{s}  (1 - \mathrm{e}^{- s t_0})$$

## Función impulso

Se trata de un pulso de área $A$ tal que $M \rightarrow \infty$ y
$t_0 \rightarrow 0$:

```{figure} ./img/impulso.svg
---
width: 300px
figclass: margin-caption
---
Función impulso de área $A$.
```

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \bar{f} (s) = A$$

En el caso particular de que el área sea 1 se habla de la función delta
de Dirac $\delta (t)$.

A continuación se calcula la transformada de Laplace de un impulso de altura A, $f(t) = A \delta(t)$:

from sympy import laplace_transform, DiracDelta, symbols

A, t, s = symbols('A t s')

laplace_transform(A*DiracDelta(t), t, s, noconds=True)

Se puede comprobar fácilmente que el impulso es la derivada de la
función escalón.

```{admonition} Ejemplo
En el Problema 3.4 se puede comprobar las diferencias y similitudes en
la respuesta de un proceso a una entrada en escalón y en impulso.
```

## Función rampa

Se trata de una función lineal de pendiente $M$:

```{figure} ./img/0.png
---
figclass: margin
align: left
---
Función rampa de pendiente $M$.

Se puede modificar el valor de $M$ utilizando el deslizador (solo cuando se visualiza el *notebook*).
```

from ipywidgets import interact

from sympy import Symbol, Heaviside

M = Symbol('M')

def f(M):
    plot(M*t*Heaviside(t), (t, -1,5), line_color='red')

interact(f, M=(-3, 5, 0.5), continuous_update=False);

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M t & t > 0
   \end{array}\right. = M t U (t)$$

La transformada de Laplace es:

$$\mathcal{L} [M t U (t)] = \frac{M}{s^2}$$

from sympy import laplace_transform, symbols

M, t, s = symbols('A t s')

laplace_transform(M*t, t, s, noconds=True)

## Funciones trigonométricas

La función seno es:

```{figure} ./img/0.png
---
figclass: margin
align: left
---
Función seno de frecuencia $\omega$.

Se puede modificar el valor de $\omega$ utilizando el deslizador (solo cuando se visualiza el *notebook*).
```

from ipywidgets import interact

from sympy import Symbol, Heaviside, sin

w = Symbol('omega')

def f(w):
    plot(sin(w*t)*Heaviside(t), (t, -1, 10), line_color='red', size=[8,4])

interact(f, w=(-3, 5, 0.5), continuous_update=False);

Se define la función como:

$$f (t) = \left\{\begin{array}{cl}
     0 & t < 0\\
     M \sin (\omega t) & t > 0
   \end{array}\right. = M U (t) \sin (\omega t)$$
   
donde $M$ es la amplitud y $\omega$ es la frecuencia angular, expresada
normalmente como rad/s.

La transformada de Laplace de la función seno es:

$$\mathcal{L} [M \sin (\omega t)] = \frac{M \omega}{s^2 + \omega^2}$$

y la de la función coseno:

$$\mathcal{L} [M \cos (\omega t)] = \frac{M s}{s^2 + \omega^2}$$

from sympy import laplace_transform, symbols, sin

M, w, t, s = symbols('M omega t s')

laplace_transform(M*sin(w*t), t, s, noconds=True)