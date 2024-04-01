dictionary = {}

dictionary["Name"] = "Lhakpa"
dictionary["age"] = 20
dictionary["subject"] = ["Math","Science","Nepali"]
dictionary["Education"] = {
    "School":{
    "Name" : "Xavier School",
    "Address" : "Kalopul ,Kathmamndu"
},
"High school":{
    "Name" : "Xavier International College",
    "Address" : "Boudha , Kathmandu"
}}
print(dictionary)

# for i in dictionary.keys():
#     print(i)
    
# for i in dictionary["subject"][0]:
#     print(i, end="")

#Accessing element of nested dictionary from for loop
for i,j in dictionary["Education"]["School"].items():
    print(i,"=",j)

dictionary = {key:{nestkey:
{subnestedkey:value}}}
print(dictionary["Education"]["School"]["Name"])