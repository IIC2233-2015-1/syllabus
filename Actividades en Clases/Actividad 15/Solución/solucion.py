import unittest
from banco import Banco, CajeroAutomatico


class TestCajeros(unittest.TestCase):

    def setUp(self):
        self.banco = Banco("Seguritas")
        self.rut1 = "18.375.852-2"
        self.nombre1 = "Alberto Rodriguez"
        self.clave1 = 2345
        self.rut2 = "13.432.113-k"
        self.nombre2 = "Fernanda Pereira"
        self.clave2 = 5912
        self.banco.agregar_usuario(self.rut1, self.nombre1, self.clave1)
        self.banco.agregar_usuario(self.rut2, self.nombre2, self.clave2)
        self.cajero = CajeroAutomatico(self.banco)

    def test_credenciales(self):
        # primer caso: rut y clave correctos
        self.cajero.login(self.rut1, self.clave1)
        rutingresado = self.banco.usuarioactual.rut
        self.assertEqual(self.rut1, rutingresado)
        # segundo caso: rut correcto pero clave incorrecta
        self.cajero.login(self.rut1, 1234)
        self.assertIsNone(self.banco.usuarioactual)
        # tercer caso: rut no está en la base de datos del banco
        self.cajero.login("10.000.000-1", 1234)
        self.assertIsNone(self.banco.usuarioactual)

    def test_dinero_disponible(self):
        self.cajero.retirar_dinero(self.rut1, self.clave1, 20000)
        saldo = self.banco.usuarioactual.saldo
        # el usuario debería tener saldo 0, ya que nunca ha depositado
        self.assertEqual(0, saldo)
        # el test falla y se aprecia que el saldo queda en -20.000 cuando
        # debería ser 0

    def test_monto_actualizado(self):
        self.cajero.login(self.rut1, self.clave1)
        # se depositan 10.000 pesos
        self.banco.depositar(self.banco.usuarioactual, 10000)
        # se retiran 5.000 pesos
        self.cajero.retirar_dinero(self.rut1, self.clave1, 5000)
        saldo = self.banco.usuarioactual.saldo
        # deberían quedar 5.000 pesos en el saldo
        self.assertEqual(5000, saldo)

    def test_cuenta_tercero(self):
        # trataremos de transferir a una cuenta que no existe
        self.cajero.login(self.rut1, self.clave1)
        self.banco.depositar(self.banco.usuarioactual, 10000)
        self.cajero.transferir_dinero(
            self.rut1, self.clave1, "1.000.000-3", 5000)
        self.assertIsNone(self.banco.usuariotercero)
        # efectivamente el usuario al que se le va transferir no se crea y no
        # es encontrado

    def test_montos_actualizados(self):
        self.cajero.login(self.rut1, self.clave1)
        # a la cuenta 1 se le deposita 15.0000
        self.banco.depositar(self.banco.usuarioactual, 15000)
        # la cuenta 1 le transfiere 5.000 a la cuenta 2
        self.cajero.transferir_dinero(self.rut1, self.clave1, self.rut2, 3000)
        # la cuenta 1 queda con 12.000 y la cuenta 2 con 3.000. Comprobémoslo
        montoUsuario = self.banco.usuarioactual.saldo
        montoTercero = self.banco.usuariotercero.saldo
        # cuenta 1 tiene 12.000
        self.assertEqual(montoUsuario, 12000)
        # cuenta 2 tiene 3.000
        self.assertEqual(montoTercero, 3000)
        # vemos que no se cumple que el tercero tenga 3.000 (de hecho tiene 0)
        # concluimos que a la cuenta 1 se le retiran 3.000 pero a la
        # cuenta 2 no están llegando los 3.000
        # Falla el test

    def test_comprobar_error(self):
        # un error que podría pasar es que el tercero no exista
        self.cajero.login(self.rut1, self.clave1)
        # a la cuenta 1 se le deposita 10.0000
        self.banco.depositar(self.banco.usuarioactual, 10000)
        # transferimos a una cuenta que no existe
        self.cajero.transferir_dinero(
            self.rut1, self.clave1, "1.000.000-3", 5000)
        # verifiquemos que no se hace la transferencia
        montoUsuario = self.banco.usuarioactual.saldo
        self.assertEqual(montoUsuario, 10000)
        # vemos que igual se sacan los 5.000 a pesar del error
        # Falla el test


if __name__ == "__main__":
    unittest.main()
