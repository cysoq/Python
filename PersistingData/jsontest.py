import json 

people_string= '''
{
    "people": [
        {
            "name": "John Smith",
            "phone": "615-555-7164",
            "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"],
            "has_license": false
        },
        {
            "name": "Jane Doe",
            "phone": "560-555-5153",
            "email": null,
            "has_license": true
        }
    ]
}
'''

# Will load json data for python use
data = json.loads(people_string) # load(s) where the s denotes a string

print(data) # The whole thing
print(data["people"]) # Can get different parts of the data 
print(type(data)) # Can see that it is now a python dict 
print(type(data["people"])) # Can see that the dict[people] contains a list 
print(type(data["people"][0])) # Can see that the dict[people][0] contains a dict
print(type(data["people"][0]["name"])) # can get down to a string 
print(data["people"][0]["name"]) # print string
print()

# Can iterate through it as well
for person in data["people"]:
    print(person["name"])
    
# Can delete and change the json 
for person in data["people"]:
    del person["phone"]
    
# Collects the json 
new_string = json.dumps(data, indent=2, sort_keys=True) # indent can make it look better, and sort the keys 

# Can now see phone is gone
print(new_string)
