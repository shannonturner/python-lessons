
def dropdown_states():
    
    """ What's a string doing all by itself, you ask? 
        Shouldn't I be attached to a variable?

        Well I'm a special string that Python looks for at the very beginning of a function.
        I'm used to describe the function.

        This function will return a string with an HTML drop-down menu of US states.
    """

    states = ['Alabama','Alaska','Arizona','Arkansas','California','Colorado','Connecticut','Delaware','Florida','Georgia','Hawaii','Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky','Louisiana','Maine','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri','Montana','Nebraska','Nevada','New Hampshire','New Jersey','New Mexico','New York','North Carolina','North Dakota','Ohio','Oklahoma','Oregon','Pennsylvania','Rhode Island','South Carolina','South Dakota','Tennessee','Texas','Utah','Vermont','Virginia','Washington','West Virginia','Wisconsin','Wyoming']
    abbreviations = ['AL','AK','AZ','AR','CA','CO','CT','DE','FL','GA','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

    output = ['<select>']

    for state, abbreviation in zip(states, abbreviations):
        output.append('\t<option value="{0}">{1}</option>'.format(abbreviation, state))

    output.append('</select>')

    output = '\n'.join(output) # Glue together the list with a newline between each list item.

    return output