import os
import getpass 


os.system("tput setaf 3")
print("\t\t\t Welcome to Menu")
os.system("tput setaf 7")
print("\t\t\t-----------------------------------")


passwd = getpass.getpass("Enter your password :")
 
if passwd!='redhat':
	print("password incorrect..")
	exit()
r = input("where you want to run this menu ?(local/remote):")
print(r)

def docker():
	
	os.system("tput setaf 2")
	ch=input("\n Tell what you want to do in docker:")
	os.system("tput setaf 7")
	if("permanent" in ch):	
		os.system("systemctl enable docker")
	elif("start" in ch):
		os.system("systemctl start docker")
	elif("status" in ch):
		os.system("systemctl status docker")
	elif("restart" in ch):
		os.system("systemctl restart docker")
	elif("stop" in ch):
		os.system("systemctl stop docker")
	elif("info" in ch  or "information" in ch):
		os.system("docker info")
	elif("install " in ch):
		os.system("yum install docker-ce --nobest")
	elif("container" in ch and "docker" in ch  or "running container" in ch):
		os.system("docker ps -a")
	elif("pull" in ch and  "ubuntu" in ch ):
		os.system("docker pull ubuntu:20.10")
	elif("pull" in ch and "centos" in ch):
		os.system("docker pull centos")
while  True :
	os.system("clear")
	print("""\n
	Press 1 :to run date
	Press 2 :to run cal
	Press 3 :to reboot
	Press 4 :to ceate user
	Press 5 :to exit
	Press 6 :for docker services
	""")
	ch=input("Enter ur choice  : ")
	print(ch)
	
	if r=="local":
		if int(ch) ==1:
			os.system("date")
		elif int(ch)==2:
			os.system("cal")
		elif int (ch) ==3:
			os.system("reboot")
		elif int(ch) ==5:
			exit()
		elif int(ch)==6:
			docker()
		else:
			print("not supported")
	elif r=="remote":
		ip=input("Enter remote ip:")
		print(ip)
		if int(ch) ==1:
			os.system("date")
		elif int(ch)==2:
			os.system("cal")
		elif int (ch) ==3:
			os.system("reboot")
		elif int(ch) ==5:
			exit()
		else:
			print("not supported")
	else: 
		print("not supported login")
	input("\n plz eneter to continue..")
