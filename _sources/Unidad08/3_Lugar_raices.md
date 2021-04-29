# Método del lugar de las raíces

Representando las raíces de la ecuación característica en el plano complejo es posible deducir el comportamiento de un sistema según su posición:

```{figure} ./img/lugar_raices.svg
---
name: lugar_raices
figclass: margin-caption
---
Situación en el plano complejo de diferentes raíces de la ecuación característica: a) Respuesta sobreamortiguada o críticamente amortiguada, b) límite de estabilidad y c) sistema inestable.
```

1.  Si todas las raíces están en el semiplano negativo de $s$, el sistema es estable

2.  Si todas las raíces se encuentran en el eje real negativo (las raíces son números reales), el sistema está sobramortiguado o críticamente amortiguado

3.  Cuanto más alejadas del origen de coordenadas estén las raíces situadas en el eje negativo, más rápida será la dinámica del sistema (menor será la constante de tiempo)

4.  Las raíces más cercanas al eje imaginario dominarán la dinámica de la respuesta mientras que aquellas que estén más alejadas dejarán de influir en la respuesta rápidamente

5.  Cuanto más alejadas se encuentren las raíces conjugadas del eje real, más subamortiguado estará el sistema

Con esta información es posible plantear una técnica para estudiar la dinámica de un sistema a partir de su ecuación característica. Esta técnica es el lugar de las raíces, se basa en representar las raíces de la ecuación característica variando la ganancia del controlador entre cero e infinito. La abscisa es la parte real de las raíces y la ordenada es la parte compleja.

```{admonition} Ejemplo
En la primera parte del problema [\[prob810\]](#prob810){reference-type="ref" reference="prob810"} se estudia la estabilidad de un bucle de control mediante la localización de las raíces de la ecuación característica.
```

Representar las raíces de la ecuación característica para un sistema de primer o segundo orden es sencillo ya que se pueden obtener ecuaciones analíticas que relacionan la posición de las raíces con la ganancia del controlador. Para sistemas de orden superior es más complejo, como consecuencia se han desarrollado métodos gráficos y métodos numéricos para facilitar esta tarea.

Frecuentemente, la función de transferencia de lazo abierto generalizada ($G_c G_f G_p G_m$) se puede escribir como un producto de ganancias $K$ por una fracción de polinomios $z(s)$ y $p(s)$. Buscando los ceros de cada uno de estos polinomios, se puede escribir:

$$G_c G_f G_p G_m = K \frac{z (s)}{p (s)} = K \frac{(s - z_1) (s - z_2)
   \ldots (s - z_m)}{(s - p_1) (s - p_2) \ldots (s - p_n)}$$
   
   donde $z_i$ son los zeros y $p_i$ son los polos de la función de lazo abierto ($G_c G_f G_p G_m$).

Para representar las raíces de la ecuación característica según la ganancia del controlador se pueden utilizar las siguientes reglas:

1.  La representación de las raíces empieza ($K_c = 0$) en los polos de la función de transferencia de lazo abierto ($G_c G_f G_p G_m$)

2.  La curva finaliza ($K_c = \infty$) en los ceros de $G_c G_f G_p G_m$. Si hay más polos que ceros, la curva tiende a infinito

3.  El número de curvas es igual al orden del sistema y al de polos de $G_c G_f G_p G_m$

4.  Las partes complejas de la curva siempre aparecen como complejos conjugados

5.  El ángulo de las asíntotas de las curvas es igual a $\frac{\pm180^{\circ}}{n - m}$ donde $n$ es el número de polos de la función de transferencia de lazo abierto y $m$ es el número de ceros
