def imprimir_tabla_posiciones(tabla):
    print("_"*90)
    print(f"{'Nombre':<15} {'Puntaje':>10} / {'Rondas Ganadas':>10} / {'Mejor ronda':>10} / {'Promedio':>10}")
    nueva = sorted(tabla.items(), key=lambda x: x[1]['Puntaje'], reverse=True)
    for nombre, stats in nueva:
        print(f"{nombre:<15} {stats['Puntaje']:>10} {stats['Rondas Ganadas']:>10} {stats['Mejor ronda']:>10} {stats['Promedio']:>10.2f}")
    print("_"*90)

def sumar_tabla(tabla,puntos,ronda):
    puntMax = -1
    ganando = None
    for nombre in tabla.keys():
        tabla[nombre]['Puntaje'] += sum(puntos[nombre].values())
        tabla[nombre]['Promedio'] = tabla[nombre]['Puntaje']/ronda
        if sum(puntos[nombre].values()) > puntMax:
            ganando = nombre
            puntMax = sum(puntos[nombre].values())
    print(f"Ganador: {ganando}({puntMax})")
    tabla[ganando]['Rondas Ganadas'] += 1
    if tabla[ganando]['Mejor ronda'] < puntMax:
        tabla[ganando]['Mejor ronda']= puntMax
        
    