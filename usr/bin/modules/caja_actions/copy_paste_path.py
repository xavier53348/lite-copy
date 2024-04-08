#!/usr/bin/python3
# if dont work  give permise chmod +x copy_path
from subprocess import call

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('filelist', help='list of absolute paths separated by /#/')
args = parser.parse_args()

command=['python3','/usr/bin/main.py']
paste_path='/tmp/path.txt'
remove_copy_path='/tmp/litecopy.txt'

if os.path.lexists(remove_copy_path):

	with open(paste_path,'w') as f:
		path_actually = args.filelist.split('/#/')
		f.write('{}\n'.format(os.path.realpath(path_actually[0])))
	call(command)
