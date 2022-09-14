def creare_lista_int():
    lst = []
    n=int(input())
    for i in range(n):
        element = input('Introduceti un numar de tip integer: ')
        try:
            lst.append(int(element))
        except:
            while not element.isnumeric():
                element = input('Introdu iar, de data aceasta un numar int: ')
            lst.append(int(element))
    return lst


def creare_lista_float():
    lst = []
    n=int(input())
    for i in range(n):
        element = input('Introduceti un numar de tip float ')
        try:
            lst.append(float(element))
        except ValueError:
            while not element.isdecimal():
                element = input('Introdu iar, de data aceasta un numar float ')
            lst.append(float(element))
    return lst

# lista1=creare_lista_int()
# print(lista1)
lista2=creare_lista_float()
print(lista2)