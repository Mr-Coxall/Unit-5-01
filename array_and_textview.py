# Created by: Mr. Coxall
# Created on: Sep 2016
# Created for: ICS3U
# This program, creates an array and saves it into a listbox

import ui
from numpy import random

# create the array
my_numbers = []

def create_array_touch_up_inside(sender):
	# this function loads numbers into the array
	
	# zero out array and textview
	global my_numbers
	my_numbers = []
	view['numbers_textview'].text = ' '
	
	for a_number in range(0,9):
	    a_number = random.randint(0, 100)
	    my_numbers.append(a_number)
	    view['numbers_textview'].text = view['numbers_textview'].text +'\r' + str(a_number)

def get_average_touch_up_inside(sender):
    # calculate the average
    
    total = 0
    for a_number in my_numbers:
        total = total + a_number
    average = total / len(my_numbers)
    view['average_label'].text = 'The average is: ' + str(average)

view = ui.load_view()
view.present('sheet')

