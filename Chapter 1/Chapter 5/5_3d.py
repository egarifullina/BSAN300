# To delete an entry from a dictionary, remove its key using the method pop 
# Pop expects a key and an optional default value as arguments 

info = {"name": "Sandy", "occupation": "manager"}
print(info.pop("job", None)) # None is returned if "job" is not found in info

print(info.pop("occupation")) # "manager" is returned and the key "occupation" is removed from info

print(info) # "occupation" is no longer in info