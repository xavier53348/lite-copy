#!/usr/bin/python3
# if dont work  give permise chmod +x copy_path
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('filelist', help='list of absolute paths separated by /#/')
args = parser.parse_args()
# fields of the file
# if state  	==  Directory or Files
# directory		==  Path of the directory
# join_path 	==  Path + Archives
# real_size_kbs	==  size in kbs
# real_size_mbs	==  Mb
# real_size_gbs ==	Gb
# create time	==  00.00.00.00.00.00
# dir!file %/% path_directory %/% path_and_file %/% name_file %/% size_kbs %/% size_mb %/% size_gb %/% created_time

with open('/tmp/litecopy.txt','a') as f:
	# f.write(os.getcwd())
	for arg in args.filelist.split('/#/'):
		print(args)
		if os.path.isdir(arg):

			#find al files in a directory
			for path , directory , file in os.walk(arg):

				for i in file:
					join_path = os.path.join(path,i)
					real_size_kbs = os.stat(join_path).st_size
					real_size_mbs = real_size_kbs/ 10**6
					real_size_mbs = '{:.0f}'.format(real_size_mbs)
					real_size_gbs = real_size_kbs/ 10**9
					real_size_gbs = '{:.2f}'.format(real_size_gbs)
					created_times = os.stat(join_path).st_ctime
					f.writelines('Directory%/%{path_directory}%/%{path_and_file}%/%{name_file}%/%{size_kbs}%/%{size_mb}%/%{size_gb}%/%{created_time}\n'.format(path_directory=arg,path_and_file=join_path,name_file=os.path.basename(join_path),size_kbs=real_size_kbs,size_mb=real_size_mbs,size_gb=real_size_gbs,created_time=created_times))
		else:
			real_size_kbs = os.stat(arg).st_size
			real_size_mbs = os.stat(arg).st_size/ 10**6
			real_size_mbs = '{:.0f}'.format(real_size_mbs)
			real_size_gbs = os.stat(arg).st_size/ 10**9
			real_size_gbs = '{:.2f}'.format(real_size_gbs)
			created_times = os.stat(arg).st_ctime
			f.writelines('Archives%/%{path_directory}%/%{path_and_file}%/%{name_file}%/%{size_kbs}%/%{size_mb}%/%{size_gb}%/%{created_time}\n'.format(path_directory=os.path.dirname(arg),path_and_file=arg,name_file=os.path.basename(arg),size_kbs=real_size_kbs,size_mb=real_size_mbs,size_gb=real_size_gbs,created_time=created_times))