# read in a file and find the number of lines associated with Benedick

# create a variable 'filename' and give it the data corpus/ado.txt
# store the filepath for the text we want
filename = "corpus/ado.txt"

# read/open the file
with open(filename, 'r') as file_input:
    # benedick_lines -> the file object thing
    # do some stuff with the file

    text = file_input.readlines()

print(text)

# find the number of lines associated with Benedick