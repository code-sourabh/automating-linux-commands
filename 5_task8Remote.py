import os
#step 6: Remote login and processing
def Remote(techin):
	IP = input("Enter IP Address for Remote Login:")
	
	if techin == 'remote':
		os.system("ssh {}".foramt(IP))
	
	elif techin == 'Linux-cal':
		os.system("ssh {} sh calendar.sh".format(IP))
		
	elif techin == 'Linux-date':
		os.system("ssh {}  sh date.sh".format(IP))
		
	elif techin == 'Linux-HDD':
		os.system("ssh {} sh hardDiskDetails.sh".format(IP))
		
	elif techin == 'Linux-yumC':
		os.system("ssh {} sh yumConf.sh".format(IP))
	
	elif techin == 'Linux-install':
		os.system("ssh {} sh installingSoftware.sh".format(IP))
		
	elif techin == 'Linux-webC':
		os.system("ssh {} sh webServerConf.sh".format(IP))
	
	elif techin == 'Linux-diskP':
		os.system("ssh {} echo Work_in_progress".format(IP))
		
	elif techin == 'docker-pullI':
		os.system("ssh {} echo Work_in_progress".format(IP))
		
	elif techin == 'docker-runC':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'docker-stopC':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'docker-startC':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'docker-renameC':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'docker-rmC':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'docker-rmI':
		os.system("ssh {} echo Work_in_progress".format(IP))
	
	elif techin == 'clear':
		os.system("ssh {} clear".format(IP))
	
	"""elif techin == 'docker-pullI':
		os.system("ssh {} echo Work_in_progress")
	
	elif techin == 'docker-pullI':
		os.system("ssh {} echo Work_in_progress")
	
	elif techin == 'docker-pullI':
		os.system("ssh {} echo Work_in_progress")"""
