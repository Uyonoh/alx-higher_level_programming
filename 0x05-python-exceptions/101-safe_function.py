#!/bin/usr/python3

def safe_function(fct, *args):
	result = None
	try:
		result = fct(*args)
	except Exception as e:
		print("Exception: {}".format(e))
	return result