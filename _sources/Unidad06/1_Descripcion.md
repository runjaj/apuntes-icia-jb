# Descripción de un bucle de control

Un bucle de control por retroalimentación se compone de un proceso, el
sistema de medición de la variable controlada, el sistema de control y
el elemento final de control

. Cada uno de estos elementos tiene su propia dinámica, que vendrá
descrita por una función de transferencia.

En este capítulo se explicará como se puede encontrar la función de
transferencia de todo un lazo de control a partir de las funciones de
transferencia de cada uno de los elementos del lazo. El medidor, el
proceso y el elemento final de control serán habitualmente sistemas
lineales de primer o de segundo orden, como los descritos en los dos
capítulos anteriores. Las funciones de transferencia de los
controladores se detallarán más adelante en este capítulo.

El sistema de control se compone del controlador y del punto suma, que
compara la lectura del medidor con la consigna para dar el error
$\varepsilon$ que alimenta el controlador. El objetivo del sistema de
control es minimizar el error para que su valor sea lo más próximo a
cero. Además debe lograr eliminar los errores lo más rápidamente
posible.

En el capítulo 1 se describe cualitativamente un bucle de control por
retroalimentación, un intercambiador de calor en una planta de
pasteurización de leche. En este capítulo se describirá el bucle de una
manera más detallada

.

El proceso, en este caso el intercambiador de calor, viene descrito por
la función de transferencia $G_p$. El proceso puede tener dos posibles
entradas: $f (t)$ que es la variable manipulable y $d (t)$ que
representa a las perturbaciones. Las perturbaciones pueden ser una
entrada en cualquier punto del lazo de control, pero normalmente son
debidas al proceso. La respuesta del proceso es la variable controlada
que normalmente se indicará como $y (t)$. Esta variable es la respuesta
global del sistema formado por todos los elementos del lazo de control.

El valor de la variable controlada se mide con un sensor, un termómetro
de resistencia de tipo Pt100 para el ejemplo, cuya dinámica viene
descrita por la función de transferencia $G_m$. Como salida de este
proceso se obtiene la variable controlada medida $y_m (t)$.

El valor de $y_m$ se compara con la consigna
$y_{\ensuremath{\operatorname{sp}}} (t)$ para obtener el error
$\varepsilon (t)$. El valor de la consigna será normalmente cero, en el
caso de estar definido utilizando variables de desviación. Este error es
la entrada del controlador, cuya función de transferencia es $G_c$. Las
respuesta del controlador $c (t)$ es una intensidad de corriente o una
diferencia de presión según sea el sistema de transmisión de información
eléctrico o neumático.

Esta acción de control $c (t)$ modifica al elemento final de control
($G_f$), en ejemplo tratado es una válvula, para que cambie el valor de
la variable manipulable $f (t)$. El cambio de la variable manipulable
modifica el estado del proceso. Si el sistema de control funciona
correctamente este cambio de la variable controlada debe tender a
eliminar el error. En el caso de que lo que se haya producido haya sido
un cambio a la consigna, debe conducir al sistema al nuevo estado
estacionario deseado.

Aunque la mayoría de elementos del bucle de control son de acción
directa --el signo de la salida es el mismo de la entrada--, también
existen procesos de acción inversa. Los procesos de acción inversa
tienen una ganancia negativa. Un elemento de acción inversa presente en
todos los lazos de control es el comparador. En el comparador se produce
una cambio de signo ya que para calcular el error se resta la variable
medida a la consigna (Fig.
[\[comparador\]](#comparador){reference-type="ref"
reference="comparador"}. a)). Por este motivo se puede considerar al
comparador como un elemento de acción inversa.

Se puede demostrar de manera muy sencilla que para que un lazo de
control pueda funcionar correctamente debe tener un número impar de
elementos de acción inversas, es decir, un número impar de cambios de
signo en el lazo de control. Si existe en el lazo de control un número
par de elementos de acción inversa se debe incluir un bloque -1 entre el
comparador y el controlador (Fig.
[\[comparador\]](#comparador){reference-type="ref"
reference="comparador"}. b))

a\) b)

.

En este curso los bloques y procesos utilizados solo tienen una entrada
y una salida. En cambio el proceso en la figura
[\[fig:lazo\]](#fig:lazo){reference-type="ref" reference="fig:lazo"} el
proceso tiene dos entradas, la variable manipulable y las
perturbaciones. Para evitar ese problema habitualmente el se considera
que además del proceso existe una función de transferencia debida a las
perturbaciones ($G_d$)

que no forma parte del lazo de control. Realizando esa modificación el
lazo de control queda como el mostrado en la figura
[\[fig:lazo perturbaciones\]](#fig:lazo perturbaciones){reference-type="ref"
reference="fig:lazo perturbaciones"}.

Con frecuencia los lazos de control se expresan de manera simplificada
utilizando la forma canónica

. Para ello es necesario tener en cuenta que $G_c$, $G_f$ y $G_p$ son
tres funciones de transferencia en serie.

La función de transferencia entre la consigna y la salida es:
$$\frac{y (s)}{y_{\ensuremath{\operatorname{sp}}} (s)} = \frac{G_c G_f G_p}{1 + G_c G_f G_p G_m}$$

La función de transferencia entre la perturbación y la salida es:
$$\frac{y (s)}{d (s)} = \frac{G_d}{1 + G_c G_f G_p G_m}$$

Por tanto la salida del lazo de control para un cambio simultáneo de la
consigna y de la perturbación será:
$$y (s) = \frac{G_c G_f G_p}{1 + G_c G_f G_p G_m} y_{\ensuremath{\operatorname{sp}}} (s) +
   \frac{G_d}{1 + G_c G_f G_p G_m} d (s)$$
