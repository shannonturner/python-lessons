def access(dictionary, nested_keys):

    """ Try to access nested keys within a dictionary.  Returns False instead of a KeyError on failure. 

        Written to avoid needing to do multiple try/except blocks when trying to access specific values in JSON.

        Previously:
            try:
                title = response['response']['docs'][0]['descriptiveNonRepeating']['title']['content']
            except KeyError:
                pass

            # ... and repeating this structure for each variable we'd like to save.  
            # We could wrap the *whole* thing in a try/except, but then it would trigger the except on the first failure.

        Now:
            title = access(response, ['response', 'docs', 0, 'descriptiveNonRepeating', 'title', 'content'])

            # ... and repeating this structure for each variable we'd like to save.

    """

    for index, key in enumerate(nested_keys):

        print index, key

        try:
            if dictionary.has_key(key):
                if nested_keys[index + 1:] != []:
                    return access(dictionary[key], nested_keys[index + 1:])
                else:
                    return dictionary[key]
            else:
                return False
        except AttributeError: # at this point, dictionary is a list, perhaps containing dictionaries
            if key < len(dictionary):
                if nested_keys[index + 1:] != []:
                    return access(dictionary[key], nested_keys[index + 1:])
                else:
                    return dictionary[key]
            else:
                return False