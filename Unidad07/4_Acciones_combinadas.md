# Acciones de control combinadas

## Acción de control PI

1.  Aumenta el orden de la respuesta (efecto de la acción I)

2.  Se elimina el *offset* (acción I)

3.  Al aumentar la ganancia del controlador, la respuesta se hace más rápida (acción P y I), más oscilatoria, aumenta el *overshoot* y la razón de disminución (acción I). Valores elevados de $K_c$ pueden hacer al lazo de control inestable

4.  Al disminuir el tiempo integral, para una ganancia del controlador constante, la respuesta se hace más rápida y más oscilatoria, con mayor *overshoot* y razón de disminución (acción I)

## Acción de control PID

La acción derivativa mantiene los beneficios de la acción PI y logra eliminar parte de los defectos. En un controlador PI al aumentar $K_c$, para lograr una respuesta más rápida, la respuesta se vuelve oscilatoria y puede llegar a ser inestable. La introducción de la acción derivativa tiene un efecto estabilizador. Al aumentar $K_c$ se logra una respuesta más rápida manteniendo el *overshoot* prácticamente constante.
