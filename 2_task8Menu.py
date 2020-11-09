import os
from task8input import Keyboard
from task8input import Voice


#step 3: After take input type it show menu with take perameter of input type
def menu(intype):
	
	print("\nInput Type:"+intype)
	menu_loop = True
	while menu_loop:
		print(20*"-"+"Main Menu"+"-"*20) #main menu
		print("Program                      |\tCommand")
		
		print("""------------------------------------------
Linux                        |\tLinux	
Hadoop                       |\thdfs
AWS                          |\taws
Networking                   |\tnet 
Docker	                     |\tdocker
Remote Login                 |\tremote
clear screen                 |\tclear
Back to Input Selection      |\tback
	""")
		if intype == 'keyboard':
			keyin = Keyboard() #go to keyboard function from task8input
			
		elif intype == 'voice':
			keyin = voice()	#go to Voice function from task8input
		
		
		if keyin == 'Linux': #secondary_menu
			Linux_loop = True
			while Linux_loop:
				os.system("clear")
				print("\n"+20*"-"+"Linux menu"+"-"*20)
				print("    Program                      |\tCommand")
				print("""----------------------------------------------				
    Calender                     |\tcal
    Date                         |\tdate
    Hard disk Details            |\tHDD
    Yum Configuration            |\tyumC
    Install Softwares            |\tinstall
    WebServer Configuration      |\twebC
    Particion                    |\tdiskP	
    Back to previous menu        |\tback
		    """)
				
				if intype == 'keyboard':
					lchoose = Keyboard()
			
				elif intype == 'voice':
					lchoose = voice()
				 
				
				
				if lchoose == 'cal':
					return("Linux-cal",intype) #return to function where called (input_type) with input type
				
				elif lchoose == 'date':
					return("Linux-date",intype)
				
				elif lchoose == 'HDD':
					return("Linux-HDD",intype)
					
				elif lchoose == 'yumC':
					return("Linux-yumC",intype)
				
				elif lchoose == 'install':
					return("Linux-install",intype)
				
				elif lchoose == 'webC':
					return("Linux-webC",intype)
				
				elif lchoose == 'diskP':
					return("Linux-diskP",intype)
					
				elif lchoose == 'back':
					Linux_loop = False	

				else:
					print("Invalid Input")
				
		
		
		
		elif keyin == 'docker':
			docker_loop = True
			while docker_loop:
				os.system("clear")
				print("\n"+20*"-"+"Docker menu"+"-"*20)
				print("    Program                      |\tCommand")
				print("""--------------------------------------------------			
	Download image	             |\tpullI
	Launch Container             |\trunC
	Stop Container	             |\tstopC
	Start Container	             |\tstartC
	Rename Container             |\trenameC
	Remove Container             |\trmC
	Remove Image	             |\trmI
	Back to previous menu        |\tback
				""")
				
				if intype == 'keyboard':
					docker_choose = Keyboard()
			
				elif intype == 'voice':
					docker_choose = voice()	
				
				
				if docker_choose == 'pullI':
					return("docker-pullI",intype)
				
				elif docker_choose == 'runC':
					return("docker-runC",intype)
				
				elif docker_choose == 'stopC':
					return("docker-stopC",intype)
				
				elif docker_choose == 'startC':
					return("docker-startC",intype)
					
				elif docker_choose == 'renameC':
					return("docker-renameC",intype)
					
				elif docker_choose == 'rmC':
					return("docker-rmC",intype)
				
				elif docker_choose == 'rmI':
					return("docker-rmI",intype)
				
				elif docker_choose == 'back':
					docker_loop = False	
					
				else:
					print("Invalid Input")
		
		
		elif keyin == 'remote':
			return("remote",intype)
			
		elif keyin == 'clear':				
			return("clear",intype)
			
		elif keyin == 'back':
			return ('0',intype)
					
		else:
			print("Invalid Input")
				
			
		"""elif keyin == 'hdfs':
			print(
				)
			hdfs_choose = input("Command:")

		elif keyin == 'aws':
			print(
				)
			aws_choose = input("Command:")

		elif keyin == 'net':
			print(
				)
			net_choose = input("Command:")"""		
