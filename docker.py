import os

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