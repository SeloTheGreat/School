import requests

name = input("Enter name of file including any extensions, leave blank for def=\"new_req.txt\"\n:") or "new_req.txt"
url = input("Enter full url to perform a get request from\n:")

file = open(name, "w")
print("CREATED FILE", name)

print("REQUESTING")
req = requests.get(url)
print("REQUEST COMPLETED")

print("WRITING TO FILE")
file.write(req.text)

req.close()
file.close()
print("TASK COMPLETE")
