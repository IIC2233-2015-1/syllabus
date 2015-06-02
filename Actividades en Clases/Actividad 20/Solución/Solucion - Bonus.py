__author__ = "figarrido"


def crear_archivo_salida(nombre_ouput, sonido, arreglo_bytes, ayudas):
    """ Separa el arreglo de bytes entregado y escribe un archivo .wav
        con el sonido que se desea (este puede ser el primer sonido
        o el segundo, False o True respectivamente). Las ayudas son los bytes
        que para escribir el header del archivo .wav
    """
    largo_bytes = len(arreglo_bytes) // 2
    largo_en_bytes = largo_bytes.to_bytes(4, byteorder='little')
    largo_en_bytes_con_header = (largo_bytes + 36).to_bytes(4, byteorder='little')

    frecuencia = 11025 if not sonido else 22050
    frecuencia_en_bytes = frecuencia.to_bytes(4, byteorder='little')

    with open(nombre_ouput, 'wb') as archivo_separado:
        archivo_separado.write(ayudas[0:4])
        archivo_separado.write(largo_en_bytes_con_header)
        archivo_separado.write(ayudas[8:24])
        archivo_separado.write(frecuencia_en_bytes)
        archivo_separado.write(frecuencia_en_bytes)
        archivo_separado.write(ayudas[32:40])
        archivo_separado.write(largo_en_bytes)

        for i in range(len(arreglo_bytes) // 2):
            byte_audio = arreglo_bytes[
                2 * i + int(sonido)].to_bytes(1, byteorder='little')
            archivo_separado.write(byte_audio)

with open('../Enunciado/audio.wav', 'rb') as audio_raro:
    archivo_completo = bytearray(audio_raro.read(44))
    bytes_importantes = bytearray(audio_raro.read())


crear_archivo_salida('out1.wav', True, bytes_importantes, archivo_completo)
crear_archivo_salida('out2.wav', False, bytes_importantes, archivo_completo)
