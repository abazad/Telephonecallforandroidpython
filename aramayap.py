print('www.ebubekirbastama.com')
import subprocess
numara=input("Type the number you want to call"+"!\n")
komutumuz = 'adb.exe shell am start -a android.intent.action.CALL -d tel:'+numara
piey = subprocess.Popen(komutumuz, shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = piey.communicate()
print ("Call started.")
print('www.ebubekirbastama.com')
