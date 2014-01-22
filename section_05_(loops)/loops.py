
def loop_example(list_to_loop_through):

    """ Assuming each item in list_to_loop_through is a number, return a list of each item in that list squared. """

    print "I'm going to begin to loop through this list: ", list_to_loop_through, "\n"

    list_items_squared = []

    for each_item in list_to_loop_through:

        print "Now I'm on: ", each_item
        print "{0} squared is {1}\n".format(each_item, each_item**2)
        
        list_items_squared.append(each_item**2)

    print "Now I'm done looping through the list, and I'm going to return the new list, where each list item has been squared."

    return list_items_squared


##Sample Output
##
##>>> my_list = [1, 3, 4, 5, 6, 78, 2334]
##>>> loop_example(my_list)
##I'm going to begin to loop through this list:  [1, 3, 4, 5, 6, 78, 2334]
##Now I'm on:  1
##1 squared is 1
##
##Now I'm on:  3
##3 squared is 9
##
##Now I'm on:  4
##4 squared is 16
##
##Now I'm on:  5
##5 squared is 25
##
##Now I'm on:  6
##6 squared is 36
##
##Now I'm on:  78
##78 squared is 6084
##
##Now I'm on:  2334
##2334 squared is 5447556
##
##[1, 9, 16, 25, 36, 6084, 5447556]
