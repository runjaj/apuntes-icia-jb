# Problema 8.7

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

En la figura se representa el diagrama de bloques de un sistema de control de velocidad de un motor de gasolina:

![Lazo de control](./img/prob807.svg)

donde:

$$\begin{align}
G_c &= \frac{1}{\tau_Is+1}\\
G_e &= \frac{K}{\tau_es+1}\\
G_m &= \frac{1}{\tau_ms+1}
\end{align}$$

$\tau_i$ es la constante de tiempo del carburador, igual a 1; $\tau_e$ es la del motor, igual a 4 segundos; y $\tau_m$ es la del medidor de velocidad, igual a 0.5 s. Determinar:

1. El valor de la ganancia $K$ del motor para que, ante una variación $M$ en la consigna, la velocidad obtenida no difiera respecto a la consigna en más de un 7 % de dicha variación $M$.

2. La estabilidad del sistema.

3. El margen de la ganancia $K$ determinada en el primer apartado.

---

**Solución**

a) En este apartado se propone un cambio en la consigna consistente en un escalón de altura *M*:

$$R (s) = \frac{M}{s}$$

La función de transferencia que describe la dinámica de este lazo de control para un cambio en la consigna es:

$$G (s) = \frac{C (s)}{R (s)} = \frac{\frac{1}{s + 1}  \frac{K}{4s + 1}}{1 + \frac{1}{s + 1}  \frac{K}{4 s + 1}  \frac{1}{0.5 s + 1}} = \frac{Ks + 2 K}{4 s^3 + 13 s^2 + 11 s + 2 K + 2}$$

La velocidad estacionaria obtenida será:

$$\lim_{s \to 0} [s G (s) R (s)] = \lim_{s \to 0}  \left[ s \frac{Ks + 2 K}{4 s^3 + 13 s^2 + 11 s + 2 K + 2} \frac{M}{s} \right] = \frac{KM}{K + 1}$$

Se desea que la diferencia entre la velocidad obtenida y la deseada no difiera en más de un 7% de $M$. En este caso se considerará el caso límite de que la diferencia sea de un 7% de $M$. Por tanto:

$$\frac{KM}{K + 1} = (1 - 0.07) M$$

Es decir,

$$K = 13.28$$
   
b) Para determinar la estabilidad del sistema se puede recurrir al método de Routh-Hurvitz ya que el sistema es lineal. La ecuación característica de este lazo de control se puede obtener a partir del denominador de la ec. {eq}`ec8.1` y es:

$$4 s^3 + 13 s^2 + 11 s + 2 K + 2 = 0$$

También se puede obtener la ecuación característica a partir de:

$$1 + G_{\mathrm{OL}} = 1 + \frac{1}{s + 1}  \frac{K}{4 s + 1}  \frac{1}{0.5 s + 1} = 0$$
   
Una vez encontrada la ecuación característica hay que construir la matriz de Routh-Hurvitz:

$$\left(\begin{array}{cc}
     4 & 11\\
     13 & 2 K + 2\\
     \frac{13 \cdot 11 - 4 (2 K + 2)}{13} = - \frac{8 K - 135}{11} & 
\end{array}\right)$$

Por tanto, el lazo de control será estable si:

$$- \frac{8 K - 135}{11} \geqslant 0$$

Resolviendo la inecuación se encuentra que el lazo de control será estable si:

$$K \leqslant \frac{135}{8} = 16.875$$

c) La ganancia límite $K_u$ para la que el lazo de control todavía es estable es:

$$K_u = 16.875$$

Por tanto, el margen de la ganancia $K$ será:

$$\mathrm{MG} = \frac{K_u}{K} = \frac{16.875}{13.28} = 1.271$$

Lo que significa que la ganancia $K$ puede aumentar hasta un 27.1% y el lazo de control continuará siendo estable.

 
