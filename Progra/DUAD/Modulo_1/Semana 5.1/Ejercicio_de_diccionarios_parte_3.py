list_of_keys=["Password","verification Code"]

user= {
    "Name": "Alvaro Vega",
    "Email":"alvega@CORP.com",
    "Password": 12345,
    "verification Code": 1452
}

for keys in list_of_keys:
    user.pop(keys)

print(user)

