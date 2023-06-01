import os
import asciiArt
import poisonedIPs
import poisonedMACs
import warnings

warnings.filterwarnings("ignore")

asciiArt.showName()

outputFile = "c:\\Users\\Public\\ARPoutput.txt"
os.system(f'cmd /c "arp -a > {outputFile}"')
f = open(outputFile, 'r')

outputArray = []
for data in f:
    data.replace(" ", "")
    " ".join(data.split())
    outputArray.append(data.split())

dict = {}
for element in outputArray:
    if element != [] and 'Interface:' not in element and 'Internet' not in element and element[1] != 'ff-ff-ff-ff-ff-ff':
        dict.update({element[0]:element[1]})

poisonedIPs = poisonedIPs.getPoisonedIPs(dict)
poisonedMACs = poisonedMACs.getPoisonedMACs(dict)

if len(poisonedIPs) == 0 and len(poisonedMACs) == 0:
    print("\033[32mNETWORK SECURE!\nNo ARP Poisoning Detected!\033[0m")
else:
    print("\033[31mSECURITY BREACH!\nARP Poisoning Detected!\033[0m")
    print(f"\033[31mThese IP addresses have the same MAC addresses: {poisonedIPs}\033[0m")
    print(f"\033[31mThese MAC addresses are poisoned: {poisonedMACs}\033[0m")

f.close()
os.remove(outputFile)
