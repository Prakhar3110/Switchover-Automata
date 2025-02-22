import win32com.client
import os, time, sys

shell = win32com.client.Dispatch("WScript.Shell")

os.popen(r'''C:\Users\Jemema\Desktop\btp\Demo\Automata.exe''')
i=0
time.sleep(0.4)

files = os.listdir('Graphs')
for file in files :
	time.sleep(0.4)
	shell.SendKeys("^o")
	time.sleep(0.4)
	shell.SendKeys(file)
	time.sleep(0.4)
	shell.SendKeys("{ENTER}", 0)
	time.sleep(0.4)
	shell.SendKeys("%")
	time.sleep(0.4)
	shell.SendKeys("s")
	time.sleep(0.4)
	shell.SendKeys("{DOWN}")
	shell.SendKeys("{DOWN}")
	time.sleep(0.4)
	shell.SendKeys("{ENTER}", 0)
	time.sleep(0.4)
	shell.SendKeys("{ENTER}", 0)
	time.sleep(0.4)
	try :
		os.rename("Graphs/" + "SyncWord.tmp", "Graphs/" + file + "_SyncWord" + ".out")
	except :
		print(file + " not sync.")
	
	time.sleep(0.4)
  
	i = i + 1
	
	