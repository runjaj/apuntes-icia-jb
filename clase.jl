using SymPy, Plots, LaTeXStrings, DSP, Roots, Interpolations

t, w = symbols("t omega", real=true)
@vars s

"""
L(f)

Encuentra la **trasnformada de Laplace** de la función f(t).
"""
L(f) = sympy.laplace_transform(f, t, s)

"""
iL(f)

Encuentra la **transformada inversa de Laplace** de la función
f(s).
"""
iL(f) = sympy.inverse_laplace_transform(f, s, t)

"""
**bode(Gol; wmin=1e-1, wmax=1e1, points=100, co=false, ra1=false)**

Representación del diagrama de Bode de la función de transferencia _Gol_.

Parámetros:

- `Gol`: Función de transferencia dependiente de _s_
- `wmin`: Frecuencia angular mínima a representar
- `wmax`: Frecuencia angular máxima a representar
- `points`: Número de puntos a representar
- `co`: Calcula y representa la frecuencia de cruce
- `ra1`: Calcula y representa la frecuencia que hace que _RA_ = 1

Ejemplo:

`salida = bode(20*(s+1)/s/(s+5)/(s^2+2s+10); wmax=10, co=true, ra1=true)`

El resultado se da como un diccionario. Para obtener los valores del ejemplo:

- Frecuencia de cruce: ```salida["wco"]```
- Frecuencia para _RA_ = 1: `salida["phi1"]`
"""
function bode(Gol; wmin=1e-1, wmax=1e1, points=100, co=false, ra1=false)
    Gw = Gol(s=>im*w)

    RAol = sqrt(real(Gw)^2+imag(Gw)^2)
    phiol = sympy.atan2(imag(Gw), real(Gw))
    
    # Hace una lista equiespaciada para los valores del log10 del desfase
    wlog = range(log10(wmin), log10(wmax); length=points)
    # Genera la versión lineal
    wlin = 10 .^wlog
    
    # Convierte la función del desfase a lenguajje Julia
    philam = lambdify(phiol)
    # Calcula los datos de desfase para los valores de frecuencia
    phidata = philam.(wlin)
    # Tiene en cuanta las "vueltas" del desfase
    DSP.unwrap!(phidata)
    # Calcularemos los valores del desfase mediante interpolación
    # lineal
    itp = LinearInterpolation(wlin,phidata)
    
    # Calculo de la frecuencia de cruce (desfase = -180°) 
    # y la RAco, si es necesario
    if co
        f(x) = itp(x)+pi
        wco = find_zero(f, (wmin, wmax))
        RAco = RAol(wco)
        phico = itp(wco)
    end
    
    #Cálculo de la frecuencia para RA=1 y su desfase
    if ra1    
        w1 = find_zero(RAol-1, (wmin, wmax))
        RA1 = RAol(w1)
        phi1 = itp(w1)
    end

    # Representación del diagrama de Bode
    l = @layout [a; b]
    RAplot = plot(RAol, wmin, wmax, xscale=:log10, yscale=:log10,
        legend=false, lw=2, xlabel="", ylabel="RA",
        minorticks=:auto)
    # Encuentra el valor mínimo de la escala del eje y 
    RAminscale = ylims(RAplot)[1]
    if co
        plot!([wmin, wco, wco],[RAco, RAco, RAminscale], color=:red, 
            annotations= (wco, float(RAco), text(L"w_{co}, RA_{co}", pointsize=10, :left)))
    end
    if ra1
        plot!([wmin, w1, w1], [RA1, RA1, RAminscale], color=:lime, 
            annotations= (w1, float(RA1), text(L"w_1, 1", pointsize=10, :left)))
    end
    phiplot = plot(wlin, phidata*180/pi, xscale=:log10,
        legend=false, lw=2, xlabel="ω", ylabel="φ",
        minorticks=:auto)
    phiminscale = ylims(phiplot)[1]
    if co
        plot!([wmin, wco, wco],[phico*180/pi, phico*180/pi, phiminscale],
            color=:red, annotations= (wco ,float(phico*180/pi), text(L"w_{co}, -180\degree",
                    pointsize=10, :left)))
    end
    if ra1
        plot!([wmin, w1, w1], [phi1*180/pi, phi1*180/pi, phiminscale], color=:lime,
        annotations = (w1, float(phi1*180/pi), text(L"w_1, \phi_1", pointsize=10, :left)))
    end
    
    # Muestra los gráficos 
    display(plot(RAplot, phiplot, layout=l))
    
    # Generación del diccionario con los valores de salida
    output = Dict()
    if co
        output["wco"] = wco
        output["RAco"] = RAco
        output["phico"] = phico
    end
    if ra1
        output["w1"] = w1
        output["RA1"] = RA1
        output["phi1"] = phi1
    end
    if co==false && ra1==false
        output = nothing
    end
    return output
end