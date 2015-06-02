import csv

__author__ = 'ivania'


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
            self.headers = reader.fieldnames
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
        aux_nombre = string.split(' ')
        if aux_nombre[0].isnumeric():
            aux_nombre = ' '.join(aux_nombre[1:])
        else:
            aux_nombre = ' '.join(aux_nombre[:])
        return aux_nombre

    @classmethod
    def corregir_numero_de_erres(cls, string):
        # Concatenación de r
        aux_texto = string.replace('rrr', '##')
        aux_texto = aux_texto.replace('rr', 'r')
        aux_texto = aux_texto.replace('##', 'rr')
        return aux_texto

    @classmethod
    def pasar_a_mayusculas(cls, string):
        return string.upper()

    def to_latex(self, file_name='alumnos.tex'):
        out = open(file_name, 'w')
        # Header archivo
        out_t = "\\begin{table}[h]\n\\begin{tabular}{|l|l|l|}\n\\hline\n"

        for h in self.headers:
            if h == "Nombre":
                out_t += h + "\\\\ \\hline\n"
            else:
                out_t += h + " & "

        out.write(out_t)

        for registro in self.students:
            out_t = "{0} & {1} & {2} \\\\ \\hline\n".format(
                registro.paterno, registro.materno, registro.nombre)
            out.write(out_t)

        out_t = "\end{tabular}\n \end{table}\n"
        out.write(out_t)
        out.close()

    def to_html(self, file_name='alumnos.html'):
        out = open(file_name, 'w')
        # Header archivo
        out_t = "<table>\n<tr>"

        for h in self.headers:
            out_t += "<th>{0}</th>".format(h)
        out_t += "</tr>"
        out.write(out_t)
        for registro in self.students:
            out_t = "<tr>\n<td>{0}</td>\n<td>{1}</td>\n<td>{2}</td>\n</tr>\n".format(
                registro.paterno, registro.materno, registro.nombre)
            out.write(out_t)

        out_t = "</table>"
        out.write(out_t)
        out.close()

    def to_markdown(self, file_name='alumnos.md'):
        out = open(file_name, 'w')
        # Header archivo
        out_t = "|"

        for h in self.headers:
            out_t += h + "|"
        out_t += "\n|------------|--------|---------|\n"
        out.write(out_t)
        out_t = ""
        for registro in self.students:
            out_t = "|{0}|{1}|{2}|\n".format(
                registro.paterno, registro.materno, registro.nombre)
            out.write(out_t)
        out.close()

if __name__ == '__main__':
    rescue_siding = RescueSiding()
    rescue_siding.to_latex()
    rescue_siding.to_html()
    rescue_siding.to_markdown()
