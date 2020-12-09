import subprocess
def addfile():
    file=open("/etc/rc.d/rc.local","a")
    file.write("\nmount /dev/cdrom  /Repo ")
    file.close
    subprocess.run(["chmod","+x","/etc/rc.d/rc.local"])
    return


def localRepo():
    print("!!! Please ensure that iso file of redhat is connected")
    try:
      subprocess.run(["mkdir","/Repo"])
      subprocess.run(["mount","/dev/cdrom","/Repo"])
      addfile()
    except:
        print("Either redhat iso file is not connected or you don't have root permission!!!!")
        subprocess.run(["sleep","2"])
    else:
        file= open("/etc/yum.repos.d/redhat.repo","w")
        file.write("""[redhatdvd-conf-1] 
baseurl=file:///Repo/AppStream/ 
gpgcheck=0 
[redhatdvd-conf-2]
baseurl=file:///Repo/BaseOS/
gpgcheck=0
        """)
        file.close
        status=subprocess.getstatusoutput("yum repolist")[0]
    if status == 0:
        subprocess.run(["tput","setaf","2"])
        print(" Yum configured successfully!!!!")
        subprocess.run(["sleep","1"])
    else :
        subprocess.run(["tput","setaf","1"])
        print(" Yum not configured !!!!")
    return


        



def onlineRepo():
    try:
        subprocess.getstatusoutput("sudo dnf install --nogpgcheck https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")[0]
        subprocess.getstatusoutput("sudo dnf install --nogpgcheck https://mirrors.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://mirrors.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm-y")[0]
    except:
        print("Either you don't have internet connection in our system or you don't have required permission!!!!")
        subprocess.run(["sleep","1"])
    else:
        subprocess.run(["tput","setaf","2"])
        print(" Yum configured successfully!!!!")
        subprocess.run(["sleep","1"])


def yum():
    while(True):
      subprocess.run(["clear"])
      subprocess.run(["tput", "setaf","2"])
      print("""\n\n                                                                      ****Yum Configuration**** 
                                                --------------------------------------------------------------------------------------------------------
       \n\n\n""")
      subprocess.run(["tput", "setaf","7"])
      print("""select the way you want to configure yum :
         1.Using redhat dvd
         2.Using some online repository
         3.Back
         4.exit
      """)
      choice=int(input("Enter your choice : "))

      if choice== 1:
          localRepo()
      elif choice==2:
          onlineRepo()
      elif choice==3:
          return
      elif choice==4:
          subprocess.run(["clear"])
          exit()
      else :
          subprocess.run(["tput", "setaf 1"])
          print("Invalid option \n Plz choose coorect option")
          subprocess.run(["sleep","2"])
