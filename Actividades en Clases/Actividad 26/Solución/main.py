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

        # Solucion ------------------------------------------------------------
        request = requests.patch(
            url="{}/students/{}".format(self.url, victim.id),
            params={"assistance": False}
        )
        # ---------------------------------------------------------------------

        if request and request.status_code == 202:
            return request.json()
        return request.text  # Error

    def register_me(self):
        """
        Registra tu usuario en el servidor
        """
        username = self.my_username
        name = self.my_name
        assistance = True

        # Solucion ------------------------------------------------------------
        params = {'username': username,
                  'name': name,
                  'assistance': assistance}

        request = requests.post(url="{}/students".format(self.url),
                                params=params)

        if request and request.status_code == 201:
            return request.json()

        else:
            # Opcional: si ya me crearon, me aseguro de ponerme como asistente.
            me = next((s for s in self.download_list() if
                       s.username.lower() == username.lower()), None)

            request = requests.patch(
                url="{}/students/{}".format(self.url, me.id),
                params={"assistance": True}
            )

            if request and request.status_code == 202:
                return request.json()
        # -----------------------------------------------------------------------

        return request.text  # Error

    def download_list(self):
        """
        Devuelve una lista de Student con todos los estudiantes en el servidor
        """

        # Solucion ------------------------------------------------------------
        students = []
        request = requests.get(url="{}/students".format(self.url))
        for dic in request.json()['students']:
            students.append(
                Student(id=dic['id'],
                        name=dic['name'],
                        username=dic['username'],
                        assistance=dic['assistance'])
            )
        # -----------------------------------------------------------------------

        return students


if __name__ == "__main__":
    spykiller = SpyKiller(
        my_name="NOMBRE_APELLIDO1_APELLIDO2",
        my_username="GITHUB_USERNAME",
        url="http://assistance-py.herokuapp.com"
    )

    ConsoleApp(spykiller).run()
