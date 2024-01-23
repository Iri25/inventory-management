from Domain import create_object, get_id, get_name, get_description, get_price, get_location
from Logic import add_object, remove_object, update_object, move_object, concatenation_string, max_price_location, sorted_by__price, sum_price_location

def test_add_object():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1), get_price(object1), get_location(object1))
    assert list_of_objects == [object1]
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3.0, 'banca')
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects2), get_name(list_of_objects2), get_description(list_of_objects2), get_price(list_of_objects2), get_location(list_of_objects2))
    assert list_of_objects == [object1, list_of_objects2]
test_add_object()


def test_remove_object():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3.0, 'banca')
    list_of_objects3 = create_object(3, 'telefon', 'Samsung', 677.0, 'S33')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1), get_price(object1), get_location(object1))
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects2), get_name(list_of_objects2), get_description(list_of_objects2), get_price(list_of_objects2), get_location(list_of_objects2))
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects3), get_name(list_of_objects3), get_description(list_of_objects3), get_price(list_of_objects3), get_location(list_of_objects3))
    list_of_objects = remove_object(list_of_objects, get_id(list_of_objects2))
    assert list_of_objects == [object1, list_of_objects3]
test_remove_object()

def test_update_object() :
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1), get_price(object1), get_location(object1))
    assert list_of_objects == [object1]
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3.0, 'banca')
    list_of_objects = update_object(list_of_objects, get_id(list_of_objects2), get_name(list_of_objects2), get_description(list_of_objects2), get_price(list_of_objects2), get_location(list_of_objects2))
    assert list_of_objects == [list_of_objects2]



def test_move_object():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3.0, 'banca')
    list_of_objects3 = create_object(3, 'telefon', 'Samsung', 677.0, 'S33')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1),
                          get_price(object1), get_location(object1))
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects2), get_name(list_of_objects2), get_description(list_of_objects2),
                          get_price(list_of_objects2), get_location(list_of_objects2))
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects3), get_name(list_of_objects3), get_description(list_of_objects3),
                          get_price(list_of_objects3), get_location(list_of_objects3))
    list_of_objects = move_object(list_of_objects, get_location(list_of_objects2))
    assert list_of_objects == [object1, list_of_objects2, list_of_objects3]

def test_max_price_location():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects = add_object(list_of_objects, dict, get_id(object1), get_name(object1), get_description(object1),
                          get_price(object1), get_location(object1))
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3, 'banca')
    list_of_objects = add_object(list_of_objects, dict, get_id(list_of_objects2), get_name(list_of_objects2), get_description(list_of_objects2),
                          get_price(list_of_objects2), get_location(list_of_objects2))
    list_of_objects3 = create_object(5.5, 'foaie', 'roz', 1, 'masa')
    list_of_objects = add_object(list_of_objects, dict, get_id(list_of_objects3), get_name(list_of_objects3), get_description(list_of_objects3),
                          get_price(list_of_objects), get_location(list_of_objects3))
    list_of_objects4 = create_object(80, 'caiet', 'verde', 5.5, 'banca')
    list_of_objects = add_object(list_of_objects, dict, get_id(list_of_objects4), get_name(list_of_objects4), get_description(list_of_objects4),
                          get_price(list_of_objects4), get_location(list_of_objects4))
    max_price = {}
    max_price = max_price_location(list_of_objects)
    assert max_price == {'masa': object1, 'banca': list_of_objects4}


def test_sorted_by__price():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1),
                          get_price(object1), get_location(object1))
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3, 'banca')
    list_of_objects = sorted_by__price(list_of_objects)
    assert list_of_objects == [list_of_objects2, object1]



def test_sum_price_location():
    list_of_objects = []
    object1 = create_object(1, 'penar', 'rosu', 20.0, 'masa')
    list_of_objects = add_object(list_of_objects, get_id(object1), get_name(object1), get_description(object1),
                          get_price(object1), get_location(object1))
    list_of_objects2 = create_object(2, 'caiet', 'alb', 3.0, 'banca')
    list_of_objects3 = create_object(5.5, 'foaie', 'roz', 1.0, 'masa')
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects3), get_name(list_of_objects3), get_description(list_of_objects3),
                          get_price(list_of_objects), get_location(list_of_objects3))
    list_of_objects4 = create_object(80, 'caiet', 'verde', 5.5, 'banca')
    list_of_objects = add_object(list_of_objects, get_id(list_of_objects4), get_name(list_of_objects4), get_description(list_of_objects4),
                          get_price(list_of_objects4), get_location(list_of_objects4))
    sum_price = {}
    sum_price = sum_price_location(list_of_objects)
    assert sum_price == {'masa': 21.0, 'banca':80}

