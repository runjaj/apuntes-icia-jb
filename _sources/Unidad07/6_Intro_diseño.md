# Introducción al diseño de sistemas de control por retroalimentación

Una vez decidido qué se va a controlar (variable controlada) y a través de qué (variable manipulable) es necesario llevara a cabo el diseño del controlador. Para ello hay que contestar fundamentalmente a las siguientes preguntas:

1.  *Qué criterio de rendimiento se debe tomar para llevar a cabo la selección y la sintonía del controlador?*

    Existen multitud de criterios para la evaluación del controlador. Por ejemplo:

    -   Mantener la máxima desviación lo menor posible

    -   Lograr tiempos de ajuste cortos

    -   Minimizar la integral de los errores hasta que el proceso alcanza el *set point* deseado

    -   Criterio de la razón de disminución 1/4

2.  *Qué tipo de controlador se debe seleccionar para el proceso a controlar?*

    De manera cualitativa se pueden considerar las siguientes conclusiones:

    I.  Control proporcional

    1.  Acelera la respuesta del proceso controlado

    2.  Produce *offset* para todos los procesos excepto para aquellos con términos $\frac{1}{s}$ en su función de transferencia

    II. Control integral

    1.  Elimina el *offset*

    2.  La eliminación del *offset* causa normalmente unas desviaciones máximas mayores

    3.  Ralentiza el sistema o produce respuestas oscilantes

    4.  Si se aumenta $K_c$ para aumentar la velocidad de la respuesta, el sistema aumenta las oscilaciones y puede pasar a ser inestable

    III. Control derivativo

    1.  Se anticipa a los errores futuros e introduce la acción de control adecuada

    2.  Introduce un efecto estabilizador en la respuesta de ciclo cerrado de los procesos

    Como consecuencia se pueden aplicar los siguientes criterios:

    i.  Si es posible, utilizar un controlador P. Por ejemplo, sistemas de control de presión de gases o nivel de líquidos

    ii. Si el controlador P es inaceptable, utilizar un PI. Se utiliza casi siempre para el control de caudales

    iii. Utilizar un PID para aumentar la velocidad de la respuesta de ciclo cerrado y mantener la estabilidad. P.ej., control de temperatura y concentraciones

3.  *Cómo se pueden seleccionar los mejores valores a los parámetros del controlador (sintonía del controlador)?*

    Esta pregunta se contestará en los capítulos siguientes.

