# Problema 8.1

Estimar la estabilidad de un sistema de control autimático cuya función de transferencia de lazo abierto es:

$$GH=\frac{9}{(10 s+1)^3}$$

---

**Solución**

Para determinar si el lazo de control es estable se puede utilizar el criterio de Routh. La ecuación característica de este sistema es:

$$\begin{aligned}
  1 + G H = 0\\
  1 + \frac{9}{(10 s + 1)^3} = 0\\
  1000 s^3 + 300 s^2 + 30 s + 10 = 0
\end{aligned}$$ 

La matríz de Routh es:

$$\begin{array}
     1000 & 30\\
     300 & 10\\
     -3.33 & 
     \end{array}$$
     
La primera columna tiene un signo negativo, lo que implica que es sistema es inestable.