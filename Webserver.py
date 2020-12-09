import subprocess
from os import system


def setweb():
    system("tput setaf 2")
    print("\nApache websever has loaded properly")
    system("tput setaf 7")
    print("""Tell me from where you want to load the website :
    1.download web page from github
    2.copy local web page to the webserver
    3.back
    """)
    choice= int(input("Enter your choice : "))
    if choice==1:
        url =input("Enter the github url: ")
        name = input("Ener your github's project name: ")
        ip= subprocess.getoutput(["hostname -I | awk '{print $1}'"]) 
        system("clear")
        subprocess.run(["yum","install","git","-y"])
        system("git clone {0}  /var/www/html/{1} ".format(url,name))
        system("/usr/sbin/httpd -k restart")
        system("tput setaf 2")
        print("\nweb server started successfully !!")
        system("tput setaf 1")
        print("\nurl of webserver is : {0}/{1}/ ".format(ip,name))
        system("tput setaf 2")
        input("\nPress enter for continue...")
        system("tput setaf 7")
    elif choice==2:
        location = input("Enter your website full local location that you want to deploy : ")  
        ip= subprocess.getoutput(["hostname -I | awk '{print $1}"]) 
        system("sudo yes | cp {} /var/www/html/ ".format(location))
        system("/usr/sbin/httpd -k restart")
        system("tput setaf 2")
        print(" web server started successfully !!")
        system("tput setaf 1")
        print("\nurl of webserver is : {0}/{1}/ ".format(ip,name))
        system("tput setaf 2")
        input("\nPress enter for continue...")
        system("tput setaf 7")

def webserver():
    try:
        subprocess.run(["yum","install","httpd","-y"])
    except Exception as e:
        subprocess.run(["tput","setaf","1"])
        print("Error")
        print(e)
    else:
        setweb()