# Acción de control integral

El efecto de la acción integral $\left( G_c = K_c  \frac{1}{\tau_I s} \right)$ sobre un lazo de control formado por un proceso de primer orden (el mismo caso que en el apartado anterior) para un cambio en la consigna será:

$$y (s) = \frac{G_c G_p}{1 + G_c G_p} = \frac{K_c  \frac{1}{\tau_I s} 
   \frac{K_p}{\tau_p s + 1}}{1 + K_c  \frac{1}{\tau_I s}  \frac{K_p}{\tau_p s
   + 1}} y_{sp} (s) = \frac{1}{\tau^2 s^2 + 2 \tau \zeta s + 1}
   y_{sp} (s)$$
   
siendo $\tau = \sqrt{\frac{\tau_I \tau_p}{K_p K_c}}$ y $\zeta = \frac{1}{2} \sqrt{\frac{\tau_I}{\tau_p K_p K_c}}$.

Se observa que el lazo de control formado por el proceso de primer orden y la acción integral es un sistema de segundo orden.

En este caso, para un cambio en escalón unidad:

$$\lim_{t \to \infty}y(t) = \lim_{s \to 0}s y(s) = \lim_{s \to 0}s y(s) s \frac{1}{\tau^2 s^2 + 2 \tau \zeta s + 1}  \frac{1}{s}    = 1$$ 
   
Por tanto, el *offset* será igual a 0. La acción de control integral elimina el *offset*.

Si se aumenta la ganancia del controlador $K_c$ o se disminuye el tiempo integral $\tau_I$, disminuye el coeficiente de amortiguamiento $\zeta$. Con el objetivo de eliminar lo más rápidamente posible las perturbaciones o alcanzar el nuevo valor de la consigna, se prefieretrabajar normalmente con coeficientes de amortiguamiento menores que 1. Se logra aumentar la velocidad de la respuesta a expensas de tenerdesviaciones mayores a corto plazo, aparición de *overshoot*, y oscilaciones durante un tiempo mayor.
