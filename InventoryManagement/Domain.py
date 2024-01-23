def create_object(id_object, name, description, price, location):
    """
    Creates a new object.
    :param id_object: the id, must be unique.
    :param name: the name of the cake.
    :param description: the description of the cake.
    :param price: the price.
    :param location: the location.
    :return: an object.
    """
    object = str(id_object) + '=' + str(name) + '=' + str(description) + '=' + str(price) + '=' + str(location)
    return object


def get_id(object):
    """
    Gets the id of an object
    :param object: the object.
    :return: the object id.
    """
    return int(object.split('=')[0])


def get_name(object):
    """
    Gets the name of an object
    :param object: the object.
    :return: the object name.
    """
    return object.split('=')[1]


def get_description(object):
    """
    Gets the description of an object
    :param object: the object.
    :return: the object description.
    """
    return object.split('=')[2]


def get_price(object):
    """
    Gets the price of an object
    :param object: the object.
    :return: the object price.
    """
    return float(object.split('=')[3])


def get_location(object):
    """
    Gets the location of an object
    :param object: the object.
    :return: the object location.
    """
    return object.split('=')[4]


def to_string(object):
    return '{}. - name: {}, - description: {}, - price: {}, - location: {}'.format(
        get_id(object),
        get_name(object),
        get_description(object),
        get_price(object),
        get_location(object)
        )
