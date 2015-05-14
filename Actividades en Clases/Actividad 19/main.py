import csv


class Estudiante:

    def __init__(self, nombre, paterno, materno):
        self.nombre = nombre
        self.paterno = paterno
        self.materno = materno


class RescueSiding:

    def __init__(self, file_name='alumnos.csv'):
        self.students = [student for student in self.lector(file_name)]

    def lector(self, file_name='alumnos.csv'):
        with open(file_name) as file:
            reader = csv.DictReader(file)
            for row in reader:
                nombre = self.preparar_string(row['Nombre'])
                paterno = self.preparar_string(row['Apellido paterno'])
                materno = self.preparar_string(row['Apellido materno'])
                yield (Estudiante(nombre, paterno, materno))

    @classmethod
    def preparar_string(cls, string):
        result = cls.pasar_a_mayusculas(string)
        result = cls.corregir_numero_de_erres(result)
        result = cls.remover_numero_random_if_present(result)
        return result

    @classmethod
    def remover_numero_random_if_present(cls, string):
        #############
        # COMPLETAR #
        #############
        return string

    @classmethod
    def corregir_numero_de_erres(cls, string):
        #############
        # COMPLETAR #
        #############
        return string

    @classmethod
    def pasar_a_mayusculas(cls, string):
        #############
        # COMPLETAR #
        #############
        return string

    def to_latex(self, file_name='alumnos.tex'):
        #############
        # COMPLETAR #
        #############
        pass

    def to_html(self, file_name='alumnos.html'):
        #############
        # COMPLETAR #
        #############
        pass

    def to_markdown(self, file_name='alumnos.md'):
        #############
        # COMPLETAR #
        #############
        pass


if __name__ == '__main__':
    rescue_siding = RescueSiding()
    rescue_siding.to_latex()
    rescue_siding.to_html()
    rescue_siding.to_markdown()
