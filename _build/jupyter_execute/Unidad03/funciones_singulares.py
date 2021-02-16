# Transformadas de algunas funciones singulares

A continuación se muestran las transformadas de algunas funciones con
las que se trabajará frecuentemente más adelante ya que pueden ser
asimiladas como las perturbaciones más frecuentes.

Si no se dice lo contrario todas estas funciones se definen para que su
valor sea nulo a tiempo menor que cero.

## Función escalón

Es una función cuyo valor para tiempos menores que cero es nulo y que
alcanza el valor $M$ para tiempo mayores que 0:

from ipywidgets import interact

from sympy import Heaviside, plot, Symbol

t = Symbol('t')

def f(M):
    plot(M*Heaviside(t), (t, -1,5), line_color='red')

interact(f, M=(-5, 5, 0.1));

```{glue:figure} step_fig
---
align: center
name: step-fig
figclass: margin-caption
---
Función escalón de altura $M$. Utilizando el control deslizante se puede modificar la altura del escalón de manera interactiva.
```

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M & t > 0
   \end{array}\right.$$

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \frac{M}{s}$$

Si $M$ es igual a 1 se tiene la función escalón unidad, $U(t)$.

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

Por tanto, aplicando la propiedad número
[\[translacion\]](#translacion){reference-type="ref"
reference="translacion"} (ecuación
[\[ec:translacion\]](#ec:translacion){reference-type="ref"
reference="ec:translacion"}), la transformada de Laplace será:

$$\mathcal{L} [f (t - t_0)] = \frac{M}{s} \mathrm{e}^{- s t_0}$$

## Función pulso

Se trata de una función pulso con área $A = M t_0$:

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

Se trata de un pulso tal que $M \rightarrow \infty$ y
$t_0 \rightarrow 0$:

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \bar{f} (s) = A$$

En el caso particular de que el área sea 1 se habla de la función delta
de Dirac $\delta (t)$.

Se puede comprobar fácilmente que el impulso es la derivada de la
función escalón.

```{admonition} Ejemplo
En el Problema 3.4 se puede comprobar las diferencias y similitudes en
la respuesta de un proceso a una entrada en escalón y en impulso.
```

## Función rampa

Se trata de una función lineal de pendiente *M*:

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M t & t > 0
   \end{array}\right. = M t U (t)$$

La transformada de Laplace es:

$$\mathcal{L} [M t U (t)] = \frac{M}{s^2}$$

## Funciones trigonométricas

La función seno es:

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