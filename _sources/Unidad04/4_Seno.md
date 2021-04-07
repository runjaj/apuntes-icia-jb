
# Respuesta a una función sinusoidal

+++

Para una entrada sinusoidal de tipo:

$$f (t) = M U (t) \sin \omega t$$

se obtiene la siguiente respuesta:

$$y (s) = \frac{K_p}{\tau_p s + 1}  \frac{M \omega}{s^2 + \omega^2}$$

que en tiempo real es:

$$y (t) = \frac{K_p M}{1 + \omega^2 \tau_p^2}  \left( \omega \tau_p \mathrm{e}^{-
   \frac{t}{\tau_p}} \cos \omega t + \sin \omega t \right)$$

Aplicando la propiedad trigonométrica:

$$x \sin \alpha + y \cos \alpha = z \sin (\alpha + \varphi)$$

donde $z^2 = x^2 + y^2$ y $\tan \varphi = \frac{y}{x}$, se obtiene:

$$\label{ec:sinusoidal-1} y (t) = \frac{K_p M \omega \tau_p}{1 + \omega^2
  \tau_p^2} \mathrm{e}^{- \frac{t}{\tau_p}} + \frac{K_p M}{\sqrt[]{1 + \omega^2
  \tau_p^2}} \sin (\omega t + \varphi)$$
  
donde $\varphi = \mathrm{atan} (- \omega \tau_p)$.

El primer término de la respuesta es un término transitorio, ya que
tiende a cero cuando el tiempo tiende a infinito. Este término pierde
importancia para tiempos grandes.

La respuesta obtenida es de tipo sinusoidal con la misma frecuencia de
oscilación $\omega$ que la entrada pero con un desfase $\varphi$. Además
el desfase está directamente relacionado con la frecuencia angular. Al
aumentar el desfase, aumenta el desfase.

En el caso de que la frecuencia angular tienda a infinito, el desfase
tiende a $\frac{\pi}{2}$, que es el desfase máximo.

```python
from sympy import *

```
