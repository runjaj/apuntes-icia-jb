(expansion)=
# Expansión en fracciones parciales

Un método de inversión de transformadas de Laplace es la expansión en
fracciones parciales. Para invertir la función $\bar{f} (s)$ se reordena
como una suma de funciones simples:

$$\bar{f} (s) = \overline{f_1} (s) + \overline{f_2} (s) + \ldots +
   \overline{f_s} (s)$$

Una vez realizada la descomposición se realiza la inversión de
transformadas:

$$f (t) =\mathcal{L}^{- 1} [\overline{f_1} (s)] +\mathcal{L}^{- 1}
   [\overline{f_2} (s)] + \ldots +\mathcal{L}^{- 1} [\overline{f_s} (s)]$$

Normalmente las funciones a invertir en control de procesos aparecen
como fracciones de polinomios en *s* del tipo:

$$\bar{f} (s) = \frac{\bar{z} (s)}{\bar{p} (s)}$$

donde *z(s)* es un
polinomio de orden *m* y *p(s)* es un polinomio de orden *n*.

Para realizar la inversión de la transformada de Laplace se factoriza el
denominador:

$$\bar{f} (s) = \frac{z (s)}{(s - p_1)  (s - p_2) \ldots (s - p_n)}$$

donde $p_i$ son las raíces (ceros) del polinomio *p(s)*.

Si todos los $p_i$ son diferentes, se puede expresar *f(s)* como una
suma de *n* términos:

$$\bar{f} (s) = \frac{A}{s - p_1} + \frac{B}{s - p_2} + \frac{C}{s - p_3} +
   \cdots + \frac{W}{s - p_n}$$

Los numeradores de la ecuación anterior se evalúan de la siguiente
manera: 

$$\begin{aligned}
  & A = \lim_{s \to p_1} [(s - p_1) \bar{f} (s)]
  & \\
  & B = \lim_{s \to p_2} [(s - p_2) \bar{f} (s)]
  & \\
  & \vdots & \\
  & W = \lim_{s \to p_n} [(s - p_n) \bar{f} (s)]
  & \end{aligned}$$

Si existen raíces del denominador de *f(s)* repetidas, de nuevo se
expresa *f(s)* como un producto de fracciones simples. Por ejemplo, en
el caso de que una raíz se repita dos veces:

$$\bar{f} (s) = \frac{z (s)}{(s - p_1)^2  (s - p_3)  (s - p_4) \ldots (s -
   p_n)}$$
   
la descomposición en fracciones simples es:

$$\label{ec:dos raices} \bar{f} (s) = \frac{A}{(s - p_1)^2} + \frac{B}{s -
  p_1} + \frac{C}{s - p_3} + \cdots + \frac{W}{s - p_n}$$

Si la raíz se repite 3 veces (orden 3) la expansión sería así:

$$\begin{aligned}
  & \bar{f} (s) = \frac{z (s)}{(s - p_1)^3  (s - p_4)  (s - p_5) \ldots (s -
  p_n)} &  \nonumber\\
  & \label{ec:tres raices} \bar{f} (s) = \frac{A}{(s - p_1)^3} + \frac{B}{(s
  - p_1)^2} + \frac{C}{s - p_1} + \frac{D}{s - p_4} + \cdots + \frac{W}{s -
  p_n} & \end{aligned}$$

Los numeradores de la ecuación
[\[ec:dos raices\]](#ec:dos raices){reference-type="ref"
reference="ec:dos raices"} se calculan de la siguiente manera:

$$\begin{aligned}
  & A = \lim_{s \to p_1} [(s - p_1)^2  \bar{f}
  (s)] & \\
  & B = \lim_{s \to p_1} \left\{
  \frac{\mathrm{d}}{\mathrm{d}s} [(s - p_1)^2  \bar{f} (s)] \right\} & \\
  & C = \lim_{s \to p_3} [(s - p_3) \bar{f} (s)]
  & \\
  & \vdots & \end{aligned}$$ 
  
Para encontrar el numerador *C* de la
ecuación [\[ec:tres raices\]](#ec:tres raices){reference-type="ref"
reference="ec:tres raices"} se debe tomar la segunda derivada.
Generalizando al término $A_j$ de una raíz de orden *N* en $p_1$:

$$A_j = \lim_{s \to p_1} \left\{ \frac{\mathrm{d}^{m
   - 1}}{\mathrm{d}s^{m - 1}}  [(s - p_1)^N  \bar{f} (s)] \right\}  \frac{1}{(m -
   1) !}$$

Aunque su utilización es un tanto tediosa existen casos, como el
apartado d) del problema 3.2, que muy difícilmente se puede resolver sin
utilizar la técnica de expansión en fracciones parciales. Esta técnica
tiene la ventaja de ser muy sistemática.

```julia
using SymPy
s, t = symbols("s t")
apart(3*s+3/(2*s^2+s+1))
```
