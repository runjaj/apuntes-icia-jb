# Método del ensayo y error

Para realizar la sintonía experimentalmente se sigue un procedimiento similar al siguiente:

1.  Se pone el controlador en manual y se eliminan las acciones integral y derivativa ($\tau_I \to \infty$ y $\tau_D = 0$)

2.  Fijar la banda proporcional a un valor elevado, por ejemplo, 200 (ganancia proporcional pequeña)

3.  Poner el controlador en automático

4.  Realizar un pequeño cambio en la consigna o en la carga y seguir la respuesta de la variable controlada hasta que se alcance una respuesta estacionaria. Al ser la ganancia tan baja, la respuesta debe ser lenta

5.  Reducir la banda proporcional a la mitad (doblar la ganancia) y realizar un nuevo cambio en la consigna o en la carga

6.  Repetir el paso 5. hasta que la respuesta sea muy subamortiguada y oscilatoria. Esta es la *ganancia última*

7.  Fijar la banda proporcional al doble de su último valor (la mitad de la ganancia proporcional)

8.  Iniciar una acción integral reduciendo el valor de $\tau_I$ a su mitad. Realizar pequeñas perturbaciones o cambios en la consigna y observar el efecto

9.  Encontrar el valor de $\tau_I$ que hace que la dinámica del sistema sea muy subamortiguada y fijar $\tau_I$ al doble de ese valor

10. Aumentar el valor de $\tau_D$ y realizar cambios en la consigna o en la carga. Encontrar el valor de $\tau_D$ que proporciona la mayor acción de control sin amplificar el ruido en el proceso de medida de la señal

11. Reducir el valor de la banda proporcional en pasos de un 10% hasta que se cumplan las especificaciones deseadas

Es importante decir que este método funciona para casi todos los lazos de control pero no funciona con aquellos sistemas que son inestables para ganancias elevadas y para ganancias bajas, es decir, aquellos que solo sean estables para valores de ganancia proporcional intermedios.