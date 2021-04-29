# Control Proporcional + Derivativo (PD)

Se define como:

$$c (s) = K_c \varepsilon (t) + K_c \tau_D  \frac{\mathrm{d}\varepsilon
   (t)}{\mathrm{d}t} + c_s$$
   
donde $\tau_D$ es la constante de tiempo
derivativa. La acción de control derivativa aplica una acción de control
proporcional a la velocidad de cambio del error. En cierta manera se
anticipa al error futuro, por ello se la conoce a veces como control
anticipativo. En lugar de la constante de tiempo derivativa se utiliza a
veces la ganancia derivativa $K_D$ que es $K_c
\tau_D$.

Presenta el problema de que puede tomar acciones de control derivativas
intensas para sistemas con ruido pero con un error próximo a cero, lo
que implica que la acción de control no es necesario. Este problema se
puede solucionar añadiendo algún sistema de filtrado que elimine o
minimice el ruido.

Su función de transferencia es: 

$$G_c (s) = K_c  (1 + \tau_D s)$$

```{tip}
Problema [\[prob:control pd\]](#prob:control pd){reference-type="ref"
reference="prob:control pd"}
```
