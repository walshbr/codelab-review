# data types

# strings: sequence of characters
my_string = 'a list is here'

# integers: numbers
my_int = 4

# floats: numbers w/ decimals
my_float = 4.0

# data collections
# list: property 1 - it has an order; property 2 - it has many things in it; 3 - you can do list-like things to it
# my_list[2]

my_list = ['a', 'list', 'is', 'here']
my_list[2]

# dictionary: property 1 - associative; property 2 - no order
# my_dict = {key: value, key: value }
my_dict = {'virginia': 'va', 'texas': 'tx'}
my_dict['virginia']

my_authors = {'dickens': 'hard times', 'woolf': 'orlando'}

# ways of organizing data
# let's organize the praxis cohort

# a string - we could capitalize it or lowercase it
the_string_cohort = "The Praxis cohort consists of Susan, Joseph, Jennifer, Jacqui, Tarushi, Cherrie"

# a list
the_list_cohort = ['Susan', 'Joseph', 'Jennifer', 'Jacqui', 'Tarushi', 'Cherrie']
# this would give us a sense of ordering. We could shuffle them up, etc. But now we have more of a sense of each of these people as actual, separate units.


# a dictionary expects you to have an association, two pieces of data that are connected.
# first_name: last_name
# initials: full name
# cohort_num: list_of_students
# let's do name: year_in_program
the_dict_cohort = {'Susan': 3, 'Joseph': 5}
 
# let's organize the same data two different ways, using a sort-of humanist example
# book - author, death_date, title, list of words in the book
book_one_list = ['Dickens', '1894', 'Hard Times', ['It', 'was', 'the', 'hardest', 'time']]
book_one_dict = {'author': 'Dickens', 'title': 'Hard Times', 'the_words': ['It', 'was', 'the', 'hardest','time']}
