(historia)=
# Breve historia del control de procesos

## En la antiguedad

Los primeros sistemas de control conocidos, ya en la antigüedad, son mecanismos destinados al control del caudal para regular un reloj de
agua o el control de nivel de líquido en una lámpara de aceite o en un
recipiente de vino, que se mantiene lleno a pesar de los muchos vasos
que se sacan. De hecho, el control del caudal de fluido se reduce al
control del nivel del fluido, ya que un pequeño orificio producirá
caudal constante si la presión es constante. El mecanismo de control de
nivel de líquido inventado en la antigüedad y todavía usado para
controlar nivel es la válvula flotante, semejante a la del depósito de
agua de un inodoro corriente. El flotador está hecho de tal manera que,
cuando el nivel baja, el caudal del depósito aumenta y cuando el nivel
sube, el caudal disminuye y, si es necesario, se corta ({numref}`romanos`). En
este caso el sensor y el actuador están combinados en el mismo
dispositivo, el flotador y la combinación de tubo de alimentación.

```{figure} ./img/romanos.svg
---
height: 300px
name: romanos
figclass: margin-caption
---
Un tonel que nunca se acaba Ejemplo del control de nivel de líquido y caludal tal como se realizaba en la antiguedad.
```

## Durante la revolución industrial

Un caso más moderno de control por retroalimentación es el control de
temperatura de un horno para calentar una incubadora, sistema que fue
diseñado por Drebbel (hacia 1620). El horno constaba de una caja que
contenía el fuego, con un tubo en la parte superior provisto de un
regulador de tiro ({numref}`drebbel`). Dentro de la cámara de combustión estaba la
incubadora de paredes dobles y el hueco que quedaba entre las paredes se
llenaba de agua. El sensor de temperatura era un recipiente de vidrio
lleno de alcohol y mercurio colocado en la cámara de agua en torno a la
incubadora. A medida que el fuego calentaba la caja y el agua, el
alcohol se dilataba y el vástago con flotador se desplazaba hacia
arriba, bajando el regulador de tiro sobre la boca del tubo. Si la caja
está demasiado fría, el alcohol se contrae, el regulador de tiro se abre
y el fuego arde más fuertemente. La temperatura deseada está determinada
por la longitud del vástago del flotador, que determina la apertura del
regulador de tiro para una dilatación determinada de alcohol.

```{figure} ./img/drebbel.png
---
height: 300px
name: drebbel
figclass: margin-caption
---
Croquis de la incubadora de Drebbel para empollar huevos de gallina.
```

La búsqueda de un medio para controlar la velocidad de rotación de un
eje fue un problema famoso en las crónicas del control automático. La
principal motivación era la de controlar automáticamente la velocidad de
la piedra de molienda de un molino de viento harinero. De los varios
métodos que se intentaron, el más prometedor resultó ser el que usaba un
péndulo cónico, o regulador de bola flotante. Este dispositivo se usó
para medir la velocidad del molino; las aspas del molino de viento se
hacían girar con cuerdas y poleas, casi como persianas, para mantener
una velocidad fija. Pero no fue el molino de viento es que hizo famoso
el regulador de bola flotante, fue su adaptación a la máquina de vapor
en los laboratorios de James Watt, alrededor de 1788 ({numref}`watt`).

```{figure} ./img/Vapor.png
---
height: 300px
name: watt
figclass: margin-caption
---
Máquina de vapor con un regulador centrífugo o de bola flotante, que aparece en la parte derecha de la imagen.
```

La acción del regulador centrífugo es fácil de describir. Supongamos que
la máquina está operando en equilibrio y aplicamos de pronto una carga.
En ese momento disminuirá la velocidad de la máquina y las bolas del
regulador caerán a un cono más pequeño. De este modo, el ángulo de las
bolas se usa como sensor de salida. Esta acción, a través de palancas,
abrirá la válvula principal al núcleo de vapor (que es el actuador) y
admitirá más vapor a la máquina, recuperando la totalidad de la
velocidad perdida. Para mantener la válvula de vapor en una nueva
posición es necesario que las bolas giren a un ángulo diferente, lo que
implica que la velocidad con una carga no es exactamente la misma que la
anterior. Para recobrar la misma velocidad en este sistema, sería
necesario reponer la velocidad deseada cambiando la longitud de la barra
de la palanca a la válvula. Otros inventores introdujeron mecanismos que
integraron el error de velocidad y así proporcionaron una reposición
automáticas. Estos sistemas tienen error estacionario cero a
perturbaciones constantes.

Watt fue un hombre práctico, como el constructor de molinos anterior a
él, y no se ocupó de análisis teóricos del regulador. En este sentido
son de gran importancia las contribuciones de G.B. Airy, que fue
profesor de matemáticas y astronomía de la Universidad de Cambridge
desde 1826 a 1835 y Astrónomo Real en el Observatorio de Greenwich desde
1835 a 1881. Airy se interesó por el control de la velocidad; si sus
telescopios hubieran podido girar en sentido contrario a la Tierra, se
habría podido observar una estrella fija durante largos períodos de
tiempo. Él utilizó el regulador centrífugo de péndulo y descubrió que
era capaz de movimiento inestable. Airy realizó la primera exposición
histórica de la inestabilidad en un sistema de control, el análisis de
un sistema a través de ecuaciones diferenciales y, por tanto, los
comienzos del estudio de la dinámica de control con retroalimentación.

## Inicios teóricos

El primer estudio sistemático de la estabilidad del control
retroalimentado apareció en el trabajo *On Governors* de J.C. Maxwell
(1868). En este trabajo, Maxwell desarrolla las ecuaciones diferenciales
del regulador, linealizándolas en torno al equilibrio, y estableció que
la estabilidad depende de que las raíces de una cierta ecuación
(característica) tengan partes reales negativas. Lo consiguió solamente
para los casos de segundo y tercer orden. El problema de la
determinación de criterios de estabilidad sirvió para el premio Adams de
1877, que fue ganado por E.J. Routh. Su criterio, desarrollado en el
ensayo que obtuvo el premio, tiene el interés suficiente como para que
los ingenieros de control sigan aprendiendo a aplicar su sencilla
técnica. El análisis de la ecuación característica siguió siendo el
fundamento de la teoría de control hasta la invención del amplificador
retroalimentado electrónico por H.S. Black en 1927 en los laboratorios
de la Bell Telephone. Después de la publicación del trabajo de Routh, el
matemático ruso A.M. Lyapunov comenzó a estudiar la cuestión de la
estabilidad del movimiento; en 1892 utilizó las ecuaciones no lineales
de movimiento e incluyó resultados equivalentes al criterio de Routh. Su
trabajo fue fundamental, pero no se introdujo en la literatura de
control hasta 1958.

Con la introducción de los amplificadores electrónicos, las llamadas a
larga distancia llegaron a ser posibles en las décadas posteriores a la
Primera Guerra Mundial. Sin embargo, conforme la distancia aumenta, lo
hace la pérdida de energía eléctrica, a pesar del uso del alambre de
gran diámetro, y se requieren más y más amplificadores para reemplazar
las pérdidas. Lamentablemente, con tantos amplificadores había mucha
distorsión ya que las pequeñas no linealidades de los tubos de vacío se
multiplicaban una y otra vez. Como solución a este problema, Black
propuso el amplificador retroalimentado. Para reducir la distorsión hay
que aumentar la retroalimentación, es decir, la ganancia del lazo del
actuador debe aumentarse mucho. Todos los que han tratado de subir el
volumen en un sistema de amplificación público mal ubicado han
experimentado lo descubierto por Black; con altas ganancias el lazo de
retroalimentación comienza a pitar y es inestable. Aquí, en una
tecnología diferente estaba el problema de estabilidad de Maxwell y
Routh, y la dinámica era tan compleja (las ecuaciones diferenciales de
orden 50 son muy comunes) que el criterio de Routh no sirvió de mucho.
Los ingenieros de comunicaciones estaban familiarizados con la idea de
respuesta de frecuencia y con matemáticas de variable compleja
desarrollada por Cauchy y otros, así que los trabajos en los
laboratorios de la Bell se orientaron al análisis complejo. En 1932, H.
Nyquist publicó un artículo describiendo como determinar la estabilidad
desde un gráfico de la respuesta de frecuencia del lazo. A partir de
esta teoría se desarrolló una extensa metodología de diseño de
amplificadores retroalimentados, descrita en el libro de Bode (1945).

## Implantación en la industria

Simultáneamente al desarrollo del amplificador retoralimentado, el
control retroalimentado de procesos industriales empezó a ser la norma.
En este campo, caracterizado por procesos que no solamente son muy
complejos sino también no lineales y sujetos a retrasos de tiempo
relativamente largos entre actuador y sensor, se desarrolló la práctica
del control proporcional, más integral y más diferencial, el control PID
descrito por Callender, Hartree y Porter (1936). Esta tecnología, basada
en un amplio trabajo experimental y aproximaciones linealizadas simples
al sistema dinámico, llevó a experimentos estándar apropiados para la
aplicación en el campo y finalmente a una satisfactoria sintonía de los
coeficientes del controlador PID. También se desarrollaron en esta época
los dispositivos para guía y control de aviones; especialmente
importante fue el desarrollo de sensores adecuados para medición de
altura y velocidad de los aviones.

Se dio un enorme impulso al control retroalimentado durante la Segunda
Guerra Mundial. En Estados Unidos, ingenieros y matemáticos del
Laboratorio de Radiación del MIT combinaron sus conocimientos para
aportar juntos no solamente la teoría de los amplificadores
retroalimentados de Bode y el control PID de los procesos, sino también
de procesos estocásticos desarrollados por N. Wiener (1930). El
resultado fue el desarrollo de un conjunto completo de técnicas para el
diseño de mecanismos de control, o servomecanismos, como también han
sido llamados.

Otro enfoque al diseño de sistemas de control se introdujo en 1948 por
W.R. Evans, que trabajaba en el campo de guía y control de aviones.
Muchos de estos problemas tiene estados dinámicos inestables o
neutralmente estables, y él sugirió un retorno al estudio de la ecuación
característica que había sido la base del trabajo de Maxwell y Routh 70
años antes. Sin embargo Evans desarrolló técnicas y reglas que permiten
seguir gráficamente los pasos de los lugares geométricos de las raíces
de la ecuación característica cuando se cambiaba un parámetro. Su
método, el lugar geométrico de las raíces, es adecuado para el diseño y
análisis de estabilidad y continúa siendo hoy día una técnica
importante.
