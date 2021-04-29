(ejemplo_dinamica)=
# Un ejemplo de dinámica de un sistema. ¿Qué se desea conocer?

Como ejemplo se considera un sistema dinámico de nivel. En este caso se
pretende encontrar el comportamiento con el tiempo de un depósito en
función del caudal de entrada. Para ello habrá que buscar un modelo
matemático que describa dicho comportamiento. Se recomienda seguir el
siguiente procedimiento:

1.  Se realiza el *diagrama de flujo del sistema*: En ese diagrama se
    marcan todas las variables implicadas. En este caso se trata de un
    depósito que se descarga por gravedad. Las variables implicadas son:

    -   Sección del depósito: $A(t)$

    -   Resistencia de la tubería al paso del fluido: $R$

    -   Caudales volumétricos de entrada y salida: $q_1 (t)$ y $q_2 (t)$

    -   Nivel del depósito: $h(t)$

    -   Densidad del fluido: $\rho (t)$
    
    ```{figure} ./img/deposito.svg
    ---
    width: 300px
    figclass: margin-caption
    ---
    El nivel del depósito depende de los caudales de entrada y salida del mismo.
    ```

2.  Planteamiento del *modelo matemático*: Un modelo matemático es un
    conjunto de ecuaciones que relacionan entre sí las variables del
    sistema. Se basan en ecuaciones de estado, leyes de equilibrio,
    ecuaciones cinéticas y balances de materia, energía y cantidad de
    movimiento.

    Para el ejemplo, al aplicar el Balance Macroscópico de Materia:
    
    ```{math}
    :label: BMM
    \frac{d A (t) h (t) \rho (t)}{d t} = \rho (t) q_1 (t) - \rho(t) q_2 (t)
    ```
        
    En el momento de plantear el modelo matemático hay
    que explicitar todas las hipótesis o simplificaciones realizadas. En
    este caso se han realizado las siguientes suposiciones:

    -   La densidad ($\rho$) y el area del depósito ($A$) son constantes
        e independientes del tiempo.

    -   El caudal de salida del depósito depende del nivel y de la
        resistencia de la tubería al paso del fluido de este modo:
        $q_2 (t) =
            \frac{h (t)}{R}$.

    Teniendo en cuenta las hipótesis anteriores la ec. {eq}`BMM` queda como:
        
    $$\label{BMMh} A \frac{d h}{d t} = q_1 (t) - \frac{h (t)}{R}$$

3.  Definición de las *variables de desviación*: Debido a que lo
    realmente importante en control es conocer cuánto se ha desplazado
    el sistema respecto al estado estacionario se definen unas variables
    de desviación.

    Para el ejemplo, el balance macroscópico de materia en estado
    estacionario es: 
    
    ```{math}
    :label: BMMe
    0 = q_{1 e} - \frac{h_e}{R}
    ```
   
    donde
    $_e$ indica estado estacionario.

    Restando ambos balances macroscópicos de materia (ecs. {eq}`BMM` y {eq}`BMMe`):

    ```{math}
    :label: BMMd
    A \frac{d (h (t) - h_e)}{d t} = q_1 (t) - q_{1 e} - \frac{h(t) - h_e}{R}
    ``` 
        
    Se definen las siguientes variables de
    desviación:
        
    $$\begin{aligned}
        H (t) &\equiv h (t) - h_e & \\
        Q_1 (t) &\equiv q_1 (t) - q_{1 e}
    \end{aligned}$$
    
     Las mayúsculas indican que se tratan de variables
    de desviación.

    Sustituyendo en la ec. {eq}`BMMd` se obtiene:
        
    ```{math}
    :label: ODE 
    A \frac{d H (t)}{d t} = Q_1 (t) - \frac{H (t)}{R}
    ```
    
    Esta ecuación es el modelo matemático que representa la respuesta
    dinámica del tanque a cambios en el caudal de entrada. Resolviendo
    esta ecuación diferencial se puede saber cómo varía el nivel con el
    tiempo según cambia el caudal de entrada.

