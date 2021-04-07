<!-- #region -->
# Respuesta a una función impulso

+++

Al introducir un impulso de área $A$ se obtiene la siguiente respuesta:

$$y (s) = \frac{K_p}{\tau_p s + 1} A$$ 

que en tiempo real es:


$$y (t) = \frac{K_p A}{\tau_p} \mathrm{e}^{- \frac{t}{\tau_p}}$$
<!-- #endregion -->

```python
from sympy import *
t, Kp, A = symbols("t K_p A", real=True)
Tp = symbols('tau_p', positive=True)
s = symbols('s')

f = A
G = Kp/(Tp*s + 1)

y = inverse_laplace_transform(G*f, s, t)
y
```

De forma adimensional se puede escribir:

$$\frac{y (t)}{K_p A} = \mathrm{e}^{- \frac{t}{\tau_p}}$$

se obtiene la función simétrica a la respuesta a una entrada en escalón, lo que
implica que tiene las mismas características.

```python
y_imp = inverse_laplace_transform(G*f, s, t).subs({A:1, Kp:1, Tp: 1})

y_esc = inverse_laplace_transform(G*A/s, s, t).subs({A:1, Kp:1, Tp: 1})
```

```python
plot(y_imp, y_esc, (t, -1, 5));
```

```python

```
