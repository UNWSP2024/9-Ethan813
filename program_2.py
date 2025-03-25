# Program #2: Random Number File Writer
# Write a program that writes a series of random numbers (up to 1000) to a file.
# Each random number should be in the range of 1 through 500. 
# The application should let the user specify how many random numbers the file will hold 
# (up to 1000).
import random
numbers_file = open('numbers.txt', 'w')
number_of_times = int(input('how many random numbers do you want? (up to 1000) '))
if number_of_times <= 1000:
    for number in range(number_of_times):
        write_number = str(random.randrange(0,500))
        numbers_file.write(write_number)
        numbers_file.write('\n')
else:
    print('please restart the program and enter a number between 0 and 1000')
#ethan collins 3/25/2025