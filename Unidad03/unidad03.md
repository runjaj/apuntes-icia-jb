Cómo abordar la dinámica de un sistema
======================================

Un ejemplo de dinámica de un sistema. Qué se desea conocer?
-----------------------------------------------------------

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

(transformada)=
La transformada de Laplace como herramienta útil
------------------------------------------------

La transformada de Laplace $\bar{f} (s)$ de una función $f (t)$ se
define como:

$$\mathcal{L} [f (t)] \equiv \bar{f} (s) = \int_0^{\infty} f (t) e^{- s t} d
   t$$ 

donde $t \in \mathbb{R}$ y $s \in \mathbb{C}$.

El uso de transformadas de Laplace ofrece un método simple y elegante de
resolver ecuaciones diferenciales como las que se obtienen en los
modelos matemáticos de los procesos alimentarios.

Entre las diferentes propiedades de las transformadas de Laplace cabe
destacar:

1.  Es un operador lineal:

    $$\mathcal{L} [a_1 f_1 (t) + a_2 f_2 (t)] = a_1 \mathcal{L} [f_1 (t)] + a_2
         \mathcal{L} [f_2 (t)]$$

2.  La transformada de una derivada es:

    $$\mathcal{L} \left[ \frac{d f (t)}{d t} \right] = s \bar{f} (s) - f (0)$$
    
    Es importante resaltar que una ecuación diferencial ordinaria de
    primer orden pasa a ser una ecuación lineal de primer grado.

    La transformada de la segunda derivada es:
        
    $$\mathcal{L} \left[ \frac{d^2 f (t)}{d t^2} \right] = s^2  \bar{f} (s) - s
         f (0) - f' (0)$$ 
    
    Generalizando:
    
    $$\mathcal{L} \left[ \frac{d^{(n)} f (t)}{d t^n} \right] = s^n  \bar{f} (s)
         - s^{n - 1} f (0) - s^{n - 2} f' (0) - \ldots - s f^{(n - 2)} (0) - f^{(n
         - 1)} (0)$$

    Esta propiedad permite resolver de manera sencilla ecuaciones
    diferenciales ya que las convierte en ecuaciones algebraicas. El
    Problema 2.3 muestra cómo se puede utilizar la transformada de
    Laplace para resolver una ecuación diferencial.

3.  La transformada de Laplace de una integral es:

    $$\mathcal{L} \left[ \int_0^t f (t) d t \right] = \frac{1}{s} \bar{f} (s)$$

4.  (translacion)= Translación de la transformada:

    $$\mathcal{L} [e^{- \alpha t} f (t)] = \bar{f} (\alpha + s)$$
    
    Translación de la función:
        
    ```{math}
    :label: translacion
    \mathcal{L} [f (t - t_0)] = e^{- t_0 s}  \bar{f}(s)
    ```

5.  Teorema del valor final:

    ```{math}
    :label: valor_final
    \mathcal{L} \left[ \underset{t \rightarrow \infty}{\lim} f (t) \right] = \underset{s \rightarrow 0}{\lim} [s \bar{f}(s)]
    ```

```{admonition} Ejemplo
La aplicación de la transformada de Laplace a una función es sencilla
disponiendo de las tablas de transformadas de Laplace y del conocimiento
de las propiedades anteriores. En el Problema 2.1 se muestra cómo se
aplica.
```

La función de transferencia. Álgebra de funciones de transferencia
------------------------------------------------------------------

Para un proceso sencillo, como el del nivel del depósito, se puede
plantear un esquema sencillo que describa en cierta medida al sistema:

Para el ejemplo del nivel del depósito, $f (t) = Q_1 (t)$ y $y (t) = H
(t)$. Es decir, en este caso el depósito es el proceso, la salida es la
variación del nivel del depósito y la entrada al proceso es el caudal de
entrada.

En el caso de trabajar utilizando las transformadas de Laplace de las
funciones de entrada y salida, se puede representar la dinámica del
proceso mediante el uso de la *función de transferencia*. La función de
transferencia $G (s)$ liga la entrada y la salida del sistema:

$$G (s) = \frac{\mathcal{L} [y (t)]}{\mathcal{L} [f (t)]} = \frac{\bar{y}
   (s)}{\bar{f} (t)}$$ 
   
donde $\bar{y} (s)$ es la transformada de Laplace
de la respuesta del proceso definida utilizando variables de desviación
y $\bar{f} (s)$ es la transformada de la función de desviación de la
entrada.

Para obtener la función de transferencia del ejemplo se realiza la
transformada de Laplace de la ecuación diferencial
{eq}`ODE`:

$$\mathcal{L} \left[ A \frac{d H (t)}{d t} \right] =\mathcal{L} \left[ Q_1
   (t) - \frac{H (t)}{R} \right]$$ 
   
Se realizan las transformadas
considerando que el operador es lineal y conociendo la transformada de
una derivada:

$$A s \bar{H} (s) = \overline{Q_1} (s) - \frac{\bar{H} (s)}{R}$$

Se
supone que para $t = 0$ el sistema está todavía en estado estacionario,
las variables de desviación son nulas.

Operando la ecuación anterior para encontrar la función de
transferencia:

$$G (s) = \frac{\bar{H} (s)}{\overline{Q_1} (s)} = \frac{R}{R A s + 1}$$

Este es la función de transferencia típica de un sistema de primer
orden.

Para los procesos más complicados, con diagramas de bloques más
complejos, se recurre al álgebra de funciones de transferencia.

En el caso de tener un conjunto de procesos en paralelo, es decir, para
un diagrama de bloques en paralelo, se puede obtener una función de
transferencia equivalente:

$$G (s) = \frac{Y (s)}{X (s)} = \frac{Y_1 (s) + Y_2 (s) + Y_3 (s)}{X (s)} =
   G_1 (s) + G_2 (s) + G_3 (s)$$

Generalizando: $$G (s) = \sum_i G_i (s)$$ Para un diagrama de bloques en
serie:

$$G (s) = \frac{X_n}{X_0} = \frac{X_1}{X_0}  \frac{X_2}{X_1} \cdots
   \frac{X_n}{X_{n - 1}} = G_1 G_2 \ldots G_n$$

Generalizando:

$$\label{ec:serie} G (s) = \prod_i G_i (s)$$

```{admonition} Ejemplo
El problema 3.6 muestra un ejemplo de sistema en serie. Se trata de dos
depósitos de almacenamiento en serie. La curiosidad es que se plantea el
sistema con interacción (el mostrado en la figura
[\[fig:serie\]](#fig:serie){reference-type="ref" reference="fig:serie"})
y el sistema de tanques sin interacción, para el que no es aplicable de
manera directa la ecuación
[\[ec:serie\]](#ec:serie){reference-type="ref" reference="ec:serie"}.
```

Transformadas de algunas funciones singulares
---------------------------------------------

A continuación se muestran las transformadas de algunas funciones con
las que se trabajará frecuentemente más adelante ya que pueden ser
asimiladas como las perturbaciones más frecuentes.

Si no se dice lo contrario todas estas funciones se definen para que su
valor sea nulo a tiempo menor que cero.

### Función escalón

Es una función cuyo valor para tiempos menores que cero es nulo y que
alcanza el valor $M$ para tiempo mayores que 0:

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M & t > 0
   \end{array}\right.$$

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \frac{M}{s}$$

Si $M$ es igual a 1 se tiene la función escalón unidad, $U(t)$.

En el caso de que la función tenga un retraso $t_0$:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < t_0\\
     M & t > t_0
   \end{array}\right.$$

O lo que es lo mismo:

$$f (t - t_0) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M & t > 0
   \end{array}\right.$$

Por tanto, aplicando la propiedad número
[\[translacion\]](#translacion){reference-type="ref"
reference="translacion"} (ecuación
[\[ec:translacion\]](#ec:translacion){reference-type="ref"
reference="ec:translacion"}), la transformada de Laplace será:

$$\mathcal{L} [f (t - t_0)] = \frac{M}{s} \mathrm{e}^{- s t_0}$$

### Función pulso

Se trata de una función pulso con área $A = M t_0$:

La función pulso se define como:

$$f (t) = \left\{\begin{array}{cc}
     0 & t < 0\\
     M & 0 < t < t_0\\
     0 & t > t_0
   \end{array}\right.$$

Utilizando la definición del escalón unidad también se puede escribir
como:

$$f (t) = M [U (t) - U (t - t_0)]$$

Por tanto, la transformada de Laplace será:

$$\mathcal{L} [f (t)] = \bar{f} (s) = M \left( \frac{1}{s} - \frac{\mathrm{e}^{-
   s t_0}}{s} \right) = \frac{M}{s}  (1 - \mathrm{e}^{- s t_0})$$

### Función impulso

Se trata de un pulso tal que $M \rightarrow \infty$ y
$t_0 \rightarrow 0$:

La transformada de Laplace de esta función es:

$$\mathcal{L} [f (t)] = \bar{f} (s) = A$$

En el caso particular de que el área sea 1 se habla de la función delta
de Dirac $\delta (t)$.

Se puede comprobar fácilmente que el impulso es la derivada de la
función escalón.

```{admonition} Ejemplo
En el Problema 3.4 se puede comprobar las diferencias y similitudes en
la respuesta de un proceso a una entrada en escalón y en impulso.
```

### Función rampa

Se trata de una función lineal de pendiente *M*:

Esta función se define como:

$$f (t) = \left\{\begin{array}{ll}
     0 & t < 0\\
     M t & t > 0
   \end{array}\right. = M t U (t)$$

La transformada de Laplace es:

$$\mathcal{L} [M t U (t)] = \frac{M}{s^2}$$

### Funciones trigonométricas

La función seno es:

Se define la función como:

$$f (t) = \left\{\begin{array}{cl}
     0 & t < 0\\
     M \sin (\omega t) & t > 0
   \end{array}\right. = M U (t) \sin (\omega t)$$
   
donde $M$ es la amplitud y $\omega$ es la frecuencia angular, expresada
normalmente como rad/s.

La transformada de Laplace de la función seno es:

$$\mathcal{L} [M \sin (\omega t)] = \frac{M \omega}{s^2 + \omega^2}$$

y la de la función coseno:

$$\mathcal{L} [M \cos (\omega t)] = \frac{M s}{s^2 + \omega^2}$$

Inversión de transformadas. De vuelta al tiempo real
----------------------------------------------------

Continuando con el ejemplo se estudiará la salida del sistema para una
entrada de tipo escalón unidad:

$$\bar{H} (s) = \left[ \frac{R}{R A s + 1} \right]  \overline{Q_1} (s) =
   \left[ \frac{R}{R A s + 1} \right]  \frac{1}{s}$$

Mediante el operador transformada inversa de Laplace
($\mathcal{L}^{- 1}$) se obtiene la salida en tiempo real. Para ello hay
que descomponer la función a invertir en partes asimilables a las que se
encuentran en las tablas de transformadas de Laplace (apartado
[1.7](#sec:transformadas){reference-type="ref"
reference="sec:transformadas"}):

$$\bar{H} (s) = \left[ \frac{R}{R A s + 1} \right]  \frac{1}{s} = \frac{a}{s}
   + \frac{b}{s + \frac{1}{A R}}$$

Donde *a* y *b* son dos variables a
determinar. Obviamente, $a =
R$ y $b = - R$. Por tanto,

$$\bar{H} (s) = \left[ R - R \mathrm{e}^{- \frac{t}{R A}} \right] U (t) = R U (t)
   \left[ 1 - \mathrm{e}^{- \frac{t}{R A}} \right] = R U (t)  \left[ 1 - \mathrm{e}^{-
   \frac{t}{\tau}} \right]$$
   
donde $\tau = R A$ es la constante de
tiempo y tiene dimensiones de tiempo.

Cuanto mayor es $\tau$ más lenta es la respuesta, más tarda el sistema en alcanzar el estado estacionario. Se comprueba
que cuanto menor es la sección del tanque más rápida es la respuesta. Si
$\tau$ es grande se dice que el sistema presenta una gran inercia.

La técnica propuesta en este capítulo para obtener modelos matemáticos
se puede utilizar para modelos de mayor complejidad, como el que se
obtiene en la resolución del problema 3.7.

Expansión en fracciones parciales
---------------------------------

Un método de inversión de transformadas de Laplace es la expansión en
fracciones parciales. Para invertir la función $\bar{f} (s)$ se reordena
como una suma de funciones simples:

$$\bar{f} (s) = \overline{f_1} (s) + \overline{f_2} (s) + \ldots +
   \overline{f_s} (s)$$

Una vez realizada la descomposición se realiza la inversión de
transformadas:

$$f (t) =\mathcal{L}^{- 1} [\overline{f_1} (s)] +\mathcal{L}^{- 1}
   [\overline{f_2} (s)] + \ldots +\mathcal{L}^{- 1} [\overline{f_s} (s)]$$

Normalmente las funciones a invertir en control de procesos aparecen
como fracciones de polinomios en *s* del tipo:

$$\bar{f} (s) = \frac{\bar{z} (s)}{\bar{p} (s)}$$

donde *z(s)* es un
polinomio de orden *m* y *p(s)* es un polinomio de orden *n*.

Para realizar la inversión de la transformada de Laplace se factoriza el
denominador:

$$\bar{f} (s) = \frac{z (s)}{(s - p_1)  (s - p_2) \ldots (s - p_n)}$$

donde $p_i$ son las raíces (ceros) del polinomio *p(s)*.

Si todos los $p_i$ son diferentes, se puede expresar *f(s)* como una
suma de *n* términos:

$$\bar{f} (s) = \frac{A}{s - p_1} + \frac{B}{s - p_2} + \frac{C}{s - p_3} +
   \cdots + \frac{W}{s - p_n}$$

Los numeradores de la ecuación anterior se evalúan de la siguiente
manera: 

$$\begin{aligned}
  & A = \underset{s \rightarrow p_1}{\text{l{\'i}m}} [(s - p_1) \bar{f} (s)]
  & \\
  & B = \underset{s \rightarrow p_2}{\text{l{\'i}m}} [(s - p_2) \bar{f} (s)]
  & \\
  & \vdots & \\
  & W = \underset{s \rightarrow p_n}{\text{l{\'i}m}} [(s - p_n) \bar{f} (s)]
  & \end{aligned}$$

Si existen raíces del denominador de *f(s)* repetidas, de nuevo se
expresa *f(s)* como un producto de fracciones simples. Por ejemplo, en
el caso de que una raíz se repita dos veces:

$$\bar{f} (s) = \frac{z (s)}{(s - p_1)^2  (s - p_3)  (s - p_4) \ldots (s -
   p_n)}$$
   
la descomposición en fracciones simples es:

$$\label{ec:dos raices} \bar{f} (s) = \frac{A}{(s - p_1)^2} + \frac{B}{s -
  p_1} + \frac{C}{s - p_3} + \cdots + \frac{W}{s - p_n}$$

Si la raíz se repite 3 veces (orden 3) la expansión sería así:

$$\begin{aligned}
  & \bar{f} (s) = \frac{z (s)}{(s - p_1)^3  (s - p_4)  (s - p_5) \ldots (s -
  p_n)} &  \nonumber\\
  & \label{ec:tres raices} \bar{f} (s) = \frac{A}{(s - p_1)^3} + \frac{B}{(s
  - p_1)^2} + \frac{C}{s - p_1} + \frac{D}{s - p_4} + \cdots + \frac{W}{s -
  p_n} & \end{aligned}$$

Los numeradores de la ecuación
[\[ec:dos raices\]](#ec:dos raices){reference-type="ref"
reference="ec:dos raices"} se calculan de la siguiente manera:

$$\begin{aligned}
  & A = \underset{s \rightarrow p_1}{\text{l{\'i}m}} [(s - p_1)^2  \bar{f}
  (s)] & \\
  & B = \underset{s \rightarrow p_1}{\text{l{\'i}m}} \left\{
  \frac{\mathrm{d}}{\mathrm{d}s} [(s - p_1)^2  \bar{f} (s)] \right\} & \\
  & C = \underset{s \rightarrow p_3}{\text{l{\'i}m}} [(s - p_3) \bar{f} (s)]
  & \\
  & \vdots & \end{aligned}$$ 
  
Para encontrar el numerador *C* de la
ecuación [\[ec:tres raices\]](#ec:tres raices){reference-type="ref"
reference="ec:tres raices"} se debe tomar la segunda derivada.
Generalizando al término $A_j$ de una raíz de orden *N* en $p_1$:

$$A_j = \underset{s \rightarrow p_1}{\text{l{\'i}m}} \left\{ \frac{\mathrm{d}^{m
   - 1}}{\mathrm{d}s^{m - 1}}  [(s - p_1)^N  \bar{f} (s)] \right\}  \frac{1}{(m -
   1) !}$$

Aunque su utilización es un tanto tediosa existen casos, como el
apartado d) del problema 3.2, que muy difícilmente se puede resolver sin
utilizar la técnica de expansión en fracciones parciales. Esta técnica
tiene la ventaja de ser muy sistemática.

(transformadas)=
Transformadas de Laplace
------------------------

```{table} Transformadas de Laplace de funciones seleccionadas.

$\mathbf{f (t), t > 0}$ | $\mathbf{\bar{f}(s)}$
-------------------|------------------
Impulso unidad, $\delta(t_0)$ | 1
Pulso unidad, $\delta_A(t)$ | $\frac{1}{A}  \frac{1 - e^{- sA}}{s}$
Escalón unidad | $\frac{1}{s}$
Rampa, $f(t) = t$ | $\frac{1}{s^2}$
$t^2$ | $\frac{2!}{s^3}$
$t^n$ | $\frac{n!}{s^{n + 1}}$
$e^{- a t}$ | $\frac{1}{s + a}$
$t^n e^{- a t}$ | $\frac{n!}{(s + a)^{n + 1}}$
$\sin (\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$
$\cos (\omega t)$ | $\frac{s}{s^2 + \omega^2}$
$\sinh (\omega t)$ | $\frac{\omega}{s^2 - \omega^2}$
$\cosh (\omega t)$ | $\frac{s}{s^2 - \omega^2}$
$e^{- a t} \sin (\omega t)$ | $\frac{\omega}{(s + a)^2 + \omega^2}$
$e^{- a t} \cos (\omega t)$ | $\frac{s + a}{(s + a)^2 + \omega^2}$
```

```{table} Transformada inversa de Laplace de funciones seleccionadas.
 
  $\mathbf{\bar{f} (s)}$   |   $\mathbf{f (t)}$
  -------------------------|-----------
  $\frac{1}{(s + a)  (s + b)}$                              | $\frac{e^{- a t} - e^{- b t}}{b - a}$
  $\frac{1}{(s + a)  (s + b)  (s + c)}$                     | $\frac{e^{- a t}}{(b - a)  (c - a)} + \frac{e^{- b t}}{(c - b)  (a - b)} + \frac{e^{- a t}}{(a - c)  (b - c)}$
  $\frac{s + a}{(s + b)  (s + c)}$                          | $\frac{1}{c - b}  [(a - b) e^{- b t} -(a - c) e^{- c t}]$
  $\frac{a}{(s + b)^2}$                                     | $a t e^{- b t}$
  $\frac{a}{(s + b)^3}$                                     | $\frac{a}{2} t^2 e^{- b t}$
  $\frac{a}{(s + b)^{n + 1}}$                               | $\frac{a}{n!} t^n b^{- b t}$
  $\frac{1}{s (a s + 1)}$                                   | $1 - e^{- t / a}$
  $\frac{1}{s (a s + 1)^2}$                                 | $1 - \frac{a + t}{a} e^{- t / a}$
  $\frac{\omega^2}{s (s^2 + 2 \zeta \omega s + \omega^2)}$  | $1 + \frac{e^{-\zeta \omega t}}{ \sqrt[]{1 - \zeta^2}} \sin \left( \omega \sqrt[]{1- \zeta^2} t - \varphi \right)$ donde $\cos \varphi = - \zeta$
  $\frac{s}{(1 + a s)  (s^2 + \omega^2)}$                   | $- \frac{1}{1 + a^2 \omega^2}e^{- t / a} + \frac{1}{\sqrt[]{1 + a^2 \omega^2}} \cos (\omega t +\varphi)$ donde $\varphi = \arctan (a \omega)$
  $\frac{s}{(s^2 + \omega^2)^2}$                            | $\frac{1}{2 \omega} \sin (\omega t)$
  $\frac{1}{(s + a)  [(s + b)^2 + \omega^2]}$               | $\frac{e^{- a t}}{(a - b)^2+ \omega^2} + \frac{e^{- b t} \sin (\omega t + \varphi)}{\omega\sqrt[]{(a - b)^2 + \omega^2}}$ donde $\varphi = \arctan \left(\frac{\omega}{a - b} \right)$
```
