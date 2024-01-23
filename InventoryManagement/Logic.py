import json
from copy import deepcopy

from Domain import create_object, get_id, get_name, get_description, get_price, get_location, to_string


def save_to_file(list_of_objects):
    """
        Saves a list of objects to file as json.
        :param list_of_objects: the list of objects
        :return: -
    """
    with open('Objects.txt', 'w') as f_out:
        f_out.write(json.dumps(list_of_objects))


def read_from_file():
    """
        Reads a list of objects from a file containing json
        :return: a list of objects
    """
    try:
        with open('Objects.txt', 'r') as f_in:
            return json.loads(f_in.read())
    except FileNotFoundError:
        return []


def get_object_by_id(list_of_objects, id_object):
    """
        Gets an objects with a given id.
        :param list_of_objects: the list of objects.
        :param id_object: the ID to search for.
        :return: an object with id=id_object
    """
    for object in list_of_objects:
        if get_id(object) == id_object:
            return object
    return None


def add_object(list_of_objects, id_object, name, description, price, location):
    """
    Adds a new object.
    :param list_of_objects: the current list of list_of_objects.
    :param id_object: the id.
    :param name: the name.
    :param description: the description.
    :param price: the price.
    :param location: the location.
    :return: a new list of list_of_objects, with the new object added to its end.
    """

    if get_object_by_id(list_of_objects, id_object) is not None:
        raise ValueError('There is already an object with the id {}'.format(
            id_object))

    new_object = create_object(id_object, name, description, price, location)
    result = list_of_objects + [new_object]
    save_to_file(result)
    return result


def remove_object(list_of_objects, id_object):
    """
    Removes an object based on id.
    :param list_of_objects: the list of objects
    :param id_object: the id object
    :return: removed object
    """

    delete = [object for object in list_of_objects if get_id(object) != id_object]
    save_to_file(delete)
    return delete


def update_object(list_of_objects, id_object, name, description, price, location):
    """
        Updates an object by id.
        Empty string for a parameter means that it won't be changed.
        :param list_of_objects: the current list of objects
        :param id_object: the id of the object to update.
        :param name: the new name.
        :param description: the new description.
        :param price: str, the new price.
        :param location: str, the new location
        :return: a list of objects, with the given object updated.
    """
    read_from_file()
    new_objects = []
    for object in list_of_objects:
        if get_id(object) != id_object:
            new_objects.append(object)
        else:
            new_object = create_object(
                get_id(object),
                name if name != '' else get_name(object),
                description if description != '' else get_description(object),
                int(price) if price != '' else get_price(object),
                location if location != '' else get_location(object)
            )
            new_objects.append(new_object
                               )
    save_to_file(new_objects)
    return new_objects

def move_object(list_of_objects, old_location, new_location):
    """
    Moving all objects from one room to another
    :param list_of_objects: the list of objects
    :param old_location: the old location
    :param new_location: the new location
    :return: a new list of objects with the location moved
    """
    read_from_file()
    list_of_objects = deepcopy(list_of_objects)
    for object in list_of_objects:
        if get_location(object) == old_location:
            list_of_objects = update_object(list_of_objects, get_id(object), get_name(object), get_description(object), get_price(object), new_location)
    save_to_file(list_of_objects)
    return list_of_objects

def concatenation_string(list_of_objects, price_given, description_given):
    """
    Concatenating a read string to all object descriptions at a price higher than a read value
    :param list_of_objects: the list of objects
    :param price_given: the price given
    :param description_given: the description given
    :return: a new list of objects with the update descriptions
    """
    read_from_file()
    new_objects = deepcopy(list_of_objects)
    concatenation = []
    result_description = []
    for object in list_of_objects:
        if get_price(object) > price_given:
            new_description = get_description(object) + description_given
            result_description = create_object(get_id(object), get_name(object), new_description, get_price(object), get_location(object))
            concatenation.append(result_description)
        else:
            concatenation.append(result_description)
    save_to_file(concatenation)
    return concatenation

def max_price_location(list_of_objects):
    """
    Maximum price of objects per location
    :param list_of_objects: the list of objects
    :return: a dictionary with the maximum prices
    """

    location_price = {}
    for object in list_of_objects:
        price = get_price(object)
        location = get_location(object)
        if location in location_price:
            if get_price(location_price[location]) < price:
                location_price[location] = object
        else:
            location_price[location] = object
    save_to_file(location_price)
    return location_price


def sorted_by__price(list_of_objects):
    """
    Sorting objects in ascending order by purchase price
    :param list_of_objects: the list of objects
    :return: a new list with the sorted objects
    """
    def sort_key(list_of_objects):
        return get_price(list_of_objects)

    sorting = sorted(list_of_objects, key=sort_key)
    save_to_file(sorting)
    return sorting


def sum_price_location(list_of_objects):
    """
    Display of all amounts in each location
    :param list_of_objects: the list of objects
    :return: a dictionary with the amounts per location
    """
    location_sum = {}
    for object in list_of_objects:
        price = get_price(object)
        location = get_location(object)
        if location in location_sum:
            location_sum[location] += price
    else:
        location_sum[location] = price
    save_to_file(location_sum)
    return location_sum

def undo(list):
    list.pop()
    save_to_file(list[-1])
    return list[-1]










