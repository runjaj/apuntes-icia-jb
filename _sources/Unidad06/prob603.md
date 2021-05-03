(prob603)=
# Problema 6.3

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

Un controlador neumático de acción directa, que opera en el intervalo de 3-15 psig para una escala de temperatura de 0 a 100 ℃, está saturado para temperaturas inferiores a 30 ℃ y superiores a 90 ℃. Determinar:

1. La ganancia y la BP.

2. La presión del aire a la salida del controlador cuando la temperatura sea de 70 ℃.

3. La $\tau_I$ de un controlador integral incorporado al proporcional, si al introducir ele elemento medido en un medio a 70 ℃ (inicialmente a 30 ℃) el controlador se satura en 10 minutos.

---

**Solución**

1. En este caso el sistema controlador-elemento final de control tiene la capacidad de controlar cambios de temperatura entre 0 y 100 °C, pero se utiliza para controlar cambios entre 30 y 90 °C. Eso supone que no se utiliza toda la capacidad de control del sistema de control pero que se utiliza una ganancia proporcional del controlador más elevada, con las ventajas que eso puede suponer. La banda proporcional de este sistema es:

$$\mathrm{BP} = \frac{90\text{ ºC} - 30 \text{ ºC}}{100\text{ ºC} - 0\text{ ºC}} 100 = 60\%$$
   
La ganancia del controlador es:

$$K_c = \frac{15\ \mathrm{psig} - 3 \text{ psig}}{90 \text{ ºC} -   30 \text{ ºC}} = 0.2 \mathrm{psig} /\text{ºC}$$

b) La salida de un controlador proporcional es:

$$c (t) = K_c \varepsilon (t) + c_s$$

donde $c_s$ es el *bias* del controlador, es decir, la salida del controlador cuando el error es nulo.

En primer lugar hay que calcular el *bias* del controlador, para ello se va a suponer que en estado estacionario la temperatura es de 30 °C y que la salida del controlador es de 3 psig. Por tanto, 

$$3\ \mathrm{psig} = K_c 0 + c_s \Rightarrow c_s = 3\ \mathrm{psig}$$

Si la temperatura es de 70 °C, el error será:

$$\varepsilon = 70 \text{ ºC} - 30 \text{ ºC} = 40 \text{ ºC}$$

Por tanto, la salida del controlador es:

$$c = (0.2\ \mathrm{psig} /\text{ºC}) (40 \text{ ºC}) + 3\ \mathrm{psig} = 11\ \mathrm{psig}$$

c) Aquí se plantea un cambio en la temperatura en forma de escalón de
altura 40 °C, lo que supone que $\varepsilon = 40 $°C.

Un controlador proporcional-integral (PI) responde a la siguiente
dinámica:

$$c (t) = K_c \varepsilon + \frac{K_c}{\tau_I} \int_0^t \varepsilon \mathrm{d}t
   + c_s$$ 

Se debe buscar qué constante de tiempo integral hace que el controlador se sature (que alcance uno de los valores límite de salida, en este caso, la máxima presión de salida) a los 10 minutos. Por tanto:

$$c (t = 10) = 15\ \mathrm{psig} = (0.2\ \mathrm{psig} /\text{ºC}) (40\text{ ºC}) + \frac{0.2}{\tau_I} \int_0^{10} (40\text{ ºC}) \mathrm{d}t + 3\ \mathrm{psig}$$

Resolviendo la ecuación anterior se encuentra que $\tau_I = 20 \min$.