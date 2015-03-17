__author__ = 'Javiera'

class Persona():

    def __init__(self, age, name, mail):

        #_atributo: el _ al principio de un nombre de algún campo indica que se supone que sea privado
        # aunque en la práctica en c# no existen privados.
        self._age = age
        self._name = name
        self._mail = mail

    #SIN DESCRIPTOR
    #hagamos una restricción de integridad: age no puede ser negativo
    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age < 0:
            raise ValueError("Must be >= 0")
        else:
            self._age = new_age

    def del_age(self):
        del self._age

    age = property(get_age, set_age, del_age)

    #CON DESCRIPTOR
    # No queremos que desde otras clases/objetos modifiquen name (read only) ni lo eliminen
    @property
    def name(self):
        """Soy el property de name"""
        return self._name

    # Si modifican mail, debe ser por una dirección de mail válida
    @property
    def mail(self):
        return self._mail

    @mail.setter
    def mail(self, new_mail):
        if '@' in new_mail:
            self._mail = new_mail
        else:
            raise ValueError("This mail is not valid")

    @mail.deleter
    def mail(self):
        del self._mail





