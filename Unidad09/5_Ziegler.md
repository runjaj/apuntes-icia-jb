# Método de Ziegler y Nichols

Al contrario que el método anterior, ésta es una técnica de lazo cerrado. El procedimiento es el siguiente:

1.  Llevar el sistema al nivel de operación deseado, que normalmente corresponderá con las condiciones de diseño

2.  Utilizando solo el control proporcional y con el ciclo cerrado, introducir un cambio en la consigna y variar la ganancia proporcional hasta que el sistema varíe continuamente. La frecuencia de oscilación sostenida es la frecuencia de cruce $\omega_{co}$. La razón de amplitudes de la respuesta en la frecuencia de cruce es $M$

3.  Se calculan las siguientes magnitudes:

    $$\begin{aligned}
        \text{Ganancia última: } & K_u = \frac{1}{M} & \\
        \text{Periodo último de oscilaciones sostenidas: } & P_u = \frac{2
        \pi}{\omega_{co}} & 
      \end{aligned}$$

4.  Ziegler y Nichols recomendaron los siguientes parámetros para controladores por retroalimentación:

    - P:
        
        $$K_c = \frac{K_u}{2}$$
        
    - PI:
        
        $$\begin{align}
            K_c &= \frac{K_u}{2.2}\\
            \tau_I &= \frac{P_u}{1.2}
        \end{align}$$
        
    - PID:
        
        $$\begin{align}
            K_c &= \frac{K_u}{1.7}\\
            \tau_I &= \frac{P_u}{2}\\
            \tau_D &= \frac{P_u}{8}
        \end{align}$$