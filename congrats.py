#!/usr/bin/env python

WINTER_2017 = ['K. Student', 'J. Student', 'L. Student', 'M. Student']

def wish_congrats(class_list) :
	for students in class_list: 
		print 'Congrats %s!  You completed Programming for Data Analytics!' % students

wish_congrats(WINTER_2017)
