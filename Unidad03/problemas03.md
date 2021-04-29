# Tema 3

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

**Problema 3.1**

Hallar la transformada de Laplace de las siguientes funciones:

1.  $f (t) = \mathrm{e}^{- 2 t} \cos (t)$

2.  $f (t) = \mathrm{e}^{- 4 t} + \theta(t-2) \sin (t - 2) + t^2 \mathrm{e}^{- 2 t}$

3.  $f (t) = 2 \mathrm{e}^{- t} \cos (10 t) - t^4 + 6 \mathrm{e}^{- (t - 10)} \theta(t-10)$

**Problema 3.2**

Hallar la transformada inversa de:

1.  $f (s) = \frac{1}{\frac{s}{3} + 1}$

2.  $f (s) = \frac{s}{(s + 1)  (s^2 + 1)}$

3.  $f (s) = \frac{3 s + 4}{s^3  (s + 2)}$

4.  $f (s) = \frac{s^2}{(s^2 + 1)^2}$

**Problema 3.3**

Usando la técnica de la transformada de Laplace, encontrar las
respuestas transitoria y estacionaria del sistema descrito por la
ecuación diferencial siguiente:

$$\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + 3 \frac{\mathrm{d}y}{\mathrm{d}t} + 2 y = 1$$

con las condiciones iniciales $y (0) = y' (0) = 1$.

**Problema 3.04**

La respuesta a un escalón unidad de un sistema viene dada por:

$$y (t) = 1 - \frac{7}{3} \mathrm{e}^{- t} + \frac{3}{2} \mathrm{e}^{- 2 t} -
     \frac{1}{6} \mathrm{e}^{- 4 t}$$

1.  ¿Cuál es la función de transferencia de dicho sistema?

2.  ¿Cuál sería la respuesta en tiempo real si la entrada fuera un
    impulso unidad?
    
**Problema 3.5**

Resolver las siguientes ecuaciones diferenciales:

1.  $\frac{\mathrm{d}^2 y}{\mathrm{d}t^2} + 4 y = 3$ con
    $y (0) = y' (0) = 1$

2.  $\frac{\mathrm{d}y}{\mathrm{d}t} + 2 y = 5 \sin (3 t)$
    con $y (0) = 1$

**Problema 3.6**

Determinar las funciones de transferencia $\frac{h_2 (s)}{F_i (s)}$ de
los sistemas siguientes:

![Problema 3.6](img/prob306.svg)

El fluido tiene una densidad constante y las resistencias son lineales
($F = \frac{h}{R}$).
  
**Problema 3.7**

En un reactor tanque agitado se lleva a acabo una reacción irreversible
de primer orden, $A \rightarrow B$, con un coeficiente cinético $k = 1
 \ \mathrm{h^{-1}}$, El caudal de alimentación es de 10 l/min, con $c_{A_0}$ =
0.5 mol/l. El volumen del tanque es de 1 $m^3$. Determinar el efecto
causado por una subida instantánea de la concentración a 0.7 mol/l.
Indicar cual hubiese sido el transitorio, si la perturbación se hubiera
producido en forma de impulso unidad. Cuáles serán la ganancia y la
constante de tiempo del sistema?

**Problema 3.8**

Considerar el tanque encamisado de la figura utilizado como
precalentador. Suponiendo que la capacitancia de la pared del tanque es
despreciable y que la temperatura en el interior del mismo es uniforme.

![Problema 3.8](img/prob308.svg)

Deducir:

1.  La función de transferencia para variaciones de $T_1$ y/o $T_s$.

2.  El diagrama de bloques del sistema.

3.  La respuesta del sistema para una entrada en escalón unidad en $T_1$ ($T_s$ cte).