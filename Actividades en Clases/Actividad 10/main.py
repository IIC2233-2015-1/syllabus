# debes definir la metaclase 'Meta' a continuacion


# debes definir las clases 'Person' y 'Company' a continuacion


# El resto es para probar tu programa
if __name__ == '__main__':

    c = Company()
    c.name = 'Apple'
    c.stock_value = 125.78
    c.employees = ['Tim Cook', 'Kevin Lynch']

    print(c.name, c.stock_value, c.employees, sep=', ')

    p = Person()
    p.name = 'Karim'
    p.age = 'hola'
    # Esto debiese imprimir 'ERROR'

    print(p.name, p.age, sep=', ')
