###Solución###


class MetaEmpresa(type):

    first = True

    def __new__(meta, namecls, bases, dicc):
        if not(namecls == 'Empresa'):
            raise NameError('El nombre de la clase no es correcto')

        def subir_sueldo(self, id_empleado, password):
            if self.boss.password == password:
                self.empleados[id_empleado].sueldo *= 2

        def nuevo_empleado(self, empleado):
            if empleado.__class__.__name__ == 'Empleado':
                self.empleados[empleado.id_empleado] = empleado

        dicc['nuevo_empleado'] = nuevo_empleado
        dicc['subir_sueldo'] = subir_sueldo

        print('Creando empresa...\n')
        
        return super().__new__(meta, namecls, bases, dicc)

    def __call__(cls, *args, **kwargs):
        if kwargs == {}:
            MetaEmpresa.first = not MetaEmpresa.first
            return super().__call__(*args, **kwargs)
        elif 'empresa' in kwargs and kwargs['empresa'].__class__.__name__ == 'Empresa':
            s = 0
            for ID in kwargs['empresa'].empleados:
                s += kwargs['empresa'].empleados[ID].sueldo
            s += kwargs['empresa'].boss.sueldo
            return 'La empresa debe gastar en sus trabajadores ${}'.format(s)
        else:
            raise AttributeError('No es una Empresa')



class MetaPersona(type):

    def __new__(meta, namecls, bases, dicc):
        if namecls not in ['Persona', 'Empleado', 'Jefe']:
            raise NameError('El nombre de la clase no es correcto')

        def hacer_tarea(self, tarea):
            print('{} tiene que {}'.format(self.nombre, tarea))
            print('Realizando tarea...')
            print('Termine de {}'.format(tarea), '\n')

        dicc['__call__'] = hacer_tarea
        return super().__new__(meta, namecls, bases, dicc)
