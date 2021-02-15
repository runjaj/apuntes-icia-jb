# Inversión de transformadas. De vuelta al tiempo real

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