
def func_verificadora(email):
    comp = email.split("@")  # Componentes
    if not len(comp) == 2:  # Exactamente un "@"
        return False
    if not comp[0] or not comp[1]:  # Antes y después de @ no vacíos
        return False
    dom = comp[1].split(".")  # Sub dominios
    if not dom[-1] == "cl":  # Solo dominios chilenos
        return False
    for d in dom:
        # Ningún sub dominio puede ser vacío.
        # Se asume que puntos sepran sub dominios.
        if not d:
            return False
    return True
