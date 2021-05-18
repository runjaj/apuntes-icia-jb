# Problema 8.8

<style type="text/css">
   ol { list-style-type: lower-alpha; }
</style>
   
Sea el sistema de control representado en la figura:

![Problema 8.8](./img/prob808.svg)

donde $G_c=K_c$, $G_1=\frac{1}{(\tau_1s+1)(\tau_2s+1)}$ y $G_2=\frac{1}{\tau_3s+1}$.

1. Calcular el _offset_ de la respuesta del sistema si se produce una carga ($U$) en escalón unidad.

2. Si $\tau_1=1$, $\tau_2=\frac{1}{2}$ y $\tau_3=\frac{1}{3}$, ¿para qé valores de ganancia $Kc$ es estable el sistema?

3. Si se sustituyera el control proporcional por un control PI, siendo $K_c=5$ y $\tau_I=0.25$, ¿sería estable el sistema?

---

**Solución**

a) La función de transferencia para un cambio en la carga es:

$$\frac{C}{U} = \frac{G_1}{1 + G_c G_1 G_2} = \frac{\tau_3 s + 1}{(\tau_1 s + 1) (\tau_2 s + 1) (\tau_3 s + 1) + K_c}$$

El *offset* para un cambio en la carga en escalón unidad será:

$$\mathrm{offset} = \lim_{s \to 0} \left( s R - s \frac{C}{U} U \right) = \lim_{s \to 0} \left( s 0 - s \frac{C}{U} \frac{1}{s} \right) = - \frac{1}{1 + K_c}$$

b) La ecuación característica de este lazo de control es:

$$1 + G_c G_1 G_2 = 0$$

Obviamente la parte derecha de la ecuación característica coincide con el denominador de la función de transferencia encontrada en el apartado a). Por tanto,

$$(\tau_1 s + 1) (\tau_2 s + 1) (\tau_3 s + 1) + K_c = 0$$

Sustituyendo se encuentra:

$$0.1667 s^3 + s^2 + 1.833 s + 1 + K_c = 0$$

Para buscar para qué valores de $K_c$ el sistema es estable se puede recurrir al
criterio de Routh-Hurvitz. La matriz de Routh es:

$$\begin{array}{cc}
     0.1667 & 1.833\\
     1 & 1 + K_c\\
     1.666 - 0.1667 K_c & 
\end{array}$$
   
Para que el sistema sea estable:

$$1.666 - 0.1667 K_c > 0$$

Lo que supone que el sistema será estable
para ganancias proporcionales que cumplan la siguiente condición:

$$0 < K_c < 9.994$$

c) Si el controlador propocional se sustituye por un controlador PI con ganancia $K_c = 5$ y $\tau_I = 0.25$, la nueva ecuación característica será:

$$1 + 5 \left( 1 + \frac{1}{0.25 s} \right)  \frac{1}{(\tau_1 s + 1)  (\tau_2
   s + 1)}  \frac{1}{\tau_3 s + 1} = 0$$
   
Sustituyendo y operando se obtiene:

$$4.1667 \cdot 10^{- 2} s^4 + 0.20833 s^3 + 0.375 s^2 + 1.625 s + 5 = 0$$

La matriz de Routh es:

$$\begin{array}{ccc}
     4.1667 \cdot 10^{- 2} & 0.375 & 5\\
     0.20833 & 1.625 & \\
     4.9992 \cdot 10^{- 2} & 5 & \\
     - 19.211 &  & 
\end{array}$$

En la primera columna de la matriz hay un elemento negativo, lo que implica que el nuevo lazo de control es inestable.
