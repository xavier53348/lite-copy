#!/usr/bin/python3
import os


remove_copy_path='/tmp/litecopy.txt'

if os.path.lexists(remove_copy_path):
	os.remove(remove_copy_path)
