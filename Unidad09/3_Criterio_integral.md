# Método del criterio integral con el tiempo

En este método se toma la respuesta dinámica del sistema de control. En lugar de caracterizarla con un solo parámetro, como en el apartado anterior, se utilizará toda la curva desde $t = 0$ hasta $t \to \infty$. La sintonía del controlador se realizará minimizando una de las siguientes integrales con el tiempo:

1.  Integral del error al cuadrado (*Integral of the square error*):

    $$\mathrm{ISE} = \int_0^{\infty} \varepsilon^2 (t) \mathrm{d}t$$

    Se minimiza esta integral cuando se desea eliminar errores grandes, ya que estos son los que más contribuyen al valor de la integral.

2.  Integral del valor absoluto del error (*Integral of the absolute valor of the error*):

    $$\mathrm{IAE} = \int_0^{\infty} | \varepsilon (t) | \mathrm{d}t$$
    
    En este caso se trata de eliminar errores pequeños. Estos errores podrían ser muy difíciles de eliminar minimizando la ISE ya que al elevarlos al cuadrado se hace todavía más pequeños respecto a los errores grandes.

3.  Integral del valor absoluto del error ponderado con el tiempo (*Integral of the time-weighted absolute error*):

    $$\mathrm{ITAE} = \int_0^{\infty} t | \varepsilon (t) | \mathrm{d}t$$
    
    Se utiliza cuando se desea eliminar errores muy persistentes en el tiempo, ya que la integral amplifica los errores que permanecen durante tiempos largos, incluso cuando se trata de errores pequeños

