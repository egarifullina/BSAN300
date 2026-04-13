# You can sort the list first the traverse it to print the entries of the dictionary in alphabetical order

info = {"occupation": "manager", "name": "Sandy"}

theKeys = list(info.keys()) # list of keys in info
theKeys.sort() # sort the list of keys

for key in theKeys:
    print(key, info[key])

    