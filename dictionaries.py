person = {
    "name": "Thet Tun Kyaw",
    "age": 24,
    "address": "Myanmar",
}

print("\n----- Before Changed -----")
print("person:", "\t\t\t", person)
print("person['key']:", "\t\t", person["name"], person["age"], person["address"])
print("person.get('key'):", "\t", person.get("name"), person.get("age"), person.get("address"))
print("person.keys():", "\t\t", person.keys())
print("person.values():", "\t", person.values())

person["age"] = 25

print("\n----- After Changed -----")
print("person:", "\t\t\t", person)
print("person['key']:", "\t\t", person["name"], person["age"], person["address"])
print("person.get('key'):", "\t", person.get("name"), person.get("age"), person.get("address"))
print("person.keys():", "\t\t", person.keys())
print("person.values():", "\t", person.values())