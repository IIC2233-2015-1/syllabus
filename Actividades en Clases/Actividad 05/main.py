from estaciones_metro import Direccion, MapaMetro, Estacion


# Retornar true si existe un camino desde la estacion_origen a
# la estacion_destino, false en caso contrario.
# Solo puede controlar las variables estacion_origen y
# estacion_destino , no el mapa.

# Por ejemplo puedes hacer:
#   estacion_origen.izquierda.izquierda

def camino(estacion_origen, estacion_destino):
    # ==========
    # COMPLETAR
    # ==========
    return False


if __name__ == "__main__":
    mapa = MapaMetro.mapa_de_ejemplo()
    print(camino(mapa.primera_estacion, mapa.estaciones[10]))
    print(camino(mapa.estaciones[1], mapa.primera_estacion))
    print(camino(mapa.estaciones[9], mapa.estaciones[14]))
    print(camino(mapa.primera_estacion, mapa.primera_estacion))
    print(camino(mapa.primera_estacion, mapa.ultima_estacion))
