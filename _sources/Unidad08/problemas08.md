# Tema 8

**Problema 8.1**

Estimar la estabilidad de un sistema de control autimático cuya función de transferencia de lazo abierto es:

$$GH=\frac{9}{(10 s+1)^3$$

**Problema 8.2**

Considérese un proceso de segundo orden cuya función de transferencia es:

$$G_p = \frac{1}{s^2+2s+1}

1. ¿Es estable dicho proceso?

2. Si el proceso se encuentra en un lazo de control, con un controlador PI($K_c=100$, $\tau_I=0.1$), siendo las funciones de trasnferencia de los elementos medidor y final de control $H=G_v=1$, ¿es estable dicho conjunto? (Puede aplicarse el criterio de Routh-Hurvitz)

3. Hacer el análisis de estabilidad de este sistema de lazo de control en función de $K_c$ y$\tau_I$.

**Problema 8.3**

Un sistema tiene una dinámica cuya ecuación característica es:

$$s^4 + 3 s^3 + 5 s^2 + 4 s + 2 = 0$$

Determinar su estabilidad mediante el criterio de Routh.

{.problem}
 

Sea el sistema de control de tercer orden de la figura:



Si $\tau_1 = 1$, $\tau_2 = 1 / 2$ y $\tau_3 = 1 / 3$, determinar los
valores de $K_c$ para los que el sistema de control es estable.

 {.problem}
 

Un sistema formado por dos tanques en serie independientes se regula por
un control PID. Las constantes de tiempo de los tanques son 20 y 10 min,
mientras que las del elemento de medida de nivel es de 30 segundos. El
tiempo integral es de 3 min y el derivativo 40 s. Determinar el
intervalo de valores de $K_c$ para los que el lazo de control es
estable.

 {.problem}
 

En la actualidad se emplean discos duros en los ordenadores para
almacenar la información. Un cabezal de lectura se desplaza sobre el
disco giratorio a las posiciones requeridas en las operaciones de
lectura o grabación de información. Este desplazamiento ha de ser rápido
y preciso. En la figura adjunta se presenta el diagrama de bloques del
sistema de desplazamiento del cabezal de lectura.



Determinar los intervalos de estabilidad de $K$ y $a$. Qué valores
podría tomar $a$ para $K = 40$?


 {.problem}
 

Dibujar el lugar de las raíces para un sistema cuya función de
transferencia de lazo abierto es:
$$G_c G_f G_p G_m = \frac{K (s + 1)}{s (s + 2)}$$

 {.problem}
 

Sea un proceso con la siguiente función de transferencia:
$$G_p = \frac{10}{s + 1} \mathrm{e}^{- t_d s}$$ Este proceso se controla
mediante un controlador proporcional. Asumiendo que $G_m = G_f = 1$,
determinar la relación entre $K_c$ y $t_d$ que hace al lazo cerrado
estable en los siguientes casos:

1.  Aproximar el retraso con una aproximación de Padé de primer orden:
    $$\mathrm{e}^{- t_d s} \approx \frac{1 - \frac{t_d}{2} s}{1 + \frac{t_d}{2}
           s}$$

2.  Utilizar una aproximación de Padé para el retraso de segundo orden:
    $$\mathrm{e}^{- t_d s} \approx \frac{t_d^2 s^2 - 6 t_d s + 12}{t_d^2 s^2 + 6
           t_d s - 12}$$

{.problem}
 

Sea un proceso cuya función de transferencias es:
$$G_p = \frac{10 \mathrm{e}^{- 0.1 s}}{0.5 s + 1}$$

Los valores de los parámetros se han determinado con un error de $\pm
  20\%$. Calcular la mayor ganancia de un controlador proporcional que
hace al ciclo cerrado estable. Suponer $G_m = G_f = 1$.

