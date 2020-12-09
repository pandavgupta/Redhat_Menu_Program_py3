from os import system
import getpass
passwd="redhat"





def menuPage():
    while(True): 

      system("clear")
      system("tput setaf 6")
      print("""\n\n                                                                      ****Welcome to the Menu Page****
                                                     -----------------------------------------------------------------------------------------------
              \n\n\n""")
      system("tput setaf 7")
      print("""\tWhich task do you want to perform ::
\t  1.RHEL 8 (eg: date,stop firewall,etc)
\t  2.Hadoop (eg: configure datanode,masternode,etc)
\t  3.Docker (eg: configure docker,stop container,launch container,etc)
\t  4.Configure webserver
\t  5.Configure yum
\t  6.exit

      """)
      choice=int(input("Enter your choice (eg:1):" ))
      if choice == 1:
        import Rhel
        Rhel.rhel()
      elif choice==4:
        import Webserver
        Webserver.webserver()
      elif choice==5:
        import yumconf
        yumconf.yum()
      elif choice==6:
        system("clear")
        exit()
      else:
          system("tput setaf 1")
          print("!!! Wrong choice !!!")
          print ("Plz select one appropriate option..")
          system("sleep 2")






def loginPage():
  system("clear")
  system("tput setaf 2")
  print("""\n\n                                                                         ****Login Page****
                                                 --------------------------------------------------------------------------------------------
        \n\n\n""")
  system("tput setaf 7")
  while(True):
    system("tput setaf 7")
    pw = getpass.getpass("Enter you password : ")
    if pw== passwd :
        system("tput setaf 2")
        print("\nLogin successfully..\n Redirecting to Menu page.")
        system("sleep 2")
        return
    else:
        system("tput setaf 1")
        print("!!!!  Incorrect password  !!!!\n")



loginPage()
menuPage()
