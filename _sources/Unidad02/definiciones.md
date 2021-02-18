# Algunas definiciones de instrumentación

A continuación se definen unos cuantos conceptos de uso frecuente en el
campo de la instrumentación:

```{figure} ./img/defs_instrumentacion.svg
---
name: defs_instrum
figclass: margin-caption
---
Representación gráfica de algunas de las definiciones de los instrumentos. En b) y c) las fle- chas indican el sentido de la medida. En c), se ha exagerado la histéresis para que su efecto fuera más visible.
```

1.  **Campo de medida** (*range*): Espectro o conjunto de valores de medida que están comprendidos dentro de los límites superior e inferior de la capacidad de medida o de transmisión del instrumento. Viene expresado estableciendo los dos valores extremos. Para el ejemplo de la {numref}`defs_instrum` es de 100-300 ℃.

2.  **Alcance** (*span*): Es la diferencia algebraica entre los valores
    superior e inferior del campo de medida del instrumento. Para el
    ejemplo el valor es de 200 ℃.

3.  **Error**: Es la diferencia entre el valor leído transmitido por el
    instrumento y el valor real de la variable medida. El error medio
    del instrumento es la media aritmética de los errores determinados
    para todos los valores crecientes y decrecientes de la variable
    medida.

4.  **Precisión** (*accuracy*): Es la tolerancia de media o de transmisión
    del instrumento y define los límites de los errores cometidos cuando
    el instrumento se emplea en condiciones normales de servicio. Se
    puede expresar de las siguientes maneras:

    1.  Porcentaje del alcance. Para el ejemplo de la figura anterior
        una lectura de 150 ℃ y una precisión de 0.5 %, la lectura se
        encontrará entre 149 y 151 ℃, ya que 150 ℃ ± 0.005/200 = 150
        ℃ ± 1 ℃.

    2.  Directamente. Por ejemplo, ±1 ℃.

    3.  Porcentaje de la lectura efectuada. Por ejemplo, precisión de ±1 % de 150 ℃, es decir, ±1.5 ℃.

    4.  Porcentaje del valor máximo del campo de medida. Precisión de
        ±0.5 % de 300 ℃, ±1.5 ℃.

    La precisión varía en cada punto del campo de medida, el fabricante
    la especifica en todo el margen del instrumento indicando a veces su
    valor en algunas zonas de la escala. Cuando se desea obtener la
    máxima precisión en un punto determinado de la escala, se puede
    calibrar únicamente para este punto de trabajo, sin considerar los
    valores restantes del campo de medida.

5.  **Zona muerta** (*dead zone* o *dead band*): Es el campo de valores que
    no hace variar la indicación o señal de salida del instrumento, es
    decir, que no produce su respuesta. Viene dada como porcentaje del
    alcance de la medida. Para el instrumento de la figura es de ±1
    %, es decir, ±0.001 · 200 ℃ = ±0.2 ℃.

6.  **Sensibilidad** (*sensitivity*): Es la razón entre el incremento de la
    lectura y el incremento de la variable que la ocasiona, después de
    alcanzarse el estado de reposo. Por ejemplo, si en un transmisor
    electrónico de 0-10 bar, la presión pasa de 5 a 5.5 bar y la señal
    de 11.9 a 12.3 mA (en una línea 4-20 mA), la sensibilidad es:
        
    $$\frac{\frac{12.3 \text{ mA} - 11.9 \text{ mA}}{20 \text{ mA} - 4 \text{ mA}}}{{\frac{5.5 \text{ bar} - 5 \text{ bar}}{10 \text{ bar}}}} = \pm 0.5$$
         
    También puede venir expresada en forma de porcentaje del
    alcance de la medida. Si la sensibilidad del instrumento de la
    figura es de ±0.05 %, su sensibilidad será de ±0.01 ℃.

7.  **Repetibilidad** (*repeatability*): Es la capacidad de reproducción de
    las medidas o señales de salida del instrumento al medir
    repetidamente valores idénticos de la variable en las mismas
    condiciones de servicio y en el mismo sentido de la variación,
    recorriendo todo el campo. Se considera en general su valor máximo
    (repetibilidad máxima) y se expresa como porcentaje del alcance, un
    valor representativo es el de ± 0.01 %. El término de
    repetibilidad no incluye la histéresis.

    Para determinarla, el fabricante comprueba la diferencia entre el
    valor verdadero de la variable y la indicación o señal de salida del
    instrumento recorriendo todo el campo, y partiendo, para cada
    determinación, desde el valor mínimo del campo de medida. La
    repetibilidad viene dad por la fórmula siguiente:
        
    $$\mathrm{Repetibilidad} = \sqrt{\frac{\sum (x_i - x)^2}{N}}$$
    
    De manera que para los datos de la tabla siguiente la repetibilidad
    es:
        
    $$\mathrm{Repetibilidad} = \sqrt[]{\frac{0.00785}{19}} = \pm 0.02\%$$

    ```{table}  Ejemplo de medidas de un instrumento recorriendo todo el campo de medida.          
      
      Variable | Indicación     |        Variable     |  Indicación
      ---|---:|---|---:
    Desde 0.0 a 0.5  |   0.502    |        Desde 0.0 a 5.5   |   5.505
    Desde 0.0 a 1.0  |   1.006    |        Desde 0.0 a 6.0   |   6.006
    Desde 0.0 a 1.5  |   1.509    |        Desde 0.0 a 6.5   |   6.501
    Desde 0.0 a 2.0  |   2.008    |        Desde 0.0 a 7.0   |   7.003
    Desde 0.0 a 2.5  |   2.506    |        Desde 0.0 a 7.5   |   7.504
    Desde 0.0 a 3.0  |   3.007    |        Desde 0.0 a 8.0   |   8.009
    Desde 0.0 a 3.5  |   3.503    |        Desde 0.0 a 8.5   |   8.508
    Desde 0.0 a 4.0  |   4.006    |        Desde 0.0 a 9.0   |   9.008
    Desde 0.0 a 4.5  |   4.507    |        Desde 0.0 a 10.0 |    10.005
    Desde 0.0 a 5.0  |   5.010    |                   
    ```

8.  **Histéresis** (*hysteresis*): Es la diferencia entre los valores
    indicados por el instrumento para un valor cualquiera del campo de
    medida cuando la variable recorre toda la escala en sentido
    ascendente y descendente. Se expresa como porcentaje del alcance.

    Por ejemplo, si un termómetro de 0-100 ℃, para el valor de la
    variable 40 ℃, la temperatura es de 39.9 ℃ al subir la temperatura
    desde 0 ℃, e indica 40.1 ℃ al bajar la temperatura desde 100 ℃, el
    valor de la histéresis es de:
        
    $$\frac{40.1 \ \mathrm{ ºC} - 39.9 \ \mathrm{ ºC}}{100 \ \mathrm{ºC} - 0\ \mathrm{ºC}} 100 = \pm 0.2\%$$
