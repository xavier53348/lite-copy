#!/usr/bin/python3
from main import SuperCopy
from tkinter import ttk,messagebox,PhotoImage, filedialog
from threading import Thread
from subprocess import call
from subprocess import PIPE,Popen,STDOUT
import psutil
import os ,shutil,time ,random

from pydub import AudioSegment
from pydub.playback import play
# 
class copying(SuperCopy):
	global my_dict , list_copy,PID,STOP

	PID=[]
	list_copy = list()

	def __init__(self):

		super().__init__(self)

	def read_and_insert(self):
		'''
			This function start to load all propietes in the supercopy
		'''
		global total_sum , list_doc, space_used
		global total_space , path_to , USER ,result_capacity

		USER , path_to, result_capacity = '','',''
		total_space , themes_used = [] , []
		# call_system=os.system('whoami')

		# if call_system != 0:
		# 	USER = call_system
		USER=psutil.users()[0][0]
		try:
			os.stat('/tmp/litecopy.txt')
			self.read_change = Thread(target=self.update_list)
			self.read_change.start()

		except FileNotFoundError as e:
			alert = messagebox.askokcancel('Linux Desktop Copy','No existen ficheros a copiar 	\nDesea agregar uno\n')
			if not alert:
				quit()

		else:
			list_copy.clear()

			with open('/tmp/litecopy.txt','r') as f:
				
				list_doc = f.readlines()
				list_doc = set(list_doc)
				list_doc = list(list_doc)
				full_total=len(list_doc)
				total_sum=0
				size_=0
				self.len_words=45
				try:

					with open('/tmp/path.txt'.format(USER)) as f:
						path_to = f.read().strip('\n')
						self.to_.config(text='to: {}'.format(path_to[-45:]))	# to destination
				except FileNotFoundError:
					self.dir_selected = filedialog.askdirectory(title='Dir to paste all data ')
					with open('/tmp/path.txt','w') as wfile: 
						wfile.write(self.dir_selected)
				finally:
					with open('/tmp/path.txt'.format(USER)) as f:
						path_to = f.read().strip('\n')
						self.to_.config(text='to: {}'.format(path_to[-45:]))	# to destination

				for index ,target in enumerate(list_doc):
					# split_text  = target.split('%/%')
					# dir_or_file = split_text[0]
					# dire_name   = split_text[1]
					# full_path   = split_text[2]
					# file_name   = split_text[3]
					# size_bits   = split_text[4] 
					# size_mbs    = split_text[5]
					# size_gbs    = split_text[6] 
					# time_cfile  = split_text[7]

					# THIS METOD RETURN ALL DATA UP
					try:
						self.text_formated_1=initialize_text_split.extrac_part_of_text(self,target)
					except IndexError:
						self.text_formated_1=initialize_text_split.extrac_part_of_text(self,target)
						self.answer=messagebox.showinfo('Info','Incorrect file selected Please load correct "save.txt" or your saves 	' )
						os.remove('/tmp/litecopy.txt')

					# size_kbs=split_text[]
					self.list_copies.tag_configure('add_white',background='white')
					self.list_copies.tag_configure('add_light_blue',background='lightblue')

					self.Mb_Gb=int(self.text_formated_1[5])

					if self.Mb_Gb <= 1:
						self.Mb_Gb = int(self.text_formated_1[4])/10**3
						self.Mb_Gb = '{:.0f} kb'.format(self.Mb_Gb).rjust(6,'0') # averiguar

					elif self.Mb_Gb < 999:
						self.Mb_Gb = '{} MB'.format(self.text_formated_1[5])

					elif self.Mb_Gb > 1000:
						self.Mb_Gb = '{} GB'.format(self.text_formated_1[6])

					if index % 2:
						self.list_copies.insert('',full_total,text=index,value=[self.text_formated_1[3],self.Mb_Gb],tags=('add_light_blue',))	# insert in treview 
					else:
						self.list_copies.insert('',full_total,text=index,value=[self.text_formated_1[3],self.Mb_Gb],tags=('add_white',))	# insert in treview 

					list_copy.append(target)
					total_sum += int(self.text_formated_1[4])

				self.from_.config(text='From .../{}'.format(list_copy[0].split('%/%')[2][-self.len_words:])) # of fullpath get the last 60 caracters

				################################ capacity##################
				# print(total_sum)
				used_capacity=shutil.disk_usage(path_to).used # filling
				free_capacity=shutil.disk_usage(path_to).free # memory

				used_capacity_disk=round(shutil.disk_usage(path_to).used/10**6)
				free_capacity_disk=round(shutil.disk_usage(path_to).free/10**6)

				if used_capacity_disk > 999:
					result_ocupasy = ' Used:  {:.1f} GB '.format(used_capacity/10**9)
				elif used_capacity_disk < 999:
					result_ocupasy = ' Used:  {:.0f} MB '.format(used_capacity/10**6)
				elif used_capacity_disk < 1:
					result_ocupasy = ' Used:  {:.0f} KB '.format(used_capacity/10**3)

				if free_capacity_disk > 999: 
					result_free = ' Free:    {:.1f} GB '.format(free_capacity/10**9)
				elif free_capacity_disk < 999: 
					result_free = ' Free:    {:.0f} MB '.format(free_capacity/10**6)
				elif free_capacity_disk < 1: 
					result_free = ' Free:    {:.0f} KB '.format(free_capacity/10**3)

				self.used_capacity.config(text=result_ocupasy)
				self.label_space.config(text=result_free)
				check_size = (total_sum-free_capacity)/10**6

				# # ###########################################################
			
				if total_sum/10**6 <= 1:
					total_sum_by_size = '{:.0f} KB'.format(total_sum/10**3)
					self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(0,full_total,total_sum_by_size))
					total_space.append(total_sum)

				elif total_sum/10**6 < 999:
					total_sum_by_size = '{:.0f} MB'.format(total_sum/10**6)
					self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(0,full_total,total_sum_by_size))
					total_space.append(total_sum)

				elif (total_sum/10**6 > 1000 and total_sum/10**6 < 9999):
					total_sum_by_size ='{:.2f} GB'.format( total_sum/10**9)
					self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(0,full_total,total_sum_by_size))
					total_space.append(total_sum)
				
				elif total_sum/10**6 > 9999:
					total_sum_by_size ='{:.1f} TB'.format( total_sum/10**12)
					self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(0,full_total,total_sum_by_size))
					total_space.append(total_sum)


				if check_size < 999:
					check_size = '{:.0f} MB'.format((total_sum-free_capacity)/10**6)

				elif check_size > 1000 and check_size < 9999:
					check_size = '{:.2f} GB'.format((total_sum-free_capacity)/10**9)

				elif check_size > 9999:
					check_size = '{:.1f} TB'.format((total_sum-free_capacity)/10**12)

				###############################weqweqeqw
				if total_sum > free_capacity:
					# sound = AudioSegment.from_wav('mplayer /usr/share/sounds/litecopy/error.wav')
					# play(sound)
					# os.system('mpv /usr/share/sounds/litecopy/error.wav')
					# play(sound)
					_= messagebox.askyesno('Espacio Insuficiente','No tienes suficiente espacio para copiar los ficheros selecionados\n\
Si Desea continuar borre algunos ficheros para que se pueda realizar la copia con exito\n\nEspacio libre:\t{} \n\
a copiar:\t\t{} \nFaltan:\t\t{} \n\nDe continuar su informacion no estara completa y la perdera'.format(result_free,total_sum_by_size,check_size))

					if not _:
						os.remove('/tmp/litecopy.txt')
						quit()
				else:
					pass

				self.label_file_destination.config(text='Copy: ./{}'.format(os.path.basename(list_copy[0].split('%/%')[2])[-self.len_words:]))

	def start_copy(self):
		'''
		this function start after initialize the function by defauld read_and_insert() and start all parameter inside the copier

		'''
		global PID,STOP,STOP_IMAGE,PASSING_FILE


		full_total=len(list_copy)
		erase_conten_treview_one_by_one = self.list_copies.get_children()
		sum_size=0
		icrease_progress = 0
		total_sum_bar= 0
		counter_image=1
		sum_size_bits = 0
		increase_total=0
		suma=0
		STOP=''
		STOP_IMAGE, PASSING_FILE = 0, 0
		increase=0
		self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/{}.png".format(counter_image))

		with open('/tmp/path.txt'.format(USER)) as f:
			path_to = f.read().strip('\n')
			if not os.path.exists(path_to):
				self.answer=messagebox.showinfo('Info',"Destination It Doesn't exist\n\n{}	\n\nPlease Paste in other 'Dir'".format(path_to) )
				quit()

			# dir_or_file = split_text[0]
			# dire_name   = split_text[1]
			# full_path   = split_text[2]
			# file_name   = split_text[3]
			# size_kbs    = split_text[4] # aberiguar en una funcion
			# size_mbs    = split_text[5] # aberiguar en una funcion
			# size_gbs    = split_text[6] # aberiguar en una funcion
			# time_cfile  = split_text[7]
			
			# shutil.disk_usage()
			# shutil.copytree()
			# shutil.fnmatch
			# shutil.move()
			# shutil.stat()
			# round(int(shutil.disk_usage(x[2]).used)/1024**3,2)
		for index, target in enumerate(list_copy,1):

			self.text_formated=initialize_text_split.extrac_part_of_text(self,target) 	# return all text
			self.capture_type_kb_mb_gb = Correct_file_kb_mb_gb.filter_string(self,self.text_formated[5])

			self.Mb_Gb=int(self.text_formated[5])
			self.bits = int(self.text_formated[4])

			###################### FILTER THE SIZE IN KB MB GB
			if self.Mb_Gb <= 1:
				self.Mb_Gb = int(self.text_formated_1[4])/10**3
				self.label_velocity.config(text='Copy: {:.0f} KB'.format(self.Mb_Gb))

			elif self.Mb_Gb < 999:
				self.label_velocity.config(text='Copy: {} MB'.format(self.text_formated[5]))

			elif self.Mb_Gb > 1000:
				self.label_velocity.config(text='Copy: {} GB'.format(self.text_formated[6]))
 
			sum_size+=self.Mb_Gb
			sum_size_bits += self.bits
			# self.label_velocity2.config(text='Passed: {:.0f} KB'.format(sum_size))
			increase+=int(self.text_formated[5])
			# print(increase,'=>',sum_size)

			if increase <= 1:
				# print(increase,'klo')
				self.label_velocity2.config(text='Passed: {:.0f} KB'.format(increase/10**3))
			elif increase > 1 and increase < 999:
				# print(increase,'mega')
				self.label_velocity2.config(text='Passed: {:.0f} MB'.format(increase))
			elif increase > 1000:
				# print(increase,'gia')
				self.label_velocity2.config(text='Passed: {:.2f} GB'.format(increase/10**3))

			if len(self.text_formated[3]) > 50:
				self.label_file_destination.config(text='Copy: ./{}'.format(self.text_formated[3][-self.len_words:]))
			else:
				self.label_file_destination.config(text='Copy: ./{}'.format(self.text_formated[3]))
			# self.nota.list_copies.delete(erase_conten_treview_one_by_one[index-1])
			self.list_copies.delete(erase_conten_treview_one_by_one[index-1])
			################################ CAPACITY ##################

			used_capacity=shutil.disk_usage(path_to).used # filling
			free_capacity=shutil.disk_usage(path_to).free # memory

			used_capacity_disk=round(shutil.disk_usage(path_to).used/10**6)
			free_capacity_disk=round(shutil.disk_usage(path_to).free/10**6)

			if used_capacity_disk > 999:
				result_ocupasy = ' Used:  {:.1f} GB '.format(used_capacity/10**9)
			elif used_capacity_disk < 999:
				result_ocupasy = ' Used:  {:.0f} MB '.format(used_capacity/10**6)
			elif used_capacity_disk < 1:
				result_ocupasy = ' Used:  {:.0f} KB '.format(used_capacity/10**3)

			if free_capacity_disk > 999: 
				result_free = ' Free:    {:.1f} GB '.format(free_capacity/10**9)
			elif free_capacity_disk < 999: 
				result_free = ' Free:    {:.0f} MB '.format(free_capacity/10**6)
			elif free_capacity_disk < 1: 
				result_free = ' Free:    {:.0f} KB '.format(free_capacity/10**3)

			self.used_capacity.config(text=result_ocupasy)
			self.label_space.config(text=result_free)
			check_size = (total_sum-free_capacity)/10**6

			# # ###########################################################
		
			if total_sum/10**6 <= 1:
				total_sum_by_size = '{:.0f} KB'.format(total_sum/10**3)
				self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(index,full_total,total_sum_by_size))
				total_space.append(total_sum)

			elif total_sum/10**6 < 999:
				total_sum_by_size = '{:.0f} MB'.format(total_sum/10**6)
				self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(index,full_total,total_sum_by_size))
				total_space.append(total_sum)

			elif (total_sum/10**6 > 1000 and total_sum/10**6 < 9999):
				total_sum_by_size ='{:.2f} GB'.format( total_sum/10**9)
				self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(index,full_total,total_sum_by_size))
				total_space.append(total_sum)
			
			elif total_sum/10**6 > 9999:
				total_sum_by_size ='{:.1f} TB'.format( total_sum/10**12)
				self.label_file_capacity.config(text='Files:{}/{}   Total: {} '.format(index,full_total,total_sum_by_size))
				total_space.append(total_sum)

				check_size = '{:.0f} MB'.format((total_sum-free_capacity)/10**6)
			elif check_size > 1000 and check_size < 9999:
				check_size = '{:.2f} GB'.format((total_sum-free_capacity)/10**9)
			elif check_size > 9999:
				check_size = '{:.1f} TB'.format((total_sum-free_capacity)/10**12)

			###############################sdsdas
			if free_capacity_disk < 10:
				# sound = AudioSegment.from_wav('mplayer /usr/share/sounds/litecopy/error.wav')
				# play(sound)

				_= messagebox.askyesno('Espacio Insuficiente','No tienes suficiente espacio para copiar los ficheros selecionados\n\
Si Desea continuar borre algunos ficheros para que se pueda realizar la copia con exito\n\nEspacio libre:\t{} \n\
a copiar:\t\t{} \nFaltan:\t\t{} \n\nDe continuar su informacion no estara completa y la perdera'.format(result_free,total_sum_by_size,check_size))

				if not _:
					os.remove('/tmp/litecopy.txt')
					quit()
			else:
				pass
			
			self.label_file_destination.config(text='Copy: ./{}'.format(os.path.basename(list_copy[0].split('%/%')[2])[-self.len_words:]))

			#############################################
			time_start=time.perf_counter()
			
			src_bits=int(self.text_formated[4])

			#***********************************************
			# Thread(target=read_copy.Reading_file.now(self)).start
			############################### ARREGLAR #############################################
			porcentage_files = index/full_total*100

			#****************************************
			full_paths=self.text_formated[2]							# /home/mjay/Documentos/4.mp4 					<== full path
			dir_star_copy=self.text_formated[1].split('/')[-1] 			# Documentos									<== curdir
			path_end=full_paths.split(dir_star_copy)[1].strip('/') 		# 4.mp4											<== dirs
			all_dirs=os.path.dirname(path_end)							
			# make dirs an paste new file
			all_make_dirs= os.path.join(path_to,all_dirs)				# /home/mjay/Música/litecopy/   					<== destination dir
			join_path=os.path.join(path_to,dir_star_copy,path_end)		# /home/mjay/Música/litecopy/Documentos/4.mp4		<== destination full
			join_path2=os.path.dirname(join_path)						# /home/mjay/Música/litecopy/Documentos/			<== destination full

			#********************************
			PID=[]

			if self.text_formated[0]  == 'Directory':
				# print('Directory')
				full_paths=self.text_formated[2]							# /home/mjay/Documentos/4.mp4 					<== full path
				dir_star_copy=self.text_formated[1].split('/')[-1] 			# Documentos									<== curdir
				path_end=full_paths.split(dir_star_copy)[1].strip('/') 		# 4.mp4											<== dirs
				all_dirs=os.path.dirname(path_end)							
				# make dirs an paste new file
				all_make_dirs= os.path.join(path_to,all_dirs)				# /home/mjay/Música/litecopy/   					<== destination dir
				join_path=os.path.join(path_to,dir_star_copy,path_end)		# /home/mjay/Música/litecopy/Documentos/4.mp4		<== destination full
				join_path2=os.path.dirname(join_path)						# /home/mjay/Música/litecopy/Documentos/			<== destination full

				while not os.path.lexists(join_path2):
					os.makedirs(join_path2)

				else:
					################### if th files are the same
					exit = os.path.exists(os.path.join(join_path2,self.text_formated[3]))

					if exit:
						compare_1 = os.stat(self.text_formated[2]).st_size
						compare_2 = os.stat(os.path.join(join_path2,self.text_formated[3])).st_size
						if compare_1 == compare_2: # compare if are the same size file
							p=''
							pass
						else:	# diferents
							p=psutil.Popen(["python3",'/usr/bin/modules/start_file.py',self.text_formated[2],join_path2])
							PID=p
					else: #if doesn't exit create one
						p=psutil.Popen(["python3",'/usr/bin/modules/start_file.py',self.text_formated[2],join_path2])
						PID=p


					##################################################

					time.sleep(0.1)
					copy_one=os.path.join(join_path2,self.text_formated[3])
					self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/1.png")
					after_read=0
					calc_seg=0

					Stop_Copy=True
					###################################################################
					while Stop_Copy:
						if PASSING_FILE: #IF PRESS STOP THE COPY
							print('passing file')
							try:
								p.kill()
							except AttributeError:
								pass
							time.sleep(0.1)
							Stop_Copy=False

							PASSING_FILE=0
						###################################################################
						time.sleep(0.1)
						try:
							dst_bits=os.stat(copy_one).st_size
						except FileNotFoundError:
							time.sleep(0.2)
							dst_bits=os.stat(copy_one).st_size
						

						self.progressbar_pass_one.config(maximum=src_bits,value=dst_bits)
						self.from_.config(text='From .../{}'.format(self.text_formated[2][-self.len_words:]))
						self.to_.config(text='to: /sdcard/memoria')

						time_end=time.perf_counter()
						time_total=time_end - time_start
						capture=src_bits
						############################## img
						self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/{}.png".format(counter_image))
						if STOP_IMAGE:
							self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/{}.png".format(counter_image))
						else:
							counter_image+=1
							if counter_image >23:
								counter_image=2
						###############################################
						self.photo_image_pass.config(image=self.photo_logo)
						actually_read=dst_bits
						bits_secons = actually_read - after_read

						################ velocity by secons
						if calc_seg < 8:
							# print(calc_seg)
							calc_seg+=1
						else:
							porcentage_total=suma/total_sum*100
							mbs_secons = bits_secons/10**6
							self.label_scale_velocity.config(text='{:.0f} /MBs'.format(mbs_secons))
							self.scale_velocity.config(value=mbs_secons)
							self.label_total_progress.config(text='{:.0f} %'.format(porcentage_total,background='#1d1d1d'))
							self.progreso('total {:.0f} % files:{:.0f} %'.format(porcentage_total,porcentage_files))

							calc_seg=0

						after_read=dst_bits
						suma+=bits_secons
						# print(suma) # bits
						mb_by_seg=0
						########################################################
						# icrease_progress += capture_total

						if src_bits == dst_bits:
							break
					# resutl= total_sum - resutl
					increase_total+=dst_bits

			############################### ARREGLAR #############################################


			else: # if this elemnts are files
				# print('file')
				# if PASSING_FILE:
				# 	print('passing file')
				################### if th files are the same

				exit = os.path.exists(os.path.join(path_to,self.text_formated[3]))
				if exit:
					compare_1 = os.stat(self.text_formated[2]).st_size
					compare_2 = os.stat(os.path.join(path_to,self.text_formated[3])).st_size

					if compare_1 == compare_2: # compare if are the same size file
						pass
					else:	# diferents
						p=psutil.Popen(["python3",'/usr/bin/modules/start_file.py',self.text_formated[2],path_to])
						PID=p
				else: #if doesn't exit create one
					p=psutil.Popen(["python3",'/usr/bin/modules/start_file.py',self.text_formated[2],path_to])
					PID=p

				##################################################
				time.sleep(0.1)
				copy_one=os.path.join(path_to,self.text_formated[3])
				self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/1.png")
				after_read=0
				calc_seg=0

				Stop_Copy=True

				##################################################
				while Stop_Copy:
					if PASSING_FILE:	#if Stop_copy is press pause the copy
						print('passing file')
						try:
							p.kill()
						except AttributeError:
							pass
						time.sleep(0.1)
						Stop_Copy=False
						PASSING_FILE=0
					###################################################################
					time.sleep(0.1)
					try:
						dst_bits=os.stat(copy_one).st_size
					except FileNotFoundError:
						time.sleep(0.2)
						dst_bits=os.stat(copy_one).st_size

					# dst_bits=os.stat(copy_one).st_size

					self.progressbar_pass_one.config(maximum=src_bits,value=dst_bits)
					self.from_.config(text='From .../{}'.format(self.text_formated[2][-self.len_words:]))
					self.to_.config(text='to: /sdcard/memoria')

					time_end=time.perf_counter()
					time_total=time_end - time_start
					capture=src_bits

					self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/{}.png".format(counter_image))
					############################## img
					if STOP_IMAGE:
						self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/{}.png".format(counter_image))
					else:
						counter_image+=1
						if counter_image >23:
							counter_image=2
					###############################################
					self.photo_image_pass.config(image=self.photo_logo)
					actually_read=dst_bits
					bits_secons = actually_read - after_read

					################ velocity by secons
					if calc_seg < 8:
						# print(calc_seg)
						calc_seg+=1
					else:
						porcentage_total=suma/total_sum*100
						mbs_secons = bits_secons/10**6
						self.label_scale_velocity.config(text='{:.0f} /MBs'.format(mbs_secons))
						self.scale_velocity.config(value=mbs_secons)
						self.label_total_progress.config(text='{:.0f} %'.format(porcentage_total,background='#1d1d1d'))
						self.progreso('total {:.0f} % files:{:.0f} %'.format(porcentage_total,porcentage_files))

						calc_seg=0
											## imagen in move
					after_read=dst_bits
					suma+=bits_secons
					mb_by_seg=0
					########################################################
					if src_bits == dst_bits:
						break

				# resutl= total_sum - resutl
				increase_total+=dst_bits
		#***********************************************

		sound = AudioSegment.from_wav('/usr/share/sounds/litecopy/complete.wav')
		play(sound)
		# self.progressbar_pass_one.config(maximum=100,value=100)

		self.photo_logo = PhotoImage(file="/usr/share/icons/litecopy/mov/0.png")
		self.photo_image_pass.config(image=self.photo_logo)
		self.label_total_progress.config(text='100 %',background='#1d1d1d')
		self.progreso('total 100 % files:100 %')
		# after finish remove al files 
		os.remove('/tmp/litecopy.txt')

	#################################### position ##################################
	def delete_select_position(self):

		try:
			tuple_selects = self.list_copies.selection()
			if tuple_selects:

				for select_one in tuple_selects:
					self.index_select = self.list_copies.index(select_one)
					self.list_copies.delete(select_one)
					removed = list_doc.pop(int(self.index_select))

				if list_doc:
					with open('/tmp/litecopy.txt','w') as f:
						for i in list_doc:
							f.write(i)
				else:
					try:
						os.remove('/tmp/litecopy.txt')
					except FileNotFoundError:
						self.answer=messagebox.showinfo('Info','No more files to delete 	' )
			else:
				self.answer=messagebox.showinfo('Info','Please select the file to delete 	' )
					
		except IndexError:
			pass

	def removing(self):
		os.remove('/tmp/litecopy.txt')
		for i in self.list_copies.get_children():
			self.list_copies.delete(i)

	def save_data_store(self):
		try:
			with open('/tmp/litecopy.txt','r') as rfile:
				self.data_read = rfile.readlines()
				# print(self.list_copies.get_children())
				if self.list_copies.get_children():
					self.file_save = filedialog.asksaveasfile(initialfile='litecopy_save.txt',title='Safe all data in a file "*.txt"',defaultextension='txt',mode='w')
					if self.file_save:
						with open(self.file_save.name,'w') as wfile:
							for i in self.data_read:
								wfile.write(i)
		except FileNotFoundError:
			self.answer=messagebox.showinfo('Info','No files to save 	' )
	#******************************************************************
	def stop_copy(self):
		global STOP_IMAGE
		
		if PID != []:
			PID.suspend()
			STOP_IMAGE=1

	def continue_copy(self):
		global STOP_IMAGE

		if PID != []:
			PID.resume()
			STOP_IMAGE=0

	def pass_copy(self):
		global PASSING_FILE
		PASSING_FILE=1

		
	def load_data_store(self):
		self.file_selected = filedialog.askopenfile(initialfile='litecopy_save.txt',title='load all data in a file "*.txt"',defaultextension='txt')

		if self.file_selected:
			try:
				with open(self.file_selected.name,'r') as rfile:
					self.data = rfile.readlines()
					if os.path.exists('/tmp/litecopy.txt'):
						with open('/tmp/litecopy.txt','a') as wfile:
							for i in self.data:
								wfile.write(i)
					else:
						with open('/tmp/litecopy.txt','a') as f:
							for i in self.data:
								f.write(i)
				
			except IndexError:
				self.answer=messagebox.showinfo('Info','Incorrect file selected Please load correct "save.txt" or your saves 	' )
			
	#################################################################################
	def start_widget(self):
		self.paint_frame.grid(	row=0, column=0, columnspan=8, sticky="NSWE",	rowspan=17)
		self.from_.grid(		row=0, column=1, columnspan=3, sticky="W") 										# from
		self.to_.grid(			row=1, column=1, columnspan=3, sticky="NW",		rowspan=2)						# to
		
		self.label_file_destination.grid(row=3, column=1, columnspan=3,	sticky="W")								# copy
		self.label_single_progress.grid( row=2, column=2, columnspan=1,	sticky='W')								# label inside progres bar
		self.progressbar_pass_one.grid(  row=2, column=1, columnspan=7,	sticky="WE", padx=(0,8))				# progrees bar
		self.label_total_progress.grid(  row=0, column=0, rowspan=2,	sticky='NE', padx=(0,8), pady=(4,0))	# label inside the photo

		# self.progressbar_pass_total.grid(row=5,column=1,columnspan=4,sticky="WE")

		self.scale_velocity.grid(		row=4, sticky="WE",	column=1,columnspan=1)								#scale
		self.label_scale_velocity.grid(	row=4, sticky="W",	column=2)											#scale label
		self.label_file_capacity.grid(	row=5, sticky="W",	column=1)											#files and total

		# grid down
		self.used_capacity.grid(	row=0, column=4, columnspan=4,	sticky="E",	padx=(0,8)) 					#used
		self.label_space.grid(		row=1, column=4, columnspan=4,	sticky="E",	padx=(0,8))						#free
		self.label_velocity2.grid(	row=4, column=4, columnspan=4,	sticky="E",	padx=(0,8))						#pass
		self.label_velocity.grid(	row=5, column=0, columnspan=4,	sticky="WS",padx=(8,0))						#copy
		self.photo_image_pass.grid(	row=0, column=0, rowspan=7,		padx=(0,4))

		self.btn_1.grid(row=5, column=4, padx=0)
		self.btn_2.grid(row=5, column=5, padx=0)
		self.btn_3.grid(row=5, column=6, padx=0)
		self.btn_4.grid(row=5, column=7, padx=(0,8))
	
	def open_list(self,*arg):
		if arg[0]:
			self.notebook.grid(		row=7,  column=0, rowspan=8,	columnspan=8,sticky='WE')
			self.list_copies.grid(	row=10, column=0, columnspan=9,	rowspan=7,	padx=(10,10))
			self.btn_update.grid(	row=10, column=8, rowspan=5,	sticky="E",	pady=(0,0))
			self.btn_remove.grid(	row=11, column=8, rowspan=4,	sticky="E",	pady=(0,12))
			self.btn_clear.grid(	row=12, column=8, rowspan=3,	sticky="E",	pady=(0,24))
			self.btn_save.grid(		row=13, column=8, rowspan=2,	sticky="E",	pady=(0,36))
			self.btn_load.grid(		row=14, column=8, rowspan=1,	sticky="E",	pady=(0,48))
			self.themes.grid(		row=17, column=4, columnspan=4,	sticky="E",	padx=(0,18))

			self.label_bitcoin.grid(row=10,columnspan=7	,sticky="W",padx=(16,0),pady=(16,0))
			self.BTC.grid( row=11, column=1, pady=(10,0),padx=(10,0))
			self.BTCH.grid(row=11, column=2, pady=(10,0))
			self.DASH.grid(row=11, column=3, pady=(10,0))
			self.DOGE.grid(row=11, column=4, pady=(10,0))
			self.LTC.grid( row=11, column=5, pady=(10,0))

			self.LABEL_BTC.grid( row=12, column=1, pady=(10,0), sticky="N", padx=(10,0))
			self.LABEL_BTCH.grid(row=12, column=2, pady=(10,0), sticky="N")
			self.LABEL_DASH.grid(row=12, column=3, pady=(10,0), sticky="N")
			self.LABEL_DOGE.grid(row=12, column=4, pady=(10,0), sticky="N")
			self.LABEL_LTC.grid( row=12, column=5, pady=(10,0), sticky="N")
			
			self.PHOTO_COIN_WALLET.grid(row=11,rowspan=6,column=0	, padx=(10,0), pady=(10,0))
			
			self.LABEL_COIN_NOTE.grid(row=15,column=1 ,sticky='W',columnspan=6)
			self.LABEL_COIN_WALLET.grid(row=17,column=0 ,sticky='E')
			self.ENTRY_COIN_WALLET.grid(row=17,column=1	, padx=(10,0), columnspan=5,sticky="W")
			
		else:
			self.notebook.grid_forget()
			self.list_copies.grid_forget()
			self.btn_update.grid_forget()
			self.btn_remove.grid_forget()
			self.btn_clear.grid_forget()
			self.btn_save.grid_forget()
			self.btn_load.grid_forget()
			self.themes.grid_forget()

	def exit_supercopy(self):
		self.answer=messagebox.askyesno('Note','Would you like EXIT' )
		
		if self.answer:
			process = psutil.Process(os.getpid())
			if not PID == []:
				PID.kill()
			process.kill()
			

class initialize_text_split(copying):
	"""docstring for initialize_text_split"""
	def __init__(self, arg):
		super(initialize_text_split, self).__init__()
		self.arg = arg
	def extrac_part_of_text(self,arg):

		split_text  = arg.split('%/%')
		dir_or_file = split_text[0]
		dire_name   = split_text[1]
		full_path   = split_text[2]
		file_name   = split_text[3]
		size_kbs    = split_text[4] 
		size_mbs    = split_text[5] 
		size_gbs    = split_text[6] 
		time_cfile  = split_text[7]
		salida = dir_or_file ,dire_name, full_path, file_name, size_kbs, size_mbs, size_gbs, time_cfile
		return salida

class Correct_file_kb_mb_gb(copying):
	"""docstring for Correct_file_kb_mb_gb"""
	def __init__(self, arg):
		super(Correct_file_kb_mb_gb, self).__init__()
		self.arg = arg

	def filter_string(self,arg):
		size = int(arg)
		if size < 1024:	# kb
			result_mb='{:.2f}'.format(size)
			human_size = [result_mb,'{:.0f} MB'.format(size)]
			return human_size

		elif size > 1024  and size < 1048576: # 1024**2 == Mb
			result_gb='{:.2f}'.format(size)
			human_size = [result_gb, '{:.2f} GB'.format(size)]
			return human_size