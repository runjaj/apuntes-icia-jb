(prob604)=
# Problema 6.4

<style type="text/css">
    ol { list-style-type: lower-alpha; }
</style>

La temperatura de un proceso tien un campo de variación de 200 ℃. Para efectuar su control se dispone de dos opciones de controladores neumáticos que actúan sobre una válvula:

1. Un controlador proporcional (3-15 psig) de BP = 50 %.

2. Un controlador PI de BP = 50 % y $\tau_I$ = 1 min.

El proceso en estado estacionario está a 60 ℃, siendo la presión del controlador 3 psig. Si la temperatura aumenta bruscamente hasta 70 ℃, calcular:

1. La presión que actúa sobre la válvula en el control P.

2. La presión que actúa sobre la válvula en el control PI.

3. La influencia de la BP en el control PI.

4. La influencia de la $\tau_I$ en el control PI.

---

**Solución**

Para ambos controladores la temperatura estacionaria es de 60 °C. En esas condiciones la salida del controlador es de 3 psig. Como consecuencia se tomarán $c_s = 3 \text{ psig}$.

El cambio brusco de temperatura es un escalón de altura 10 °C:

$$\varepsilon = 70 \text{ ºC} - 60\text{ ºC} = 10\text{ ºC}$$

a) Una banda proporcional de 50% implica que aunque el campo de variación del controlador sea de 200 °C solo se controlarán variaciones de temperatura máximas de:

$$\mathrm{BP} = 50\%= \frac{\Delta T_{}}{200} 100 \Rightarrow \Delta T_{} = 100\text{ ºC}$$
   
Por tanto la ganancia proporcional es:

$$K_c = \frac{\Delta P}{\Delta T} = \frac{15 \text{ psig} - 3
   \text{ psig}}{100\text{ ºC}} = 0.12 \text{ psig} / \text{K}$$
   
La salida del controlador proporcional será:

$$c (t) = K_c \varepsilon (t) + c_s = (0.12 \text{ psig} / K)  (10^{\circ}
   \text{C}) + 3 \text{ psig} = 4.2 \text{ psig}$$
   
b) La respuesta del controlador PI es (la ganancia proporcional es la
misma que en el apartado anterior):

$$c (t) = K_c \varepsilon (t) + \frac{K_c}{\tau_I} \int_0^t \varepsilon (t)
   \mathrm{d}t + c_s = K_c \varepsilon + \frac{K_c}{\tau_I} \varepsilon t + c_s =
   4.2 \text{ psig} + (1.2 \text{ psig} / \text{min}) t$$
   
A los 9 minutos el controlador se satura ($c = 15 \text{ psig}$). Pasados 9 minutos el sistema queda fuera de control.

c\) Al aumentar la banda proporcional, disminuye la ganancia proporcional. Esa disminución supone que la acción de control será menos intensa. La pendiente de la curva del aparatado b) $\frac{K_c}{\tau_I} \varepsilon$ será menor, como consecuencia el sistema de control será más lento, tardará más tiempo en saturarse y en eliminar los errores del sistema.

d\) Si aumenta la constante de tiempo integral, la acción de control es menos intensa y más lenta ya que disminuye la pendiente
$\frac{K_c}{\tau_I} \varepsilon$.

 

 
