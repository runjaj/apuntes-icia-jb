# Cómo abordar la dinámica de un sistema

Este es un capítulo clave del temario ya que nos va a proporcionar la herramientas con las que podremos afrontar con éxito los siguientes temas. En este capítulo confluyen varias de las asignaturas que habéis estado viendo en los últimos años:

- _Matemáticas:_ Utilizaremos operadores matemáticos, números complejos, ecuaciones diferenciales, límites, métodos numéricos y propiedades trigonométricas. (Pista: los números complejos y las oscilaciones suelen ir de la mano, como ya habeis visto, por ejemplo, en electricidad con la corriente alterna.)

- _Operaciones básicas:_ Utilizaremos balances macroscópicos con el matiz interesante de que los realizaremos en estado no estacionario. Es una diferenicia importante respecto a cuando se utilizan para diseño, donde se suelen plantear las operaciones en estado estacionario.

El objetivo de esta capítulo es poder plantear modelos matemáticos de operaciones básicas que nos permitan poder simular su comportamiento, su dinámica, en el tiempo. Seguiremos esta secuencia:

1. Detallar el funcionamiento de la operación: Cuanto más conozcamos la operación, mejor será nuestro modelo matemático y las simulaciones serán más fiables

2. Plantear el modelo matemático de la operación utilizando balances no estacionarios, es decir, se tratará de ecuaciones diferenciales

2. Resolución de las ecuaciones diferenciales:
    - Solución analítica (si la hay): Resolver ecuaciones diferenciales, aunque sean ordinarias y no muy complejas, (como es nuestro caso) no es sencillo. Para simplificar la tarea recurrriremos a una herramienta matemática que facilita mucho su resolución: la transformada de Laplace.
    - Solución mediante métodos numéricos: Cuando no sea posible la obtención de soluciones analíticas, utilizarmos una herramienta de modelización y simulación informática que nos permitirá resolver numéricamente las ecuaciones diferenciales

```{warning}
En esta unidad se introducen muchos conceptos que, aunque no son difíciles una vez se dominan, requieren de práctica y un cierto pensamiento abstracto.

Hay que dedicar tiempo suficiente para practicar y asimilar las herramientas que se presentan, ya que su uso es clave en los temas siguientes.
```

La unidad se compone de los siguientes apartados:

**{numref}`%s <ejemplo_dinamica>`  {ref}`ejemplo_dinamica`:** Se explican los pasos a seguir para desarrollar el modelo matemático de una operación básica. Consideraremos que el modelo está terminado al plantear la ecuación o ecuaciones diferenciales.

**{numref}`%s <transformada>`  {ref}`transformada`:** Intoducción de la transformada de Laplace como una herramienta útil para resolver ecuaciones diferenciales. Se introducirá la definición del operador y sus principales propiedades.

**{numref}`%s <funcion_transferencia>` {ref}`funcion_transferencia`:** La función de transferencia nos permitirá trabajar con los modelos matemáticos sin tener que estar realizan la transformada de Laplace de manera continua.

**{numref}`%s <funciones_singulares>` {ref}`funciones_singulares`:** De cara a plantear las simulaciones es bueno conocer unas cuantas funciones matemáticas que, aunque son idealizaciones, son representativas de comportamientos del mundo real.

**{numref}`%s <inversion_transformadas>` {ref}`inversion_transformadas`:** Realizar la trasnformada de Laplace es sencillo, en cambio, realizar la operación inversa es mucho más complejo. Es una situación parecida a derivar e integrar. Las dos operaciones son importantes, pero resulta más complejo integrar que derivar. El problema es que es un paso imprescindible para obtener la solución de la ecuación diferencial planteada.

**{numref}`%s <expansion>`  {ref}`expansion`:** Técnicas para realizar la trasnformada inversa de Laplace.

**{numref}`%s <tablas_transformadas>` {ref}`tablas_transformadas`:** Se presentan las trasnformadas de Laplace y transformadas inversas de las funciones más habituales.

```{tip}
Aunque resolver las ecuaciones diferenciales, realizar las trasnformadas de Laplace y las transformadas inversas no es complicado, es un tarea tediosa.

Utilizaremos de manera habitual [Sympy](https://www.sympy.org), un [sistema algebráico computacional (_CAS_)](https://es.wikipedia.org/wiki/Sistema_algebraico_computacional), que nos eliminará gran parte del trabajo. Es recomendable saberlo utilizar, pero no es imprecindible para superar la asignatura.
```
