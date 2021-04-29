# Control proporcional (P)

El acción de control $c$ del controlador proporcional es:

$$c (t) = K_c \varepsilon (t) + c_s$$ (P)

donde $K_c$ es la
ganancia proporcional del controlador y $c_s$ es el *bias* del
controlador.

La ganancia del controlador también se puede expresar mediante la *Banda
proporcional*, expresada como porcentaje:

$$\mathrm{BP} = \frac{100}{K_c}$$ 

Normalmente,
$1 \leqslant \mathrm{BP} \leqslant 500$. La banda
proporcional expresa el intervalo del error para que el control se
sature. Cuanto mayor es $K_c$, menor es BP y mayor es la sensibilidad
del controlador a los cambios o, lo que es lo mismo, al error
$\varepsilon$.

El *bias* del controlador es el valor de la acción de control cuando el
error es nulo.

La función de transferencia del controlador se obtiene realizando la
transformada de Laplace a la ec. {eq}`P`: 

$$G_c (s) = K_c$$ 

teniendo en cuenta que se ha
utilizado como variable de desviación: 

$$c' (t) = c (t) - c_s$$

La acción de control proporcional es la más importante y se encuentra en
todos los sistemas de control.

```{tip}
Problema [\[prob:control p\]](#prob:control p){reference-type="ref"
reference="prob:control p"}
```

