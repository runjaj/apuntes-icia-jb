# Problema 1.4

Explicar como el concepto económico conocido como la *ley de la oferta y
la demanda* se puede interpretar como un sistema de control por
retroalimentación. Escoger el precio del mercado de un artículo en
particular como la salida del sistema y suponer que el objetivo del
sistema es mantener la estabilidad en el precio

---
**Solución**

Se puede plantear el siguiente diagrama de bloques que describe el
funcionamiento de la ley de la oferta y la demanda:

%config InLineBackend.figure_format = 'svg'
import schemdraw
from schemdraw import dsp

d = schemdraw.Drawing(unit=1, fontsize=10)

d += dsp.Line().right().label('$\Delta_{sp}$', 'left')
d += dsp.Arrowhead().right().label('+', 'top')
d += (suma1 := dsp.Circle().anchor('W'))
d += dsp.Arrow().right().label('$\epsilon$', 'top')
d += (control := dsp.Box(h=1.5).anchor('W').label('Control de\nprecios'))
d += dsp.Line().right().at(control.E)
d += (punto1 := dsp.Dot(radius=0))
d += dsp.Arrow().right().label('Precio', 'right')
d += dsp.Line().down().at(punto1.center).length(2)
d += (punto2 := dsp.Dot(radius=0))
d += dsp.Arrow().left().label('$P$', 'top')
d += (ofertantes := dsp.Box(h=1.5).anchor('E').label('Ofertantes'))
d += dsp.Line().left().label('$O$', 'top').at(ofertantes.W)
d += dsp.Arrowhead().left().label('+', 'bot')
d += (suma2 := dsp.Circle().anchor('W'))
d += dsp.Line().up().at(suma2.S).to(suma1.S).label('$\Delta$', 'top')
d += dsp.Arrowhead().up().label('-', 'top')
d += dsp.Line().down().at(punto2.center).length(2)
d += dsp.Arrow().left().label('$P$', 'top')
d += (demandantes := dsp.Box(h=1.5).anchor('E').label('Demandantes'))
d += dsp.Line().left().label('$D$', 'top').at(demandantes.W).length(1.5)
d += dsp.Line().up().to(suma2.N)
d += dsp.Arrowhead().label('-', 'top')

d.draw()

donde:

-   $P$ es el precio

-   $D$ es la cantidad de producto demandada/año

-   $O$ es a cantidad de producto ofertada/año

-   $\Delta = O - D$, es la diferencia entre la cantidad de producto
    ofertada y demandada

-   $\Delta_{sp} = 0$, ya que el objetivo
    del mercado es igualar la oferta con la demanda a través de la
    variación de los precios

-   $\varepsilon = \Delta_{sp} - \Delta = D - O$,
    es el error del que alimenta al control de precios

Se puede comprobar cualitativamente que el sistema funciona. Por
ejemplo, si la cantidad de producto ofertada/año es mayor que la
cantidad demandada, $\Delta > 0$. Como consecuencia $\varepsilon < 0$,
lo que implica que el precio disminuye.