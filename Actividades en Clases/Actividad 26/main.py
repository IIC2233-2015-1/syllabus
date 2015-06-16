import requests
import json
from classes import Student, ConsoleApp


__author__ = 'Patricio Lopez'


class SpyKiller:

    def __init__(self, my_name, my_username, url):
        self.my_username = my_username
        self.my_name = my_name
        self.url = url

    def mark_unassistent(self, victim):
        """
        Marca como inasistente a un estudiante, recibiendo su objeto Student.
        La peticion al servidor debe declarar 'assistance' y su valor booleano.
        """

        request = None

        #############
        # COMPLETAR #
        #############

        if request and request.status_code == 202:
            return "Devuelve el JSON de la response si fue exitosa"
        return "Devuelve un mensaje de error"

    def register_me(self):
        """
        Registra tu usuario en el servidor
        """
        username = self.my_username
        name = self.my_name
        assistance = True

        request = None

        #############
        # COMPLETAR #
        #############

        if request and request.status_code == 201:
            return "Devuelve el JSON de la response si fue exitosa"
        return "Devuelve un mensaje de error"

    def download_list(self):
        """
        Devuelve una lista de Student con todos los estudiantes en el servidor
        """

        students = []

        #############
        # COMPLETAR #
        #############

        return students


if __name__ == "__main__":
    spykiller = SpyKiller(
        my_name="NOMBRE_APELLIDO1_APELLIDO2",
        my_username="GITHUB_USERNAME",
        url="http://assistance-py.herokuapp.com"
    )

    ConsoleApp(spykiller).run()
