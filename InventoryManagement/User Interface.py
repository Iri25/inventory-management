
from Domain import to_string
from Logic import save_to_file, read_from_file, get_object_by_id, add_object, remove_object, update_object, move_object, \
    concatenation_string, max_price_location, sorted_by__price, sum_price_location, undo

def show_menu():
    print('1. Adauga obiect')
    print('2. Sterge obiect')
    print('3. Modifica obiect')
    print('4. Mutarea tuturor obiectelor dintr-o sala in alta')
    print('5. Concatenarea unui string citit la toate descrierile obiectelor cu prețul mai mare decât o valoare citit')
    print('6. Determinarea celui mai mare preț pentru fiecare locație')
    print('7. Ordonarea obiectelor crescător după prețul de achiziți')
    print('8. Afișarea sumelor prețurilor pentru fiecare locație')
    print('9. Undo')
    print('a. Show all objects')
    print('x. Exit')

def ui_add_object(list_of_objects):
    try:
        id_object = int(input('Dati ID-ul: '))
        name = input('Dati numele: ')
        description = input('Dati descrierea: ')
        price = float(input('Dati pretul: '))
        location = input('Dati locatia: ')

        new_objects = add_object(list_of_objects, id_object, name, description, price, location)
        print('Obiect adaugat cu succes!')
        return new_objects
    except ValueError as ve:
        print('Eroare:', ve)
        return list_of_objects

def ui_show_all(list_of_objects):
    for object in list_of_objects:
        print(to_string(object))

def ui_remove_object(list_of_objects):
    try:
        id_object = int(input('Dati id-ul de sters: '))
        print('Rezervare stearsa!')
        return remove_object(list_of_objects, id_object)
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_update_object(list_of_objects):
    try:
        id_object = int(input('Dati id-ul obiectului de actualizat: '))
        name = input('Dati noul nume, gol pentru a nu schimba: ')
        description = input('Dati noua descriere, gol pentru a nu schimba: ')
        price = float(input('Dati noul pret, gol pentru a nu schimba: '))
        location = input('Dati noua locatie, gol pentru a nu schimba: ')

        list_of_objects = update_object(
            list_of_objects,
            id_object,
            name,
            description,
            price,
            location)
        print('Obiectul a fost actualizat!')
        return list_of_objects
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_move_object(list_of_objects):
    try:
        old_location = input('Da vechea locatie: ')
        new_location = input('Da noua locatie: ')
        list_of_objects = move_object(list_of_objects, old_location, new_location)
        print('Obiectul a fost mutat!')
        return list_of_objects
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_concatenation_string(list_of_objects):
    try:
        price = float(input('Pret dat: '))
        description = input('Descrierea data: ')
        list_of_objects = concatenation_string(list_of_objects, price, description)
        print('Stringul a fost concatenat!')
        return list_of_objects
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_max_price_location(list_of_objects):
    try:
        list_of_objects = max_price_location(list_of_objects)
        print('Preturile maxime pe locatii s-au afisat!')
        return list_of_objects
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_sorted_by__price(list_of_object):
    try:
        list_of_object = sorted_by__price(list_of_object)
        print('Preturile sunt sortate crescator!')
        return list_of_object
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_object

def ui_sum_price_location(list_of_objects):
    try:
        list_of_objects = sum_price_location(list_of_objects)
        print('Sumele pe locatii s-au afisat!')
        return list_of_objects
    except ValueError as ve:
        print('Eroare', ve)
        return list_of_objects

def ui_undo(lista):
    all = undo(lista)
    return all

def optiuneinput ():
    try:
        optiune = int(input('Alege o optiune: '))
    except ValueError:
        print('Optiune incorecta')
    return optiune

def main():
    lista = []
    list_of_objects = read_from_file()
    nr = 0
    while True:
        show_menu()
        option = input('Alege optiunea: ')
        if option == '1':
            nr += 1
            list_of_objects = ui_add_object(list_of_objects)
            save_to_file(list_of_objects)
            if not lista or lista[-1] != list_of_objects:
                lista += [list_of_objects]
            print(list_of_objects)
        elif option == '2':
            nr += 1
            list_of_objects = ui_remove_object(list_of_objects)
            if not lista or lista[-1] != list_of_objects:
                lista += [list_of_objects]
            print(list_of_objects)
        elif option == '3':
            nr += 1
            list_of_objects = ui_update_object(list_of_objects)
            if not lista or lista[-1] != list_of_objects:
                lista += [list_of_objects]
            print(list_of_objects)
        elif option == '4':
            nr += 1
            list_of_objects = ui_move_object(list_of_objects)
            if not lista or lista[-1] != list_of_objects:
                lista += [list_of_objects]
            print(list_of_objects)
        elif option == '5':
            nr += 1
            new_objects = ui_concatenation_string(list_of_objects)
            if not lista or lista[-1] != list_of_objects:
                lista += [list_of_objects]
            print(new_objects)
        elif option == '6':
            nr += 1
            if not lista or lista[-1] != max_price_location(list_of_objects):
                lista += [max_price_location(list_of_objects)]
            print(ui_max_price_location(list_of_objects))
        elif option == '7':
            if not lista or lista[-1] != sorted_by__price(list_of_objects):
                lista += [sorted_by__price(list_of_objects)]
            print(ui_sorted_by__price(list_of_objects))
        elif option == '8':
            if not lista or lista[-1] != sum_price_location(list_of_objects):
                lista += [sum_price_location(list_of_objects)]
            print(ui_sum_price_location(list_of_objects))
        elif option == '9':
            if len(lista) > 1:
                del lista[-1]
                list_of_objects = lista[-1]
                print(list_of_objects)
                print("Undo aplicat!")
            elif len(lista) == 1:
                print("Undo aplicat!")
            else:
                print("Nu poti merge inapoi")
                print(list_of_objects)
        elif option == 'a':
            ui_show_all(list_of_objects)
        elif option == 'x':
            save_to_file(list_of_objects)
            break

main()
