# dictinary are ordered
dict = {
    "harsh": "human being",
    "spoon": "object",
    28: "harsh bailurkar"
}
print(dict["harsh"])
print(dict[28])
print(dict.get("name"))  # will print none if key is not present in dict
# print(dict["name"])         this will throw an error
print(dict.keys())

print(dict.items())

# traversing the dictinary

for i in dict.keys():
    print(dict[i])
    print(f"the value of key {i} is {dict[i]} ")

