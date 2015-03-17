__author__ = 'Javiera'

from Properties import Persona

p = Persona(13, 'Javiera', 'jfastudillo@uc.cl')
print(p.name)

#Propertie nombre no tiene un setter, por lo que no puede ser modificado
# p.name = 'Vicente'

#Propertie nombre no tiene un deleter, por lo que no puede ser eliminado
# del p.name

#Mail no es válido
# p.mail = 'Vicho'

# Edad no es válida
# p.age = -9


