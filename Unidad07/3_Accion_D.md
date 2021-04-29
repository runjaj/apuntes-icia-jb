# Acción de control derivativa

Considerando el mismo lazo de control que en los apartados anteriores con una acción de control derivativa ($G_c = K_c \tau_D s$), se obtiene:

$$y (s) = \frac{K_p K_c \tau_p s}{(\tau_p + K_p K_c \tau_D) s + 1}
   y_{sp} (s)$$

La acción de control derivativa no cambia el orden de la dinámica del sistema. La respuesta del sistema se hace más lenta ya que $\tau_p + K_p K_c \tau_D > \tau_p$.

Para un proceso de segundo orden:

$$y (s) = \frac{K_p K_c \tau_D s}{\tau^2 s^2 + (2 \zeta \tau + K_p K_c
   \tau_D) s + 1} y_{sp}(s)$$

Tampoco cambia el orden de la dinámica del sistema. Además el lazo tiene una respuesta más amortiguada ya que $2 \zeta \tau + K_p K_c \tau_D > 2 \zeta \tau$.

Al disminuir la velocidad de la respuesta y aumentar el amortiguamiento se dice que la acción de control derivativa produce un comportamiento más robusto del sistema controlado.
