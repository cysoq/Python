import json 

# Have to first open the file
with open('states.json') as f:
    data = json.load(f) # load it in with .load
    
# Can now iterate over it 
for state in data["states"]:
    print(state["name"], state["abbreviation"])
    
# Can delete and change the data 
for state in data["states"]:
    del state["abbreviation"]
    
# newStates will now have no abbreviations
with open("newStates.json", "w") as f:
    json.dump(data, f, indent=2) # can also pass in a indent value to make it write cleaner