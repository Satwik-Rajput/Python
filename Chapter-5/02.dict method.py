dict ={"Satwik" : 100,
       "Satyam" : 99,
       "Akash" : 80}

print(dict.get("Satwik")) # .get() method is used to get the value of the key

print(dict["Satwik"]) # [" "] is use to get the value of the key,but if the key is not present then it will throw error.

print(dict.get("Rohan")) #if key not present then it will return none

print(dict.items()) # .items() method is used to get the key and value pair

print(dict.keys()) # .keys() method is used to get the keys

dict.update({"Satyam":90}) # .update() method is used to update the value of the key

print(dict)