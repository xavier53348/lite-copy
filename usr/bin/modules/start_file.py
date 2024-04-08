#!/usr/bin/python3
from threading import Thread
import shutil,sys

text_formated_0=sys.argv[1]
text_formated_1=sys.argv[2]

copy_start = Thread(target=shutil.copy,args=(text_formated_0,text_formated_1))
copy_start.start()