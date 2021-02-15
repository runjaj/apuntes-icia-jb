(transformadas)=
# Transformadas de Laplace

```{table} Transformadas de Laplace de funciones seleccionadas.

$\mathbf{f (t), t > 0}$ | $\mathbf{\bar{f}(s)}$
-------------------|------------------
Impulso unidad, $\delta(t_0)$ | 1
Pulso unidad, $\delta_A(t)$ | $\frac{1}{A}  \frac{1 - e^{- sA}}{s}$
Escalón unidad | $\frac{1}{s}$
Rampa, $f(t) = t$ | $\frac{1}{s^2}$
$t^2$ | $\frac{2!}{s^3}$
$t^n$ | $\frac{n!}{s^{n + 1}}$
$e^{- a t}$ | $\frac{1}{s + a}$
$t^n e^{- a t}$ | $\frac{n!}{(s + a)^{n + 1}}$
$\sin (\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$
$\cos (\omega t)$ | $\frac{s}{s^2 + \omega^2}$
$\sinh (\omega t)$ | $\frac{\omega}{s^2 - \omega^2}$
$\cosh (\omega t)$ | $\frac{s}{s^2 - \omega^2}$
$e^{- a t} \sin (\omega t)$ | $\frac{\omega}{(s + a)^2 + \omega^2}$
$e^{- a t} \cos (\omega t)$ | $\frac{s + a}{(s + a)^2 + \omega^2}$
```

```{table} Transformada inversa de Laplace de funciones seleccionadas.
 
  $\mathbf{\bar{f} (s)}$   |   $\mathbf{f (t)}$
  -------------------------|-----------
  $\frac{1}{(s + a)  (s + b)}$                              | $\frac{e^{- a t} - e^{- b t}}{b - a}$
  $\frac{1}{(s + a)  (s + b)  (s + c)}$                     | $\frac{e^{- a t}}{(b - a)  (c - a)} + \frac{e^{- b t}}{(c - b)  (a - b)} + \frac{e^{- a t}}{(a - c)  (b - c)}$
  $\frac{s + a}{(s + b)  (s + c)}$                          | $\frac{1}{c - b}  [(a - b) e^{- b t} -(a - c) e^{- c t}]$
  $\frac{a}{(s + b)^2}$                                     | $a t e^{- b t}$
  $\frac{a}{(s + b)^3}$                                     | $\frac{a}{2} t^2 e^{- b t}$
  $\frac{a}{(s + b)^{n + 1}}$                               | $\frac{a}{n!} t^n b^{- b t}$
  $\frac{1}{s (a s + 1)}$                                   | $1 - e^{- t / a}$
  $\frac{1}{s (a s + 1)^2}$                                 | $1 - \frac{a + t}{a} e^{- t / a}$
  $\frac{\omega^2}{s (s^2 + 2 \zeta \omega s + \omega^2)}$  | $1 + \frac{e^{-\zeta \omega t}}{ \sqrt[]{1 - \zeta^2}} \sin \left( \omega \sqrt[]{1- \zeta^2} t - \varphi \right)$ donde $\cos \varphi = - \zeta$
  $\frac{s}{(1 + a s)  (s^2 + \omega^2)}$                   | $- \frac{1}{1 + a^2 \omega^2}e^{- t / a} + \frac{1}{\sqrt[]{1 + a^2 \omega^2}} \cos (\omega t +\varphi)$ donde $\varphi = \arctan (a \omega)$
  $\frac{s}{(s^2 + \omega^2)^2}$                            | $\frac{1}{2 \omega} \sin (\omega t)$
  $\frac{1}{(s + a)  [(s + b)^2 + \omega^2]}$               | $\frac{e^{- a t}}{(a - b)^2+ \omega^2} + \frac{e^{- b t} \sin (\omega t + \varphi)}{\omega\sqrt[]{(a - b)^2 + \omega^2}}$ donde $\varphi = \arctan \left(\frac{\omega}{a - b} \right)$
```
