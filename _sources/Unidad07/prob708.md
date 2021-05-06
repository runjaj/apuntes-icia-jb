# Problema 7.8

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

En muchas ciudades se han realizado esfuerzos significativos para reciclar los envases de vidrio. En la figura siguiente se representa un diagrama de bloques simplificado del proceso de reciclado de una ciudad:

![prob708.svg](./img/prob708.svg)

El énfasis de la campaña de recolección viene dado por la ganancia $K$. La perturbación $U$ representa los envases que se rompen o se tiran a la basura o a otro lugar no controlado. Suponter $\tau_1 = 1\mathrm{ mes}$ y $\tau_2 = 0.5\mathrm{ mes}$. Determinar:

1. La ganancia $K$ para que es sistema esté crítcamente amortiguado.

2. El _offset_ para una entrada en escalón unidad en la consigna, suponiendo $U(s)=0$. ¿Cuán sería ese _oofset_ para la ganacia del apartado a)?

3. El _offset_ para una pérdida de envases $M$ en escalón, suponiendo que no varía la consigna. ¿Este _offset_ será positivo o negativo?

---

**Solución**

a) La función de transferencia $\frac{C (s)}{R (s)}$ es la siguiente:

$$\frac{C (s)}{R (s)} = \frac{\frac{K}{s + 1}}{1 + \frac{K}{s + 1} 
   \frac{1}{0.5 s + 1}} = \frac{\frac{K (0.5 s + 1)}{1 + K}}{\frac{0.5}{1 + K}
   s^2 + \frac{1.5}{1 + K} s + 1}$$

La constante de tiempo de esta función de transferencia es:

$$\tau = \sqrt[]{\frac{0.5}{1 + K}}$$

Y el coeficiente de amortiguamiento:

$$\zeta = \frac{\frac{1.5}{\sqrt{2}}}{\sqrt{1 + K}}$$

Un sistema está críticamente amortiguado cuando su coeficiente de amoritguamiento es la unidad. Por tanto, de la expresión anterior se obtiene:

$$K = 0.125$$

b) El *offset* será:

$$\mathrm{Offset} = \lim_{t \to \infty} [R (t) - C (t)] =
   \lim_{s \to 0} s [R (t) - C (t)] = \lim_{s \to 0} \left[ s \frac{1}{s} - s \frac{C (s)}{R (s)} \frac{1}{s} \right] = \frac{1}{1 + K}$$
   
Para $K = 0.125$:

$$\mathrm{Offset} = 0.889$$

c) La función de transferencia $\frac{C (s)}{U (s)}$ es:

$$\frac{C (s)}{U (s)} = \frac{1}{1 + \frac{K}{s + 1}  \frac{1}{0.5 s + 1}} =
   \frac{\frac{0.5 s^2 + 1.5 s + 1}{1 + K}}{\frac{0.5}{1 + K} s^2 +
   \frac{1.5}{1 + K} s + 1}$$
   
El *offset* es en este caso:

$$\mathrm{Offset} = \lim_{t \to \infty} [R (t) - C (t)] =
   \lim_{s \to 0} s [R (t) - C (t)] = \lim_{s \to 0} \left[ s 0 - s \frac{C (s)}{U (s)}  \frac{M}{s}
   \right] = - \frac{M}{1 + K}$$
   
Como *M* es un valor negativo (pérdida de envases), el *offset* es positivo, es decir, $R (t) > C (t)$.

 
