# Problema 7.4

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

Sea el sencillo lazo de control de la figura:

![prob704.svg](./img/prob704.svg)

donde $G_p = \frac{k}{s(s+p)}$.

Determinar la ganancia k y el parámetro p para que la dinámica del sistema responda a las siguientes características:

1. Para un cambio en escalón el overshoot debe ser inferior al 5%.

2. El periodo de oscilación de 4 s.

---

**Solución**

La función de transferencia del lazo de control es:

$$G (s) = \frac{\bar{Y} (s)}{\bar{R} (s)} = \frac{G_p (s)}{1 + G_p (s)} =
   \frac{1}{\frac{1}{k} s^2 + \frac{p}{k} s + 1}$$
   
La función de transferencia de un sistema de segundo orden es:

$$G (s) = \frac{K_p}{\tau_p^2 s^2 + 2 \tau_p \zeta s + 1}$$

Por tanto:

$$\begin{aligned}
  \tau_p^2 &= \frac{1}{k}\\
  2 \tau_p \zeta &= \frac{p}{k}
\end{aligned}$$

Resolviendo el sistema de ecuaciones se obtiene:

$$\begin{aligned}
  \tau_p &= \sqrt{\frac{1}{k}} \\
  \zeta &= \frac{p}{2 \sqrt[]{k}}
\end{aligned}$$

El *overshoot* de este sistema de ser inferior al 5%, por tanto, el caso límite es que el *overshoot* tome el valor de 0.05:

$$0.05 = \exp \left( - \frac{\pi \zeta}{\sqrt{1 - \zeta^2}} \right)$$

Resolviendo la ecuación se encuentra que el coeficiente de amortiguamiento es $\zeta = 0.6901$.

El periodo del lazo de control debe ser de 4 s, lo que implica que:

$$T = 4 \text{s} = \frac{2 \pi \tau_p}{\sqrt{1 - \zeta^2}}$$

Sustituyendo el coeficiente de amortiguamiento se encuentra que la
constante de tiempo es $\tau_p = 0.4607$.

Una vez conocidos el coeficiente de amortiguamiento y la constante de
tiempo encontrar los parámetros del proceso es trivial:

$$\begin{aligned}
  k &= 4.71 \\
  p &= 3.00
\end{aligned}$$
