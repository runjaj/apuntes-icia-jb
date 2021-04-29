# Control Proporcional + Integral (PI)

En este tipo de controlador la acción de control es:

$$c (t) = K_c \varepsilon (t) + \frac{K_c}{\tau_I}  \int_0^t \varepsilon (t) \mathrm{d}t + c_s$$
   
donde $\tau_I$ es el tiempo integral o tiempo de *reset*. Se suele expresar como minutos por repetición y se suele encontrar entre $0.1 \text{min} \leqslant \tau_I \leqslant 50$min. También se puede expresar como $\frac{1}{\tau_I}$ (repeticiones por minuto) y se conoce como la velocidad de *reset*. $K_c$ es la ganancia del controlador, tal como ocurría con el controlador proporcional. Al conjunto $\frac{K_c}{\tau_I}$, a veces, se le conoce como la ganancia integral $K_I$.

```{figure} ./img/fig06.svg
---
name: fig06
figclass: margin-caption
---
Acción de control (respuesta) de un controlador PI a un cambio en escalón en el error.
```


A $\tau_I$ se le conoce como el tiempo de *reset* porque es el tiempo
necesario para que el controlador repita la acción de control inicial:

$$\frac{K_c}{\tau_I}  \int_0^{\tau_I} \varepsilon \mathrm{d}t =    \frac{K_c}{\tau_I} \varepsilon \tau_I = K_c \varepsilon$$
   
para un error constante con el tiempo, como por ejemplo, el debido a un escalón.

La función de transferencia de este tipo de controladores es:

$$G_c (s) = K_c  \left( 1 + \frac{1}{\tau_I s} \right)$$

El controlador PI actúa mientras exista error en la salida produciendo cada vez valores mayores para la acción integral. Por tanto, se deben tomar acciones especiales para evitar saturaciones en los actuadores
finales para errores persistentes con el tiempo.

````{margin}
```{tip} 
Problema {ref}`prob604`.
```
````