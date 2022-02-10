weekend = {"Sun": "Sunday","Sat": "Saturday"}
capitals = {}
capitals["svk"] = "Bratislava"
capitals["deu"]="Berlin"
capitals["dnk"]="Copenhagen"

print(weekend["Sun"])
print(capitals["svk"])

value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything




