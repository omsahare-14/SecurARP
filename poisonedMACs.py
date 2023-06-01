import os
import warnings

warnings.filterwarnings("ignore")

def getPoisonedMACs(ipDict):
    rev_dict = {}

    for key, value in ipDict.items():
        rev_dict.setdefault(value, set()).add(key)
    
    result = [key for key, value in rev_dict.items()
    if len(value) > 1]

    return list(result)