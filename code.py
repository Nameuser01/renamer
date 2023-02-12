#!/usr/bin/env python3
import os
import time
import random
import string

# String generation
randstr = string.ascii_lowercase
add = ''.join(random.choice(randstr) for i in range(2))

prefix = "file"

# Récupération des noms de fichiers
os.system("ls | sort -n > .file_list")

f = open(".file_list", "r")
filenames_tmp = f.readlines()
f.close()

compteur = 0
filenames = []
for line in filenames_tmp:
	filenames.append(line.replace("\n", ""))
	compteur += 1

for i in range(len(filenames)):
	extension = ""
	if(filenames[i][-4] == "."):
		extension = filenames[i][-4:]
	elif(filenames[i][-5] == "."):
		extension = filenames[i][-5:]
	elif(filenames[i][-6] == "."):
		extension = filenames[i][-6:]
	else:
		print(f"Erreur à la ligne : {i}")

	new_name = f"{prefix}_{add}_{abs(len(str(compteur-1))-len(str(i)))*'0'}{str(i)}{extension}"
	os.system(f"mv {filenames[i]} {new_name}")

os.system("ls > .file_list_result")
with open(".file_list_result") as file:
	lines_result = [line.rstrip() for line in file]

print(f"{len(filenames)} files to rename.")
print(f"{len(lines_result)} files renamed.")
if(len(filenames) == len(lines_result)):
	print("OK !")
else:
	print("Erreur: perte de fichiers")