# Problema 7.7

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

Sea el sistema cuyo diagrama de bloques se presenta en la figura adjunta:

![prob707.svg](./img/prob707.svg)

donde $G(s) = \frac{K}{s(s+1)}$ y $H(s)=1+K_ms$.

Determinar los valores de ganancia $K$ y de la constante $K_m$ para que la respuesta a un escalón unidad tenga un _overshoot_ de 0.2 al cabo de 1 s.

---

**Solución**

La función de transferencia que describe la dinámica de este sistema es:

$$\frac{Y (s)}{R (s)} = \frac{G (s)}{1 + G (s) H (s)} = \frac{\frac{K}{s (s +
   1)}}{1 + \frac{K}{s (s + 1)}  (1 + K_m s)} = \frac{1}{\frac{1}{K} s^2 +
   \frac{1 + K K_m}{K} s + 1}$$
   
El *overshoot* de este sistema debe valer 0.2, por lo tanto:

$$\mathrm{Overshoot} = 0.2 = \exp \left( \frac{- \pi \zeta}{\sqrt{1 - \zeta^2}}
   \right) = \frac{A}{B}$$
   
Resolviendo la ecuación se encuentra que el coeficiente de amortiguamiento es:

$$\zeta = 0.4559$$

El valor máximo de un sistema de segundo orden subamortiguado para una entrada en escalón unidad $\left( R (s) = \frac{1}{s} \right)$ es:

$$Y_{\max} = A + B$$

donde $B$ es el valor estacionario de la respuesta. En este caso:

$$B = \lim_{t \to \infty} Y (t) = \lim_{s \to 0} s \frac{Y (s)}{R (s)}  \frac{1}{s} = 1$$
   
Por tanto, $A = 0.2$ y $Y_{\max} = 1.2$.

La respuesta de un sistema de segundo orden subamortiguado para una
entrada en escalón es:

$$\frac{y (t)}{k M} = 1 - \frac{1}{\sqrt{1 - \zeta^2}} e^{- \frac{\zeta t}{\tau}} \sin \left( \sqrt{1 - \zeta^2}  \frac{t}{\tau} - \mathrm{atan} \frac{\sqrt{1 - \zeta^2}}{\zeta} \right)$$

donde $k$ es la ganancia global del proceso, es este caso 1. $M$ es la
altura del escalón ($M = 1$). La respuesta máxima se tiene que producir
cuando $t = 1 s$. Sustituyendo:

$$Y_{\max} (t = 1 s) = 1.2 = 1 - \frac{1}{0.89} e^{- \frac{0.4559}{\tau}} \sin \left( \frac{0.89}{\tau} + 1.0974 \right)$$
   
Resolviendo la ecuación se obtiene:

$$\tau = 0.285$$

A partir de la función de transferencia del sistema (de segundo orden) se encuentra:

$$\begin{aligned}
  \tau &= \sqrt{\frac{1}{K}}\\
  2 \zeta \tau &= \frac{1 + K K_m}{K}
\end{aligned}$$
  
Sustituyendo y operando se encuentra: 

$$\begin{aligned}
  K &= 12.31 \\
  K_m &= 0.179
\end{aligned}$$
