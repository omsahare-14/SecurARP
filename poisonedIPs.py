from itertools import chain
import warnings

warnings.filterwarnings("ignore")

def getPoisonedIPs(ipDict):
    rev_dict = {}

    for key, value in ipDict.items():
        rev_dict.setdefault(value, set()).add(key)

    result = set(chain.from_iterable(
            values for key, values in rev_dict.items()
            if len(values) > 1))

    return list(result)