---
jupytext:
  cell_metadata_filter: -all
  formats: md:myst,ipynb
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.12
    jupytext_version: 1.8.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Inversión de transformadas. De vuelta al tiempo real

Continuando con el ejemplo se estudiará la salida del sistema para una
entrada de tipo escalón unidad:

$$\bar{H} (s) = \left[ \frac{R}{R A s + 1} \right]  \overline{Q_1} (s) =
   \left[ \frac{R}{R A s + 1} \right]  \frac{1}{s}$$

Mediante el operador transformada inversa de Laplace
($\mathcal{L}^{- 1}$) se obtiene la salida en tiempo real. Para ello hay
que descomponer la función a invertir en partes asimilables a las que se
encuentran en las tablas de transformadas de Laplace (apartado
{ref}`transformadas`):

$$\bar{H} (s) = \left[ \frac{R}{R A s + 1} \right]  \frac{1}{s} = \frac{a}{s}
   + \frac{b}{s + \frac{1}{A R}}$$

Donde $a$ y $b$ son dos variables a
determinar. Obviamente, $a =
R$ y $b = - R$. Por tanto,

$$H (t) = \left[ R - R \mathrm{e}^{- \frac{t}{R A}} \right] U (t) = R U (t)
   \left[ 1 - \mathrm{e}^{- \frac{t}{R A}} \right] = R U (t)  \left[ 1 - \mathrm{e}^{-
   \frac{t}{\tau}} \right]$$
   
donde $\tau = R A$ es la constante de
tiempo y tiene dimensiones de tiempo.

Tamibén se puede realizar la transformada inversa de Laplace de una manera muy simple utilizando *Sympy*:

```{code-cell} ipython3
# Importación de las funciones necesarias
# Cuando se trabaja de manera interactiva es común usar:
#
# from sympy import *
#
# para no tener que preocuparse de que funciones están disponibles.
from sympy import inverse_laplace_transform, symbols

# Definición de los símbolos necesarios
R, A, t = symbols("R A t", real=True)
s = symbols("s")

# Definición de la función de transferencia, G(s)
G = R/(R*A*s+1)

# Definición de la función de entrada, f(s), en este caso un escalón unidad
f = 1/s

# Cálculo de la respuesta, H(t)
inverse_laplace_transform(G*f, s, t)
```

Cuanto mayor es $\tau$ más lenta es la respuesta, más tarda el sistema en alcanzar el estado estacionario. Se comprueba
que cuanto menor es la sección del tanque más rápida es la respuesta. Si
$\tau$ es grande se dice que el sistema presenta una gran inercia.

```{code-cell} ipython3
:tags: [hide-input]

from ipywidgets import FloatSlider, interactive_output

from sympy import plot, inverse_laplace_transform, symbols


tau, t = symbols('tau, t', real=True)
s = symbols('s')

T = FloatSlider(value=1.5, min=0.1, max=12, step=.1, continuous_update=False, description=r'$\tau$')

y = 1/(tau*s+1)*1/s
yt = inverse_laplace_transform(y, s, t)

def f(T):
    taus = [0.5, 1, 2, 4, 8, T]
    p = plot(yt.subs(tau, 0.5),
             yt.subs(tau, 1),
             yt.subs(tau, 2),
             yt.subs(tau, 4),
             yt.subs(tau, 8),
             yt.subs(tau, T),
             (t, -1, 10), legend=True, size= [8, 4], show=False)
    for i in range(len(taus)):
        p[i].label = str(taus[i])
    p[0].line_color = "yellow"
    p[1].line_color = "lime"
    p[2].line_color = "cyan"
    p[3].line_color = "green"
    p[4].line_color = "brown"
    p[5].line_color= 'red'
    p.show()

display(T)
interactive_output(f, {'T':T})
```

```{admonition} Ejemplo
La técnica propuesta en este capítulo para obtener modelos matemáticos
se puede utilizar para modelos de mayor complejidad, como el que se
obtiene en la resolución del problema 3.7.
```