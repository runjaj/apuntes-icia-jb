# Definición de estabilidad. Ecuación característica

Un sistema dinámico es *estable* si para cualquier entrada acotada se obtiene una salida acotada, independientemente de cual fuese su estado
inicial.

La inestabilidad de los sistemas es la mayor limitación a la hora derealizar la sintonía del controlador.

Tal como se ha visto en los temas anteriores la respuesta de bucle cerrado para un sistema de control generalizado es:

$$y = \frac{G_c G_p G_f}{1 + G_c G_p G_f G_m} y_{sp} + \frac{G_d}{1 +
   G_c G_p G_f G_m} d$$

Normalmente, la estabilidad o inestabilidad de un sistema es intrínseca al mismo, independientemente de la entrada. Es un problema del sistema.

Para estudiar la estabilidad de la respuesta es necesario realizar la transformada inversa de Laplace para obtener la respuesta en tiempo real. Para ello hay que descomponer $y (s)$ en fracciones simples. Para realizar esta descomposición se deben encontrar las raíces de la *ecuación característica* ($1 + G_c G_p G_f G_m = 0$). La ecuación característica es el denominador de las funciones de transferencia tanto del problema de la regulación o de la carga como del servocontrol, es decir, es 1 más el producto de las funciones de transferencia del lazo de retroalimentación ($G_{OL}$).

Las raíces de la ecuación característica son $\alpha_i$, $i = 1, \ldots, n$. Por tanto, una vez realizada la descomposición en fracciones simples:

$$y (s) = \frac{y_0}{s} + \frac{y_1}{s - \alpha_1} + \frac{y_2}{s - \alpha_2}
   + \ldots + \frac{y_n}{s - \alpha_n}$$

Tras realizar la transformada inversa de Laplace se obtiene la función en tiempo real:

$$y (t) = y_0 + y_1 \mathrm{e}^{\alpha_1 t} + y_2 \mathrm{e}^{\alpha_2 t} + \ldots +
   y_n \mathrm{e}^{\alpha_n t}$$ 
   
donde:

$$\alpha_i \in \mathbb{C}, \forall i$$ 

Es decir, todas las raíces de la ecuación característica son números complejos. Por tanto, para todo $i$:

$$\alpha = \beta + \mathrm{i}\gamma \Rightarrow \mathrm{e}^{\alpha t} =
   \mathrm{e}^{\beta t}  (\cos \gamma t + \mathrm{i}\sin \gamma t)$$

El valor de $\gamma$ no influye en la salida del sistema desde el punto de vista de la estabilidad, ya que tanto el seno como el coseno son funciones acotadas. Sólo cambia la frecuencia de la respuesta.

En cambio, si $\beta$ es positivo, aparece un problema de estabilidad ya que la respuesta aumentaría constantemente con el tiempo. Por tanto, para que la salida del sistema sea estable todas las partes reales de las raíces de la ecuación característica deben ser negativas, deben estar situadas en el semiplano real negativo. En el caso de que alguna no lo fuese:

$$\lim_{t \to \infty} y (t) = \infty$$

Con esta información es posible diseñar técnicas que permitan seleccionar las constantes del controlador garantizando la estabilidad del sistema.
