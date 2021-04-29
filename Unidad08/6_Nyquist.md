<!-- #region -->
# Criterio de estabilidad de Nyquist

El criterio de estabilidad de Nyquist es una alternativa a los diagramas de Bode para realizar el análisis de estabilidad de procesos. El diagrama de Nyquist contiene la misma información que los de Bode, por lo que su construcción es sencilla a partir de éstos, pero puede tratar sistemas para los que no es aplicable el criterio de estabilidad de Bode.

```{figure} ./img/bode_no.svg
---
name: bode_no
figclass: margin-caption
---
Sistemas para los que el criterio de estabilidad de Bode no es aplicable.
```

Para dibujar el diagrama de Nyquist se representa $\mathrm{Im}[G (\mathrm{i}\omega)]$ en ordenadas y $\mathrm{Re}[G (\mathrm{i}\omega)]$ en abscisas.

```{figure} ./img/nyquist.svg
---
name: nyquist
figclass: margin-caption
---
Curva de Nyquist de un proceso. El punto _1_ viene definido por una frecuencia $\omega$.
```

Para el punto *1* de la {numref}`nyquist`, definido por su frecuencia $\omega_1$, se
puede observar que:

1.  La distancia entre el punto *1* y el (0,0) es:

    $$\mathrm{distancia} = \sqrt{\{\mathrm{Re}[G (\mathrm{i}\omega)]\}^2 + \{\mathrm{Im}[G (\mathrm{i}\omega)]\}^2} = |G(\mathrm{i}\omega)| = \mathrm{Re}$$

2.  El ángulo $\varphi$ de la figura es el desfase para la frecuencia $\omega_1$:

    $$\varphi = \mathrm{atan}\frac{\mathrm{Im} [G (\mathrm{i}\omega)]}{\mathrm{Re}[G(\mathrm{i}\omega)]} = \arg G
    (\mathrm{i}\omega) = \mathrm{desfase}$$

Para trazar el diagrama de Nyquist se debe variar la frecuencia entre 0 y $\infty$ para encontrar la RA y $\varphi$ y, a continuación, representarlos en el plano complejo. Una vez trazado el diagrama se aplica el *criterio de estabilidad de Nyquist* ({numref}`crit_nyquist`):

> Si la curva de Nyquist de lazo abierto de un sistema de retroalimentación envuelve el punto (-1,0) para frecuencias $\omega$ desde $- \infty$ hasta $\infty$, la respuesta de lazo cerrado será inestable.

```{figure} ./img/crit_nyquist.svg
---
name: crit_nyquist
figclass: margin-caption
---
Curva de Nyquist para dos lazos abiertos. a) Sistema estable, b) Sistema inestable.
```

El diagrama de Nyquist se puede construir a partir del diagrama de Bode. Ambos diagramas contienen la misma información. El margen de fase y el margen de ganancia también se pueden evaluar en el diagrama de Nyquist.

```{figure} ./img/margenes_nyq.svg
---
name: margenes_nyquist
figclass: margin-caption
---
Obtención del margen de ganancia y de fase a partir de la curva de Nyquist.
```


El punto *A* de la {numref}`margenes_nyquist` es aquel cuya frecuencia hace que RA sea 1, de manera que $\varphi_{MF}$ representa el margen de fases. El punto $B$ tiene un desfase de -180º, de manera que su RA es $M$. Por tanto, el margen de ganancias es $\frac{1}{M}$.
<!-- #endregion -->
