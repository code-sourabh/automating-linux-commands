import os
import time
from task8Menu import menu
from task8Local import Local
from task8Remote import Remote

#step 5: select input type and take the choosed value from menu 
def login(option,intyper):
	if option == '0':
		input_type()
		
	os.system("clear")	
	logi = input("""\nSelect Login Type:
Local Login (press:'ll')
Remote Login (press:'rl')
Type 'back' to go to main_menu
:""")
		
	if option == 'remote': #if user want only remotely login
		Remote(option)
		
	else:
		if logi == 'll': #local login
			os.system("clear")
			print("Login type: LOCAL")
			Local(option)
	
		elif logi == 'rl': #remote login
			os.system("clear")
			print("Login type: LOCAL")
			Remote(option)
		
	option,intyper = menu(intyper)	#get back to menu with previous input type
	login(option,intyper)
	
	
			
#step2:then reach and choose input type	
def input_type():
	os.system("clear")
	print(20*"-"+"Welcome to Menu Program"+"-"*20)
	intype = input("""\nChoose Input type:
1. Keyboard (Press 1 or Type 'keyboard')
2. Voice (Press 2 or Type 'voice')
Type 'exit' to exit
:""")


	if intype == '1' or intype == 'keyboard':
		option,intyper = menu('keyboard')#call menu and take value return back
		if option == '0':
			input_type()
		else:	
			login(option,intyper) #take return value from main fuction go to login function
		
	elif intype == '2' or intype == 'voice':
		option,intyper = menu('voice')#call menu and take value return back	
		if option == '0':
			input_type()
		else:
			login(option,intyper) #take return value from main fuction go to login function
	elif intype == 'exit' or intype == 'Exit' or intype == 'EXIT':
		print("BYE,BYE")
		exit()
			
	else:
		print("Invalid input selection")	
		exit()
		
#main: step 1:Program start from here
input_type() #call input_type function		
