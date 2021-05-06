# Problema 7.6
 
<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

Uno de los problemas más importantes con el que se enfrentan los ingenieros es el empleo óptmio de las fuentes de energía. Muchos ingenieros trabajan hoy en día en sistemas de energía solar para calefacción doméstica. Uno de esos sistemas emplea colectores solares y almacenamiento térmico, tal como se indica en el diagrama superior de la figura adjunta. El diagrama de bloques del sistema de control se presenta en la parte inferior de la figura:

![prob706a.svg](./img/prob706a.svg)
![prob706b.svg](./img/prob706b.svg)

La dinámica de los colectores, el almacenamiento térmico y la propia casa viene dada por $G(s) = \frac{k_1}{s^2}$. La dinámica de los instrumentos de medida viene determinada por $H(s) = \frac{k_2}{\tau_1s + 1}$ . Suponer que $\tau_1 = 1 \mathrm{ s}$ y $\tau_2 = 0$ (aproximación).
 
1. ¿Para qué valores de $k = k_1 k_2$ el sistema será subamortiguado y para cuáles sobreamortiguado?

2. ¿Para qué valores de $k$ la temperatura de la casa, al variar la consigna, no discrepará en ningún momento más de un 5 % del nuevo valor estacionario a alcanzar?

3. Suponer que la temperatura de la casa está estabilizada en 22 ℃. Si la consigna se cambia de pronto a 24 ℃, siendo $k_2 = 1.1$, ¿qué temperatura se alcanzará en la casa?

---

**Solución**

a) La función de transferencia entre la temperatura de la casa (salida del lazo de retroalimentación) y la temperatura deseada (entrada a la lazo) es:

$$\frac{Y (s)}{R (s)} = \frac{G (s)}{1 + G (s) H (s)} =
   \frac{\frac{k_1}{s^2}}{1 + \frac{k_1}{s^2} k_2 (s + 1)} =
   \frac{\frac{1}{k_2}}{\frac{1}{k} s^2 + s + 1}$$
   
donde $k = k_1 k_2$.

Al tratarse de un sistema de segundo orden:

$$\begin{aligned}
  \tau &= \sqrt{\frac{1}{k}} \\
  2 \tau \zeta &= 1
\end{aligned}$$

donde $\tau$ es la constante de tiempo del lazo de control y $\zeta$ es el coeficiente de amortiguamiento. Despejando se encuentra:

$$k = (2 \zeta)^2$$

Por tanto,

$$\begin{aligned}
  & \zeta > 1 \rightarrow k > 4 & \text{Sobreamortiguado}\\
  & \zeta = 1 \rightarrow k = 4 & \text{Criticamente amortiguado}\\
  & \zeta < 1 \rightarrow k < 4 & \text{Subamortiguado}
\end{aligned}$$

b) Un cambio de un 5% del nuevo valor estacionario, tras un cambio en la consigna, es equivalente a un *overshoot* de 0.05. Por tanto,

$$\mathrm{Overshoot} = 0.05 = \exp \left( - \frac{\pi \zeta}{\sqrt{1 - \zeta^2}} \right)$$
   
Al resolver la ecuación se encuentra que:

$$\zeta = 0.6901$$

Como se dice que el cambio no debe superar el 5% del
valor estacionario:

$$k \geqslant 1.905$$

c) El cambio propuesto en la consigna es una función en escalón de altura 2 °C $\left( R (s) = \frac{2}{s} \right)$. El valor que alcanzará la casa es:

$$\lim_{t \to \infty} Y (t) = \underset{s \rightarrow
   0}{\lim} s Y (s) = \lim_{s \to 0} s \frac{Y (s)}{R (s)} G(s) = \lim_{s \to 0} s \frac{\frac{1}{k_2}}{\frac{1}{k} s^2 + s + 1}  \frac{2}{s} = 1.818$$

El valor anterior no es la temperatura estacionaria que alcanzará la casa que ya la variable $Y (t)$ está definida con variables de desviación. Para obtener la temperatura deseada hay que tener en cuenta que la temperatura en estado estacionario es de 22 °C, lo que significa que:

$$T_{\text{final}} = 22 + 1.818 = 23.8 \text{ ºC}$$
