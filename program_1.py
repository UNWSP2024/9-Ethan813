# Program #1: Item Counter
# Assume a file containing a series of names (as strings) is named names.txt 
# (Use the included example file names.txt) and exists on the computer's disk.
# Write a program that displays the number of names that are stored in the file.
file = open("names.txt", "r")
def count_file_lines():
    ######################
    # Add your code here #
    ######################
    number_of_names = 0
    for lines in file:
        number_of_names += 1
    print('In the count_file_lines function')
    print(number_of_names)
#ethan collins 3/25/2025
# You don't need to change anything below this line:
if __name__ == '__main__':
    count_file_lines()