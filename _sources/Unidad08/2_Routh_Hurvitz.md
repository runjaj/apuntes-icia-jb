# Método de Routh-Hurvitz

El método de Routh-Hurvitz permite comprobar de una manera rápida y sencilla si alguna de las partes reales de las raíces de la ecuación característica es positiva sin necesidad de tener que encontrar las raíces.

Operando la ecuación característica se obtiene:

$$1 + G_c G_p G_f G_m \equiv a_0 s^n + a_1 s^{n - 1} + \ldots + a_{n - 1} s +
   a_n = 0$$

donde $a_0$ debe ser positivo.

El criterio de estabilidad de Routh-Hurvitz es:

1.  Condición necesaria pero no suficiente: Todos los coeficientes $a_0, a_1, \ldots, a_n$ de la ecuación característica deben ser positivos para que el sistema sea estable. Si alguno de los coeficientes es negativo, al menos una de las raíces tendrá la parte real positiva.

2.  Condición necesaria y suficiente: Se construye la matriz de Routh:

    $$\begin{array}{c|ccccc}
           1 & a_0 & a_2 & a_4 & a_6 & \ldots\\
           2 & a_1 & a_3 & a_5 & a_7 & \ldots\\
           3 & A_1 & A_2 & A_3 & \ldots & \\
           4 & B_1 & B_2 & B_3 & \ldots & \\
           5 & C_1 & C_2 & C_3 & \ldots & \\
           \vdots & \vdots & \vdots & \vdots &  & \\
           n + 1 & W_1 & W_2 &  &  & 
         \end{array}$$
         
    donde:
        
    $$\begin{aligned}
        & A_1 = \frac{a_1 a_2 - a_0 a_3}{a_1},\ A_2 = \frac{a_1 a_4 - a_0
        a_5}{a_1},\ A_3 = \frac{a_1 a_6 - a_0 a_7}{a_1},\ \ldots & \\
        & B_1 = \frac{A_1 a_3 - a_1 A_2}{A_1},\ B_2 = \frac{A_1 a_5 - a_1
        A_3}{A_1},\ \ldots & \\
        & C_1 = \frac{B_1 A_2 - A_1 B_2}{B_1},\ C_2 = \frac{B_1 A_3 - A_1
        B_3}{B_1},\ \ldots & \\
        & \vdots & 
      \end{aligned}$$ 
      
      El sistema será estable si todos los términos de la primera columna de la matriz ($a_0, a_1, A_1, B_1, C_1, \ldots, W_1$) son positivos. Si alguno de estos elementos es negativo el sistema será inestable. Por cada    cambio de signo habrá una raíz con la parte real positiva.

El criterio de estabilidad de Routh presenta algunas limitaciones. No puede trata sistemas con retrasos (tiempos muertos) o no lineales. Sólo da información de si un sistema es estable o inestable, no da información de si un sistema estable está cerca o lejos de la inestabilidad. Otra limitación es la necesidad de tener que expresar la ecuación característica como un polinomio en $s$, esto puede ser bastante complicado en sistemas complejos.

Para encontrar qué valores de las constantes del controlador están situadas en el límite de estabilidad se debe resolver la siguiente ecuación:

$$W_1 s^2 + W_2 = 0$$

De esta manera se puede determinar un par de raíces de la ecuación característica con la parte real nula, es decir, situadas sobre el eje imaginario. Lógicamente $W_1$ y $W_2$ dependen de los parámetros del controlador.

```{admonition} Ejemplo
En el problema [\[prob802\]](#prob802){reference-type="ref"
reference="prob802"} se utiliza el criterio de Routh-Hurvitz para
demostrar la estabilidad de un lazo de control por retroalimentación.
```