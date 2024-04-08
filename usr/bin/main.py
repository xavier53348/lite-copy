#!/usr/bin/python3 

from modules import read_copy
import tkinter
from tkinter import * 
from tkinter import ttk , Spinbox ,messagebox,Toplevel
import textwrap

import os , psutil, time
from threading import Thread

chek, one_time='0',1
try:
	from ttkthemes import themed_style as tk
except:
	pass
	# print('no existe ttkthemes')

class SuperCopy(Thread):
	
	global background ,border ,width_button, background_btn_label ,relief_button ,over_relief_button ,font_size2,font_size ,font_size3 , skin_label ,skin_label2,label_light
	global USER ,background_copy,skin,porcentage_label
	global chek, one_time

	width_button=10
	label_light='grey'
	# label_light='#16a4d0'
	skin_label='#A9CED7'
	skin_label2='#34E2E2'
	skin='#424242'
	porcentage_label='yellow'
	# skin_label='#16a4d0'
	background="#1d1d1d"
	relief_button = 'flat'
	border=0
	over_relief_button='sunken'
	font_size='helvetica 9'
	font_size2='helvetica 8'
	font_size3='helvetica 11'
	USER=''
	background_copy='white'

	# background_copy='#1f1f1f'
	# call_system=os.system('whoami ')
	# if call_system != 0:
		# USER = call_system

	USER=psutil.users()[0][0]
	# ark,,ubuntu,radiace,yaru,clearlooks
	def __init__(self,root,Thread):
		s = ttk.Style()

		# s=tk.ThemedStyle()
		s.theme_use('clam') #########

		# s.con
		# print(s.theme_names())
		# print(s.get_themes())
		# s.theme_use('ubuntu')
		# s.configure('Treeview',background='red',foreground='yellow',rowheight=18,fieldbackground='pink')
		# s.map('Treeview',background=[('selected','blue')])
		# root = root
		root.protocol('WM_DELETE_WINDOW',self.ask_cancel)
		root.protocol('WM_MINIMIX_WINDOW',self.ask_cancel)

		root.title("Lite Copy")

		self.velocity = StringVar()
		root.config(bg=background_copy)

		self.photo_list  = PhotoImage(file="/usr/share/icons/litecopy/button_menu.png")
		self.photo_play = PhotoImage(file="/usr/share/icons/litecopy/button_play.png")
		self.photo_next  = PhotoImage(file="/usr/share/icons/litecopy/button_next.png")
		self.photo_pause = PhotoImage(file="/usr/share/icons/litecopy/button_pause.png")
		self.photo_stop = PhotoImage(file="/usr/share/icons/litecopy/button_stop.png")
		self.photo_cancel= PhotoImage(file="/usr/share/icons/litecopy/button_exit.png")
		self.photo_logo  = PhotoImage(file="/usr/share/icons/litecopy/mov/0.png")

		self.img_update = PhotoImage(file="/usr/share/icons/litecopy/btn_load.png"	)
		self.img_remove = PhotoImage(file="/usr/share/icons/litecopy/btn_delete.png")
		self.img_clear  = PhotoImage(file="/usr/share/icons/litecopy/btn_clear.png"	)
		self.img_save   = PhotoImage(file="/usr/share/icons/litecopy/btn_save.png"	)
		self.img_load   = PhotoImage(file="/usr/share/icons/litecopy/btn_add.png"	)

		self.IMG_BTC 	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin/bitcoincore.png"	)
		self.IMG_BTCH 	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin/bitcoincash.png")
		self.IMG_DASH  	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin/dash.png"	)
		self.IMG_DOGE   = PhotoImage(file="/usr/share/icons/litecopy/bitcoin/dogecoin.png"	)
		self.IMG_LTC   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin/litecoin.png"	)

		self.IMG_WALLET_BTCH   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin_wallet/bitcoincash.png"	)
		self.IMG_WALLET_BTC   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin_wallet/bitcoin.png"	)
		self.IMG_WALLET_DASH   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin_wallet/dashcoin.png"	)
		self.IMG_WALLET_DOGE   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin_wallet/dogecoin.png"	)
		self.IMG_WALLET_LITE   	= PhotoImage(file="/usr/share/icons/litecopy/bitcoin_wallet/litecoin.png"	)

		self.text_wallet=StringVar()
		# self.text_wallet.set('hola mundo')
		# s.theme_use('vistaTheme')

		# box destination
		self.main_frame = Frame(root,background=background_copy).grid(row=0,column=0,columnspan=5,rowspan=18,sticky="NSWE")
		self.paint_frame = Label(self.main_frame,background=skin)

		self.from_ 		= ttk.Label(self.main_frame	,font=font_size ,background=skin	,foreground=skin_label2	,width=45 ,text='From .../?')
		self.to_ 		= ttk.Label(self.main_frame	,font=font_size ,background=skin	,foreground=skin_label,text='To .../?') 
		self.ejemplo 	= StringVar()
		self.ejemplo.set('Dark')

		# grid copy
		# help(self.themes)
		self.photo_image_pass 		= Label(self.main_frame	,image=self.photo_logo			,background=background,border=0)
		self.used_capacity 			= ttk.Label(self.main_frame	,font=font_size2			,background='#1d1d1d'		,foreground=porcentage_label,border=0) 
		self.label_file_capacity 	= ttk.Label(self.main_frame	,font=font_size 			,background='#1d1d1d'		,foreground=porcentage_label,text='Files:00/00   Total: 00 KB ',border=0) 
		self.label_file_destination = ttk.Label(self.main_frame	,font=font_size 			,background=skin	,foreground=skin_label,width=45,text='Copy: ./?',border=0)

		self.progressbar_pass_one 	= ttk.Progressbar(self.main_frame, orient=HORIZONTAL, length=100, mode='determinate')
		self.progressbar_pass_one.tk_setPalette(background=skin)
		# self.progressbar_pass_total = ttk.Progressbar(self.main_frame, orient=HORIZONTAL, length=100, mode='determinate')
		# grid down
		self.label_velocity 		= ttk.Label(self.main_frame	,font=font_size2	,text='Copy: 00 MB'	,background='#1d1d1d' ,foreground=skin_label2)

		self.label_velocity2 		= ttk.Label(self.main_frame	,font=font_size2	,text='Passed: 00 GB'	,background=skin ,foreground=skin_label2) 
		self.label_single_progress 	= ttk.Label(self.main_frame	,font=font_size2	,text='00' 				,background='#bab5ab'								,border=0) 
		self.label_total_progress  	= ttk.Label(self.main_frame	,font=font_size3	,text='0 %' 			,background='#1d1d1d'		,foreground=porcentage_label 	,border=0) 
		self.label_space 			= ttk.Label(self.main_frame	,font=font_size2	,text='free: '			,background=skin	,foreground=skin_label ) 
		self.scale_velocity 		= ttk.Scale(self.main_frame	,from_= 0 ,to=100) 
		self.label_scale_velocity 	= ttk.Label(self.main_frame	,text='00 /MBs',background=skin,foreground=skin_label)


		self.btn_1 = Button(self.main_frame,text = 'menu' ,relief=relief_button,bd=border,overrelief=over_relief_button,height=30,image=self.photo_list,command=self.open_box_treview,bg=skin,fg=background,activebackground=skin)
		self.btn_2 = Button(self.main_frame,text = 'start',command=Thread(target=self.copy_pass).start 		,image=self.photo_play ,relief=relief_button,bd=border,overrelief=over_relief_button,height=30,bg=skin,fg=background,activebackground=skin)
		self.btn_3 = Button(self.main_frame,text = 'stop' ,command=self.pass_button,image=self.photo_next	,relief=relief_button  ,bd=border ,overrelief=over_relief_button ,height=30 ,bg=skin,fg=background,activebackground=skin)
		self.btn_4 = Button(self.main_frame,text = 'exit' ,command=self.ask_cancel							,relief=relief_button  ,bd=border ,overrelief=over_relief_button ,height=30 ,bg=skin,fg=background,activebackground=skin,image=self.photo_cancel,)

		self.btn_stop = Button(self.main_frame,text = 'start',command=self.stop_button		,image=self.photo_pause,relief=relief_button,bd=border,overrelief=over_relief_button,height=30,bg=skin,fg=background,activebackground=skin)
		self.btn_play = Button(self.main_frame,text = 'start',command=self.stop_button		,image=self.photo_play,relief=relief_button,bd=border,overrelief=over_relief_button,height=30,bg=skin,fg=background,activebackground=skin)

		# self.notebook = ttk.Notebook(self.main_frame)
		self.notebook = ttk.Notebook(self.main_frame)
		self.notebook1 = Frame(self.notebook)
		self.notebook2 = Frame(self.notebook)
		# self.notebook3 = Frame(self.notebook)
		# self.notebook4 = Frame(self.notebook)

		self.notebook.add(self.notebook1,text='Files')
		self.notebook.add(self.notebook2,text='Donation')

		# self.notebook.grid(row=7,column=0,columnspan=8,sticky='WE')

		self.list_copies=ttk.Treeview(self.notebook1,height=20,column=('uno','dos'))
		# self.list_copies.TAG(background='red')

		self.list_copies.column('#0',width=45 )
		self.list_copies.column('#1',width=465)
		self.list_copies.column('#2',width=60 )
		self.list_copies.heading('#0',text='#',anchor='center')
		self.list_copies.heading('#1',text='Files',anchor='center')
		self.list_copies.heading('#2',text='Size',anchor='center' )

		self.btn_update = Button(self.notebook1,text= 'update',image=self.img_update,background=skin ,command=self.refrech_data   ,border=0 ,activebackground='#504040' )
		self.btn_remove = Button(self.notebook1,text= 'remove',image=self.img_remove,background=skin ,command=self.delete_select  ,border=0 ,activebackground='#504040' )
		self.btn_clear	= Button(self.notebook1,text= 'clear', image=self.img_clear ,background=skin ,command=self.clear_data     ,border=0 ,activebackground='#504040' )
		self.btn_save	= Button(self.notebook1,text= 'save' , image=self.img_save  ,background=skin ,command=self.save_data      ,border=0 ,activebackground='#504040' )
		self.btn_load	= Button(self.notebook1,text= 'save' , image=self.img_load  ,background=skin ,command=self.load_data      ,border=0 ,activebackground='#504040' )

		self.text_donation='Usted puede ser parte de este proyecto Opensource haciendo una pequena contribucion a su gusto desde centavos hasta un dolar o lo que estime conveniente el proyecto es sin animo de lucro.Estas donaciones se utilizaran nada mas y nada menos que para el auto-consumo energetico, ya que el proyecto es libre y sin pago alguno, pero la corriente, almuerzo etc.. es costeado por mi, solo pido que me entiendan, soy humano que no soy una maquina, simplemente les doy la herramienta ya frabicada'
		
		self.label_bitcoin 	= Label(self.notebook2,text=textwrap.fill(self.text_donation,80)  ,	background=skin ,border=0 ,activebackground='#504040' )

		
		self.LTC		= Button(self.notebook2,text= 'LTC'  , 	image=self.IMG_LTC ,background=skin ,border=3 ,activebackground='#504040', command=lambda : self.wallet(1))
		self.DOGE		= Button(self.notebook2,text= 'DOGE' ,	image=self.IMG_DOGE,background=skin ,border=3 ,activebackground='#504040', command=lambda : self.wallet(2))
		self.DASH		= Button(self.notebook2,text= 'DASH' ,	image=self.IMG_DASH,background=skin ,border=3 ,activebackground='#504040', command=lambda : self.wallet(3))
		self.BTC 		= Button(self.notebook2,text= 'BTC'  ,	image=self.IMG_BTC,	background=skin ,border=3 ,activebackground='#504040', command=lambda : self.wallet(4))
		self.BTCH 		= Button(self.notebook2,text= 'BTCH' ,	image=self.IMG_BTCH,background=skin ,border=3 ,activebackground='#504040', command=lambda : self.wallet(5))


		self.LABEL_LTC	=  Label(self.notebook2,text= 'LTC'  ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_DOGE	=  Label(self.notebook2,text= 'DOGE' ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_DASH	=  Label(self.notebook2,text= 'DASH' ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_BTC 	=  Label(self.notebook2,text= 'BTC'  ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_BTCH =  Label(self.notebook2,text= 'BTCH' ,background=skin ,border=0 ,activebackground='#504040' )

		self.PHOTO_COIN_WALLET	=  Label(self.notebook2,image=self.IMG_WALLET_BTC,text= 'PHOTO'  ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_COIN_WALLET	=  Label(self.notebook2,text= 'BTC:'  ,background=skin ,border=0 ,activebackground='#504040' )
		self.LABEL_COIN_NOTE	=  Label(self.notebook2,text= 'Double clip to select:\n   <CRTL+C>  COPY  to Clipboard\n    <CRTL+V> PASTE to Clipboard',background=skin ,border=0 ,activebackground='#504040' )
		self.text_wallet.set('1McoX3eEHgzqszf6dRdngQRhWcvhAfiZWn')

		self.ENTRY_COIN_WALLET	=  Entry(self.notebook2,textvariable=self.text_wallet  ,highlightbackground='#504040',selectbackground='red',highlightcolor='#504040',foreground='yellow' ,border=0  ,width=40)
		# self.ENTRY_COIN_WALLET.config(background='red')
		# self.ENTRY_COIN_WALLET.event_delete('<<Paste>>','<Control-v>')
		# self.ENTRY_COIN_WALLET.event_add('<<Paste>>','<Control-q>')

		# self.LABEL_COIN_WALLET.config(state='disable
		# self.LABEL_COIN_WALLET.config(bg=self.LABEL_COIN_WALLET.cget('bg'))


		# self.btn_themes= ttk.Spinbox()
		# label logo imagen
		# footer
		# x=s.theme_names()
		self.themes=ttk.Combobox(value=('Dark','Light'),text='arc',textvariable=self.ejemplo,width=6)
		# self.themes=ttk.Spinbox(value=s.get_themes(),text='arc',textvariable=self.ejemplo,width=6,command=lambda : s.theme_use(self.themes.get()))
		
		#################### all frames inside ###################################
		PATH='/tmp/litecopy.txt'
		PATH_DIRECTION='/tmp/path.txt'.format(USER)
		read_copy.copying.read_and_insert(self)

		self.start_grids()
	def progreso(self,porcentage):
		root.title(porcentage)
		# print('hello')
	######################### remove

	def wallet(self,arg):
		# IMG_WALLET_LITE 1
		# IMG_WALLET_DOGE 2
		# IMG_WALLET_DASH 3
		# IMG_WALLET_BTC  4
		# IMG_WALLET_BTCH 5
		if arg == 1:
			self.PHOTO_COIN_WALLET.config(image=self.IMG_WALLET_LITE)
			self.LABEL_COIN_WALLET.config(text='LTC:')
			self.text_wallet.set('LanfsuEzoKPnSo277x4M1jbvSyqLZE5ru5')
		elif arg == 2:
			self.PHOTO_COIN_WALLET.config(image=self.IMG_WALLET_DOGE)
			self.LABEL_COIN_WALLET.config(text="DOGE:")
			self.text_wallet.set('D5d1MYJtKz9b1XT3sn5fFUZeSVdD2ZZmdb')
		elif arg == 3:
			self.PHOTO_COIN_WALLET.config(image=self.IMG_WALLET_DASH)
			self.LABEL_COIN_WALLET.config(text="DASH:")
			self.text_wallet.set('XuEQ6R6Siq6xg9ThiGvtJLBszxeHEEpUyp')
		elif arg == 4:
			self.PHOTO_COIN_WALLET.config(image=self.IMG_WALLET_BTC)
			self.LABEL_COIN_WALLET.config(text="BTC:")
			self.text_wallet.set('1McoX3eEHgzqszf6dRdngQRhWcvhAfiZWn')
		elif arg == 5:
			self.PHOTO_COIN_WALLET.config(image=self.IMG_WALLET_BTCH)
			self.LABEL_COIN_WALLET.config(text="BTCH:")
			self.text_wallet.set('qr2wk07ms425rffnuqnnugtqysevw9jujyw5tjxrek')
		
	def delete_select(self):
		read_copy.copying.delete_select_position(self)
		
	def clear_data(self):
		try:
			read_copy.copying.removing(self)
		except FileNotFoundError:
			self.answer=messagebox.showinfo('Info','No more files to delete 	' )
	def save_data(self):
		read_copy.copying.save_data_store(self)

	def load_data(self):
		read_copy.copying.load_data_store(self)
	def refrech_data(self):
		for i in self.list_copies.get_children():
			self.list_copies.delete(i)

		read_copy.copying.read_and_insert(self)
		

	###########################
	def press_theme(self):
		# print(self.themes.get())
		pass

	def start_grids(self):
		read_copy.copying.start_widget(self)
		# list of copies

	def copy_pass(self):
		global one_time
		# self.start = read_copy.copying.start_copy(self)
		try:
			# self.btn_2.config(state='disable')

			if one_time: # if one_time == 1:
				self.btn_stop.grid(row=5,column=5,padx=0)
				self.btn_2.destroy()

				one_time=0
			

			start_copy=Thread(target=read_copy.copying.start_copy(self))
			start_copy.start()
			# x=Process()
			# print(x)
			# process = start_copy.Process(os.getpid())
			# print(process,'aaaaaaaaa')

		except ZeroDivisionError:
			pass
			# print('by')

	def update_list(self):
		self.verify = os.stat('/tmp/litecopy.txt')

		while True:
			time.sleep(4)
			try:
				self.verify_now = os.stat('/tmp/litecopy.txt').st_size
				if self.verify_now != self.verify.st_size:
					# print('cambios')
					for i in self.list_copies.get_children():
						self.list_copies.delete(i)
					read_copy.copying.read_and_insert(self)
					self.verify = os.stat('/tmp/litecopy.txt')

				else: 
					pass
			except FileNotFoundError:
				break
	def chek(self,arg=0):
		cheking=arg
		return cheking

	def stop_button(self):######################################ewrwerwrerwe
		global chek
		if chek:
			# print('stop')
			self.btn_play.grid(row=5,column=5,padx=0)
			self.btn_stop.grid_forget()
			read_copy.copying.stop_copy(self)

			chek=0
		else:
			# print('continue_copy')
			self.btn_play.grid_forget()
			self.btn_stop.grid(row=5,column=5,padx=0)
			read_copy.copying.continue_copy(self)


			chek=1

	def pass_button(self):
		read_copy.copying.pass_copy(self)
		# x=Toplevel()
		# val=StringVar()
		# self.lab.set('hola mundo')
		# self.lab = Entry(x,text='hola mundo',textvariable=val).grid()
		
	def ask_cancel(self):
		read_copy.copying.exit_supercopy(self)

	def open_box_treview(self):
		if self.open_box_treview:
			x=read_copy.copying.open_list(self,1)
			self.open_box_treview=False
		else:
			x=read_copy.copying.open_list(self,0)
			self.open_box_treview=True

if __name__ == '__main__':

	
	try:
		root = Tk()
		root.resizable(width=False,height=False)
		root.iconphoto(False,tkinter.PhotoImage(file='/usr/share/icons/litecopy/image.png'))
		# root.attributes("-alpha",0.1)
		SuperCopy(root,Thread)
		root.grid()
		root.mainloop()
	except IndexError:
		os.remove('/tmp/litecopy.txt')


	