(transformada)=
# La transformada de Laplace como herramienta útil

La transformada de Laplace $\bar{f} (s)$ de una función $f (t)$ se
define como:

$$\mathcal{L} [f (t)] \equiv \bar{f} (s) = \int_0^{\infty} f (t) e^{- s t} d
   t$$ 

donde $t \in \mathbb{R}$ y $s \in \mathbb{C}$.

El uso de transformadas de Laplace ofrece un método simple y elegante de
resolver ecuaciones diferenciales como las que se obtienen en los
modelos matemáticos de los procesos alimentarios.

Entre las diferentes propiedades de las transformadas de Laplace cabe
destacar:

1.  Es un **operador lineal**:

    $$\mathcal{L} [a_1 f_1 (t) + a_2 f_2 (t)] = a_1 \mathcal{L} [f_1 (t)] + a_2
         \mathcal{L} [f_2 (t)]$$

2.  La **transformada de una derivada** es:

    $$\mathcal{L} \left[ \frac{d f (t)}{d t} \right] = s \bar{f} (s) - f (0)$$
    
    Es importante resaltar que una ecuación diferencial ordinaria de
    primer orden pasa a ser una ecuación lineal de primer grado.

    La transformada de la segunda derivada es:
        
    $$\mathcal{L} \left[ \frac{d^2 f (t)}{d t^2} \right] = s^2  \bar{f} (s) - s
         f (0) - f' (0)$$ 
    
    Generalizando:
    
    $$\mathcal{L} \left[ \frac{d^{(n)} f (t)}{d t^n} \right] = s^n  \bar{f} (s)
         - s^{n - 1} f (0) - s^{n - 2} f' (0) - \ldots - s f^{(n - 2)} (0) - f^{(n
         - 1)} (0)$$

    Esta propiedad permite resolver de manera sencilla ecuaciones
    diferenciales ya que las convierte en ecuaciones algebraicas. El
    Problema 2.3 muestra cómo se puede utilizar la transformada de
    Laplace para resolver una ecuación diferencial.

3.  La **transformada de Laplace de una integral** es:

    $$\mathcal{L} \left[ \int_0^t f (t) d t \right] = \frac{1}{s} \bar{f} (s)$$

4.  **Translación de la transformada**:

    $$\mathcal{L} [e^{- \alpha t} f (t)] = \bar{f} (\alpha + s)$$
    
    Translación de la función:
        
    ```{math}
    :label: translacion
    \mathcal{L} [f (t - t_0) U(t-t_0)] = e^{- t_0 s}  \bar{f}(s)
    ```

5.  **Teorema del valor final**:

    ```{math}
    :label: valor_final
    \mathcal{L} \left[ \underset{t \rightarrow \infty}{\lim} f (t) \right] = \underset{s \rightarrow 0}{\lim} [s \bar{f}(s)]
    ```

```{admonition} Ejemplo
La aplicación de la transformada de Laplace a una función es sencilla
disponiendo de las tablas de transformadas de Laplace y del conocimiento
de las propiedades anteriores. En el {ref}`prob301` se muestra cómo se
aplica.
```
