def remove_duplicates(from_list):

    """ 
        The function list() will convert an item to a list. 
        The function set() will convert an item to a set.

        A set is similar to a list, but all values must be unique.

        Converting a list to a set removes all duplicate values.
        We then convert it back to a list since we're most comfortable working with lists.

    """

    from_list = list(set(from_list))

    return from_list

    
