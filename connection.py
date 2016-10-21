'''
Created on Oct 13, 2016

@author: paul c. schmitz
Program reads a list of IP addresses and passes them to 
the FTP command. FTP connects to each IP, prints their
directories, logs out, and connects to the next IP...
'''
import logging
from ftplib import FTP
logging.basicConfig(filename='ftp.log',level=logging.DEBUG)

ftp = FTP()
data = [line.rstrip('\n') for line in open('ipaddr.txt', 'r+')]       

for i in data:
    try:        
        ip = str(i)    
        log = open('ftp.log', 'a')
        #ftp.set_debuglevel(1)
        log.write("Connecting to {0}\n".format(i))
        print ("Connecting to {0}".format(i))
        ftp.connect(i, 2121)
        ftp.login()
        log.write("\n")
        log.write(ftp.getwelcome())
        print "Retrieving root directory..."
        log.write("\n")
        log.write("\n")
        print ""
        log.write(ftp.retrlines('LIST', log.write))
        ftp.retrlines('LIST')
        print ""
        log.write("\n")
        log.write("\n")
        print ("Disconnecting from {0}".format(i))
        log.write("Disconnecting from {0}...".format(i))
        print "##########################################\n"
        log.write("\n")
        log.write("################################\n")
        log.write("\n")
        ftp.quit()
        log.close
    except Exception:
        logging.exception("Error: ")
        log = open('ftp.log', 'a')
        print "Couldn't connect"
        print "fuck..."
        log.write("Couldn't connect\n")
        log.write("fuck...\n")
        log.write("################################\n")
        log.close
        pass        