#!/usr/bin/env python3
import os
# You should make backups before using this tool... Just saying...

# Informations for you
prefix = "img"

# Récupération des noms de fichiers
os.system("ls > .file_list")
with open(".file_list") as file:
	lines = [line.rstrip() for line in file]
extension = ""
for i in range(len(lines)):
	if(lines[i][-4] == "."):
		extension = lines[i][-4:]
	elif(lines[i][-5] == "."):
		extension = lines[i][-5:]
	elif(lines[i][-6] == "."):
		extension = lines[i][-6:]
	else:
		print(f"Whuuut, on line {i} ????")

	if(i < 10 and i >= 0):
		new_name = prefix + "_0000" + str(i) + extension
	elif(i >= 10 and i < 100):
		new_name = prefix + "_000" + str(i) + extension
	elif(i >= 100 and i < 1000):
		new_name = prefix + "_00" + str(i) + extension
	elif(i >= 1000 and i < 10000):
		new_name = prefix + "_0" + str(i) + extension
	elif(i >= 10000):
        	new_name = prefix + "_" + str(i) + extension
	else:
		print("ERROR FILE NAME !!!")
	# print(f"{lines[i]} -> {new_name}")  # Uncomment first for testing
	os.system(f"mv {lines[i]} {new_name}")  # Comment first for testing

os.system("ls > .file_list_result")
with open(".file_list_result") as file:
	lines_result = [line.rstrip() for line in file]

print(f"{len(lines)} files to rename.")
print(f"{len(lines_result)} files renamed.")
if(len(lines) == len(lines_result)):
	print("Rien ne se créé, tout se transforme !")
else:
	print("Hum... Lavoisier ?")
