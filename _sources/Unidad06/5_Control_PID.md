# Control Proporcional + Integral + Derivativo (PID)

Simplemente es la combinación de las tres acciones de control
anteriores:

$$c (t) = K_c \varepsilon (t) + \frac{K_c}{\tau_I}  \int_0^t \varepsilon (t)
   \mathrm{d}t + K_c \tau_D  \frac{\mathrm{d}\varepsilon (t)}{\mathrm{d}t} + c_s$$
   
y su función de transferencia es:

$$G_c (s) = K_c  \left( 1 + \frac{1}{\tau_I s} + \tau_D s \right)$$

```{tip}
Problema [\[prob:control pid\]](#prob:control pid){reference-type="ref"
reference="prob:control pid"}
```

