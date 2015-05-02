class Usuario:

    def __init__(self, rut, nombre, clave):
        self.rut = rut
        self.nombre = nombre
        self.clave = clave
        self.saldo = 0

    def depositar(self, monto):
        self.saldo += monto

    def retirar(self, monto):
        self.saldo -= monto


class Banco:

    def __init__(self, nombre):
        self.nombre = nombre
        self.usuarios = []

    def agregar_usuario(self, rut, nombre, clave):
        usuario = Usuario(rut, nombre, clave)
        self.usuarios.append(usuario)

    def verificar_login(self, rut, clave):
        self.usuarioactual = None
        for usuario in self.usuarios:
            if usuario.rut == rut:
                if usuario.clave == clave:
                    self.usuarioactual = usuario
                    return True
                else:
                    return False

    def buscar_tercero(self, rut):
        self.usuariotercero = None
        for usuario in self.usuarios:
            if usuario.rut == rut:
                self.usuariotercero = usuario
                return True
        return False

    def retirar(self, usuario, monto):
        usuario.retirar(monto)

    def depositar(self, usuario, monto):
        usuario.depositar(monto)


class CajeroAutomatico:

    def __init__(self, banco):
        self.banco = banco
        self.montomaximoretiro = 200000
        self.montomaximotransferencia = 1000000

    def login(self, rut, clave):
        if(self.banco.verificar_login(rut, clave)):
            print("Ha ingresado al Banco " + self.banco.nombre)
        else:
            print("No se ha podido ingresar al Banco")

    def retirar_dinero(self, rut, clave, monto):
        self.login(rut, clave)
        if(monto < self.montomaximoretiro):
            self.banco.retirar(self.banco.usuarioactual, monto)
            print("Ha retirado ", monto)
        else:
            print("Monto supera el maximo a retirar")

    def transferir_dinero(self, rut, clave, rut_destinatario, monto):
        self.login(rut, clave)
        print("entre")
        if (monto < self.montomaximotransferencia):
            self.banco.buscar_tercero(rut_destinatario)
            self.banco.retirar(self.banco.usuarioactual, monto)
            print("Se ha transferido ", monto)
        else:
            print("Monto supera el maximo a transferir")
