import os
from itertools import chain

def getPoisonedIPs(ipDict):
    rev_dict = {}

    for key, value in ipDict.items():
        rev_dict.setdefault(value, set()).add(key)

    result = set(chain.from_iterable(
            values for key, values in rev_dict.items()
            if len(values) > 1))

    return list(result)

def getPoisonedMACs(ipDict):
    rev_dict = {}

    for key, value in ipDict.items():
        rev_dict.setdefault(value, set()).add(key)
    
    result = [key for key, value in rev_dict.items()
    if len(value) > 1]

    return list(result)

outputFile = os.getcwd()+"\\ARPoutput.txt"
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

poisonedIPs = getPoisonedIPs(dict)
poisonedMACs = getPoisonedMACs(dict)

if len(poisonedIPs) == 0 and len(poisonedMACs) == 0:
    print("NETWORK SECURE!\nNo ARP Poisoning Detected!")
else:
    print("SECURITY BREACH!\nARP Poisoning Detected!")
    print(f"These IP addresses have the same MAC addresses: {poisonedIPs}")
    print(f"These MAC addresses are poisoned: {poisonedMACs}")