import subprocess
from os import system
import getpass

def user():
  while(True):
    system("clear")
    print("""\n\n     1.list all the user
     2.add new user
     3.delete existing user
     4.back
     5.exit
  \n\n""")
    choice= int(input("Enter your choice : "))
    if choice == 1:
      system("ls /home/")
      input("\n Press any key to continue...")
    elif choice==2:
      uname=input("Give your user name : ")
      system("useradd {}".format(uname))
      system("passwd {}".format(uname))
      system("{} user created successfully".format(uname))
      input("\n Press any key to continue...")
    elif choice==3:
      system("ls /home/")
      which=input("which user do you want to delete : ")
      try:
        system("userdel -rf {}".format(which))
      except Exception as e:
        print("\n!!failed to delete this user!!")
        print(e)
        input("\n Press any key to continue...")
      else:
        print("{} user deleted successfully..")
        input("\n Press any key to continue...")
    elif choice==4:
      rhel()
    elif choice==5:
      system("clear")
      exit()


def rhelyum():
  while(True):
    system("clear")
    print("""\n\n     1.list all the configured repository
     2.list all repoistery file
     3.Add new repository
     4.Delete existing repository 
     5.back
     6.exit
  \n\n""")
    choice= int(input("Enter your choice : "))
    if choice == 1:
      system("yum repolist")
      input("\n Press any key to continue...")
    elif choice==2:
      system("ls /etc/yum.repos.d/")
      input("\n Press any key to continue...")
    elif choice == 3:
      name=input("Enter repositorys name : ")
      url=input("Enter url of the repository : ")
      id=input("Give one unique id/name for this new repository : ")
      check=int(input("Do you want to verify this repo again and again or not(if yes->1 or no->0) : "))
      repo=open("/etc/yum.repos.d/{name}.repo","a")
      repo.write("""\n[{id}]\nbaseurl={url}\ngpgcheck={check}\n""")
      repo.close()
      print("Repository added successfully..")
    elif choice== 4:
      system("ls /etc/yum.repos.d/")
      rep=input("Enter which repository do you want to delete : ")
      try:
        system("rm -rf /etc/yum.repos.d/{rep}")
      except Exception as e:
        print("Error")
        print(e)
        input("\n Press any key to continue...")
      else :
        print("Repository deleted successfully!!\n")
        input("\n Press any key to continue...")
    elif choice==5:
      rhel()
    elif choice==6:
      system("clear")
      exit()
    else:
      print("Invalid option!!")
      input("\n Press any key to continue...")






def mount():
  while(True):
    system("clear")
    print("""\n\n     1.list of all mounted folder
     2.mount a folder
     3.back
     4.exit
  \n\n""")
    choice= int(input("Enter your choice : "))
    if choice == 1:
      system("df -h")
      input("\n Press any key to continue...")
    elif choice==2:
      src=input("\nEnter the location of folder which you want to mount: ")
      dest=input("\nEnter the location of folder where you want to mount: ")
      try:
        system("mount {src} {dest} ")
      except  Exception as e:
        system("tput setaf 1")
        print(e)
        system("\nMount operation failed!!!")
        system("tput setaf 7")
        input("\n Press any key to continue...")
      else:
        print("\n Mounted successfuly")
        input("\n Press any key to continue...")
    elif choice == 3:
      system("clear")
      rhel()


def firewall():
  while(True):
    system("clear")
    print("""\n\n     1.check status of firewalld
     2.start firewalld 
     3.stop firewalld
     4.restart firewalld
     5.permanently disable firewalld
     6.permanently enable firewalld
     7.back
     8.exit
  \n\n""")
    choice= int(input("Enter your choice : "))
    if choice == 1:
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 2:
      system("systemctl start firewalld")
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 3:
      system("systemctl stop firewalld")
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 4:
      system("systemctl restart firewalld")
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 5:
      system("systemctl disable firewalld")
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 6:
      system("systemctl enable firewalld")
      system("systemctl status firewalld")
      input("\n Press any key to continue...")
    elif choice == 7:
      rhel()
    elif choice == 8:
      system("clear")
      exit()
    else :
      system("tput setaf 1")
      print("Invalid option !!!")
      system("tput setaf 7")






def rhel():
    while(True): 
      subprocess.run(["clear"])
      subprocess.run(["tput","setaf","2"])
      print("""\n\n                                                                   ****RHEL 8 Page****
                                       ---------------------------------------------------------------------------------------------------------------
       \n\n\n""")
      subprocess.run(["tput","setaf","7"])
      print("""     1.show date
     2.show calender
     3.Mount
     4.yum 
     5.firewall 
     6.user
     7.show routing table
     8.show ip Address
     9.back
     10.exit
      \n\n""")
      choice=int(input("Enter your choice : "))
      if choice==1:
        system("date")
        input("\n Press any key to continue...")
      elif choice==2:
        system("cal")
        input("\n Press any key to continue...")
      elif choice==3:
        mount()
      elif choice==4:
        rhelyum()
      elif choice==5:
        firewall()
      elif choice==6:
        user()
      elif choice==7:
        system("clear")
        print("\n")
        system("route -n")
        input("\n Press any key to continue...")
      elif choice==8:
        system("clear")
        print("\n")
        system("ifconfig")
        input("\n Press any key to continue...")
      elif choice==9:
        system("clear")
        return
      elif choice==10:
        system("clear")
        exit()
      else:
        system("tput setaf 2")
        print("Invalid Option!!!!")
        system("tput setaf 7")
        input("\n Press any key to continue...")
        


