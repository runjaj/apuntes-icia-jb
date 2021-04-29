# Influencia de los retrasos

Para todos los sistemas considerados en los apartados anteriores se ha supuesto que cualquier cambio en la entrada se reflejaba instantáneamente en la salida. Este hecho contradice la evidencia física, prácticamente todo proceso lleva un retraso entre la entrada y la salida. Normalmente este retraso es despreciable excepto en los casos siguientes que presentan retrasos elevados:

-   Procesos en los que haya transporte de fluidos a largas distancias o que incluyan fenómenos con periodos largos de incubación

-   Dispositivos de medida que requieran tiempos de muestreo o de análisis elevados. Por ejemplo, cromatografía de gases

-   Elementos finales de control que necesiten un cierto tiempo para actuar

-   Un controlador humano que necesita tiempo para pensar y tomar una decisión

Los bucles de control por retroalimentación que presentan alguno de estos elementos tienen los siguientes problemas:

-   Una perturbación que entre en el proceso no será detectada hasta que haya pasado una cantidad de tiempo significativa

-   La acción de control se realizará a partir de la última medida tomada que será inadecuada debido a que no representa correctamente lo que está ocurriendo en el proceso

-   No se puede apreciar la acción de control sobre el sistema hasta un cierto tiempo después

-   Como resultado de la combinación de los factores anteriores la presencia de tiempos muertos (retrasos) es una fuente de inestabilidad de los lazos de control

Los procesos con retraso son difíciles de controlar ya que la salida no contiene la información de lo que está ocurriendo en el proceso en este momento.
