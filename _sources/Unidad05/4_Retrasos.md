# Retrasos

Uno de los elemento no lineales más habituales en los procesos
alimentarios es la existencia de retrasos. En el capítulo 7 se estudiará
su influencia en el control de procesos.

Sea el siguiente proceso de primer orden con un retraso:

```{figure} ./img/retraso.svg
---
figclass: margin-caption
---
Diagrama de bloques de un proceso de primer orden con un retraso igual a $t_d$.

```

Para el sistema de primer orden:

$$G_p = \frac{\mathcal{L} [y (t)]}{\mathcal{L} [f (t)]} = \frac{K_p}{\tau_p s
   + 1}$$ 
   
   y para el retraso (ec.
[\[ec:translacion\]](#ec:translacion){reference-type="ref"
reference="ec:translacion"}, propiedad
[\[translacion\]](#translacion){reference-type="ref"
reference="translacion"}, apartado
[\[transformada\]](#transformada){reference-type="ref"
reference="transformada"}):

$$\frac{\mathcal{L} [y (t - t_d)]}{\mathcal{L} [y (t)]} = \mathrm{e}^{- t_d s}$$

donde $t_d$ es el retraso o tiempo muerto.

Por tanto el proceso puede representarse como:

La función de transferencia global para el proceso de primer orden y el
retraso será:

$$\frac{\mathcal{L} [y (t - t_d)]}{\mathcal{L} [f (t)]} = \frac{K_p}{\tau_p s
   + 1} \mathrm{e}^{- t_d s}$$

El cálculo de la transformada inversa de Laplace es sencillo. En este caso lo vamos a realizar utilizando Sympy. En primer lugar cargaremos las bibliotecas que vamos a utilizar, definiremos los símbolos necesarios y las funciones de transferencia del proceso ($G_p$) y del retraso ($G_d$). También calcularemos la función de transferencia $G$, resultado de plantear la serie de bloques formada por el proceso y por el retraso:

```julia
using SymPy, Plots, LaTeXStrings

t, td, K, T, M = symbols("t t_d K tau M", real=true)
s = symbols("s")

Gp = K/(T*s+1)
Gd = exp(-td*s)

G = Gp*Gd
```

La respuesta del proceso de primer orden $y(t)$ es:

```julia
y = sympy.inverse_laplace_transform(Gp*M/s, s, t)
```

La salida tras sufrir el retraso $t_d$ es:

```julia
yd = sympy.inverse_laplace_transform(G*M/s, s, t)
```

El efecto del retraso es muy evidente al representar gráficamente ambas respuestas:

```julia
plot(yd(K=>1, T=>1, td=>1, M=>1), 0, 6, legend=:bottomright, 
    label="Proceso+ Retraso", xlabel=L"\frac{t}{\tau}", ylabel=L"\frac{y(t)}{K M}",
    lw=2)
plot!(y(K=>1, T=>1, M=>1), label="Proceso", lw=2)
```

El retraso se puede simplificar matemáticamente mediante la [aproximación
de Padé](https://es.wikipedia.org/wiki/Aproximación_de_Padé):

$$\mathrm{e}^{- t_d s} \approx \frac{1 - \frac{t_d}{2} s}{1 + \frac{t_d}{2} s}$$
