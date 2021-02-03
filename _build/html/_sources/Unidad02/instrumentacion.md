# Algo de instrumentación

## Dispositivos de medida (sensores)

Para el correcto funcionamiento de un sistema de control es
imprescindible una buena medida de la variable controlada y unas líneas
de transmisión efectivas. Existe una gran cantidad de dispositivos de
medida y su número aumenta día a día. Difieren entre sí tanto en el
principio básico de medida como en su construcción. En la tabla
siguiente se muestran algunos de los sensores más típicos en el control
de procesos junto con sus posibles aplicaciones. Para una información
más detallada generalmente hay que recurrir a los fabricantes de
sensores.

```{table} Principales sensores utilizados en la industria alimentaria.

| ![](./img/comparativa.pdf) |
|---|
```

A continuación se comenta con un poco de detalle cuatro de los
dispositivos de medida más utilizados en la industria de procesos.

### Medidores de caudal

Los medidores de caudal más utilizados en la industria son aquellos que
miden una diferencia de presión en el fluido al pasar por un elemento en
la línea que crea una pérdida de carga. Para calcular el caudal
volumétrico que pasa por ese punto se recurre a la ecuación de
Bernoulli. Los más típicos son la *placa de orificio*, más barata, y el
*tubo de Venturi*, más caro pero de mayor precisión.

Un método diferente de medir el caudal volumétrico es la utilización de
*turbinas*. En este caso se calcula el flujo a partir del número de
vueltas de la turbina para un tiempo dado.

En general los medidores de caudal presentan dinámicas muy rápidas que
normalmente pueden ser modeladas con las siguiente ecuación algebráica:

$$\text{cuadal} = \alpha \sqrt{\Delta P}$$ 

donde
$\alpha$ es una constante característica del medidor de caudal y
$\Delta P$ es la diferencia de presión.

### Sensores de temperatura

Los más comunes son aquellos que miden la temperatura como una señal
eléctrica. Entre ellos cabe destacar los termopares. Independientemente
de sus diferencias constructivas, su dinámica básica puede ser descrita
en función de sus perfiles de temperatura. El elemento sensor de la
temperatura siempre se encuentra en el interior de una vaina de metal.
Los termopares pueden ser modelados siguiendo sistemas de primer orden o
sistemas de segundo orden sobreamortiguados dependiendo de como estén
construidos y de los materiales utilizados.

## Líneas de transmisión

En el caso de utilizar líneas de transmisión neumática muy largas puede
ser que su efecto sobre la dinámica global del sistema no sea
despreciable. Normalmente siguen una dinámica que puede ser descrita con
la siguiente función de transferencia:

$$\frac{P_o}{P_i} = \frac{e^{- \tau_d s}}{\tau_p + 1}$$

donde $P_o$ es
la presión de salida de la línea de transmisión neumática, $P_i$ es la
presión de entrada y $\tau_d / \tau_p \approx
0.25$.

## Elementos finales de control

El elemento final de control más común es la válvula. El sistema de
control cambia la posición del émbolo ya sea utilizando aire comprimido,
si es una válvula neumática, o corriente eléctrica. Las válvulas
neumáticas se distinguen principalmente en las *air-to-close* o *fail
open*, en las que el émbolo desciende al aumentar la presión del aire.
En caso contrario se trata de válvulas del tipo *air-to-open* o *fail
closed*.

Las válvulas puede ser modelizadas siguiendo una dinámica de segundo
orden. Pero para las válvulas pequeñas o de tamaño medio la dinámica es
tan rápida que se puede considerar que es un proceso de primer orden.
Para la mayoría de productos el caudal que pasa por la válvula puede ser
descrito por la ecuación siguiente:

$$F = Kf (x)  \sqrt{\frac{\Delta P}{\rho}}$$

 donde $\Delta P$ es la
caída de presión del fluido al paso de la válvula, $K$ es una constante
que depende del tamaño de la válvula, $\rho$ es la densidad del fluido y
$f(x)$ es una curva característica para la válvula.

Otros elementos finales de control pueden ser motores de velocidad
variable para ventiladores o bombas, la puesta en marcha o apagado de
equipos, sistemas electrohidráulicos, etc.
