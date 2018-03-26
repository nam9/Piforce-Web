import os, collections, signal, sys, subprocess, socket
import triforcetools
import logging
#from systemd import daemon
from time import sleep

logfile = open('/var/www/logs/log.txt', 'w')
rom_dir = '/boot/roms/'
logging.basicConfig(filename='/var/www/logs/debug.txt',level=logging.DEBUG)

while True:

                try:
                    triforcetools.connect('192.168.1.2', 10703)
                except:
                    #logfile.write("Error:\nConnect Failed")
			logging.debug('Error: Connection failed')
                    continue

                logfile.write(sys.argv[1])
		logging.debug('Connection Completed')

                triforcetools.HOST_SetMode(0, 1)
		logging.debug('HOST_SetMode Completed')
                triforcetools.SECURITY_SetKeycode("\x00" * 8)
		logging.debug('SECURITY_SetKeycode Completed')
				#argv[0] not games(selection)
                triforcetools.DIMM_UploadFile(rom_dir+sys.argv[1])
		logging.debug('DIMM_UploadFile Completed')
                triforcetools.HOST_Restart()
		logging.debug('HOST_Restart Completed')
                triforcetools.TIME_SetLimit(10*60*1000)
		logging.debug('TIME_SetLimit Completed')
                triforcetools.disconnect()
		logging.debug('Disconnect Completed')

                #logfile.write("Transfer\nComplete!")
                sleep(5)
		exit()
				

