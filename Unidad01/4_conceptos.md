(conceptos)=
# Conceptos generales
````{margin}
```{tip}
En el {ref}`prob101` a) se muestra la diferencia existente en un sistema de control de un tostador de pan si el control es de lazo abierto (control en adelanto) o si es de lazo cerrado (control por retroalimentación).
```
````

1.  **Dinámica**: Comportamiento de un proceso dependiente del tiempo. En la teoría del control se estudia básicamente la dinámica de dos
    tipos de sistema:


    1.  *Sistema de lazo abierto*: Respuesta del sistema sin
        controladores o con un control en adelanto (*feedforward*).

    2.  *Sistema de lazo cerrado*: Comportamiento del sistema incluido
        un control por retroalimentación (*feedback*).
        
  
2. **Variables**: A continuación se definen los diferentes tipos de variables implicados en la dinámica y control de sistemas:

    1.  *Variables manipulables*: Elementos del proceso que se pueden
        modificar para controlar la planta. Normalmente se trata de
        caudales.

    2.  *Variables controladas*: Parámetros de proceso --caudales,
        niveles, temperaturas, presiones, etc.-- que se quieren
        controlar, ya sea para mantenerlos constantes o para seguir una
        cierta evolución con el tiempo.

    3.  *Variables no controladas*: Variables del proceso que no son
        controladas aunque pueden ser medidas.

    4.  *Perturbaciones*: Entradas al proceso que no pueden ser
        controladas pero que deben tener un valor fijo en el proceso.

3.  **Consigna (*Set point*)**: Es el valor deseado de la variable a
    controlar. Puede ser constante o variar con el tiempo.

4.  **Control en adelanto (*Feedforward*)**: Se trata de un sistema de
    control de lazo abierto. Se detecta la perturbación cuando entra en
    el proceso y se realiza el cambio necesario en las variables
    manipulables para que la variable controlada se mantenga constante.

    ````{margin}
    ```{tip}
    Se muestra un sistema de control en adelanto en el {ref}`prob101` b).
    Se trata del sistema de control de una lavadora.
    ```
    ````

    Para este sistema es necesaria una calibración del sistema de
    control. Es importante resaltar que no se mide en ningún momento la
    variable controlada.

    ````{margin}
    ```{tip}
    En el apartado c) del {ref}`prob101` se muestra que el sistema de
    control automático de un avión es un sistema de control por
    retroalimentación.
    ```
    ````
5.  **Control por retroalimentación (*Feedback*)**: Se mide la variable
    controlada a la salida del proceso y se compara con la consigna (el
    valor deseado de la variable controlada). La diferencia (error) se
    alimenta al controlador por retroalimentación que modifica la
    variable manipulable.

    ````{margin}
	```{tip}
	En el {ref}`prob102` hay una discusión sobre las ventajas e inconvenientes del control por retroalimentación y en adelanto de un  sistema de control de temperatura de un edificio.
 	```
 	````
	```{list-table} Comparativa de los controladores en adelanto y los controladores por retroalimentación.
	:name: comparativa 
	:header-rows: 1

	* - **Feedforward**  
	  -  **Feedback** 
	* - *Ventajas*
	  -  
	* - 1\. Actúa antes de que la perturbación sea introducida en el sistema. 
	  - 1\. No inicia la acción de control hasta que aparece la perturbación.
	* - 2\. Bueno para sistemas lentos (multicapacidad) o con tiempos muertos significativos. 
	  - 2\. Es insatisfactorio para procesos lentos con tiempos muertos significativos.
	* - 3\. No introduce inestabilidad debida a la respuesta de ciclo cerrado. 
	   - 3\. La respuesta de bucle cerrado puede crear inestabilidad.
	* - 4\. Requiere un buen conocimiento del modelo del proceso.                       
	  - 4\. No es necesario el conocimiento del modelo del proceso.
	* - 5\. No requiere la identificación y medida de  todas las perturbaciones. 
	  - 5\. Requiere la identificación de las posibles  perturbaciones y su medida directa.
	* - 6\. Es insensible a los errores de modelado. 
	  - 6\. No puede operar con perturbaciones no  medibles.
	* - 6\. Es insensible a los cambios de parámetros. 
	  - 6\. Sensible a las variaciones de los parámetros del proceso.
	 ```

6.  **Estabilidad**: Un proceso es inestable si su salida se va haciendo
    mayor (positiva o negativamente) con el tiempo.

    La mayoría de los sistemas de lazo abierto son estables. Todos los
    sistemas de lazo cerrado son inestables si la ganancia del
    controlador se hace los suficientemente grande. Normalmente el
    rendimiento del controlador aumenta con la ganancia, pero disminuye
    su tolerancia a los cambios de parámetros del proceso.

7.  **Control analógico**: En este caso los datos son medidos de manera
    continua en el tiempo.

8.  **Control digital**: Se da cuando los datos son medidos de manera
    discreta ya sea debido a la utilización de computadores digitales o
    debido a métodos de medida muy lentos en comparación con la dinámica
    del proceso. P.ej., análisis mediante cromatografía.

9.  **Leyes del Control de Procesos**:

    1.  *Primera ley*: El sistema de control más simple es el que mejor
        funcionará.

    2.  *Segunda ley*: Se debe entender el proceso antes de intentar
        controlarlo.

10. **Elementos físicos de un sistema de control**:

    1.  *Instrumentos de medida o sensores*: Son los elementos de
        control encargados de medir las perturbaciones, las variables
        controladas, etc. Son las principales fuentes de información de
        cómo va el proceso. Un elemento crucial para la selección de un
        sensor es su capacidad de transmitir información fácilmente.
        P.ej., es preferible un termopar a un termómetro de mercurio.

    2.  *Transductores*: Elementos del sistema de control que convierten
        magnitudes físicas que no pueden ser utilizadas para el control
        en otras que sí lo pueden ser (una corriente eléctrica o una
        señal neumática, p.ej.). P.ej., convertir una señal de presión
        en una señal eléctrica.

    3.  *Lineas de transmisión*: Llevan la señal desde el sensor al
        controlador y del controlador al elemento final de control. La
        transmisión acostumbra a ser eléctrica o neumática.
        Frecuentemente se debe amplificar la señal del sensor antes de
        transmitirla.

    4.  *Controlador*: Recibe las señales de los sensores y decide la
        acción que se debe tomar.

    5.  *Elemento final de control*: Es el dispositivo físico que lleva
        a cabo la decisión del controlador. Típicamente es una válvula
        aunque también puede ser una bomba de velocidad variable, una
        compuerta, \...

    6.  *Registradores*: Proveen de un soporte visual y registro
        histórico del funcionamiento del sistema.
