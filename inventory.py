import time
import csv
import glob

#Constants
LOCATION = 0
NAME = 1
ID = 2
COUNT = 3

inv_dict = dict()
i = 0

file_list = glob.glob('*-Inventory.txt')

for file in file_list:
    inv_file = list(csv.reader(open(file, 'rb'), delimiter='\t'))
    file_name_list = file.split("-Inventory.txt")
    char_name = file_name_list[0];

    for x in range(1, len(inv_file)):
        key = i
        id = inv_file[x][ID]
        name = inv_file[x][NAME]
        location = inv_file[x][LOCATION]
        count = inv_file[x][COUNT]
    
        # Ignore any ids that are 0 - those are empty slots
        if id != "0":
            inv_dict[key] = [char_name, id, name, location, count]
            
        # Increment i
        i = i + 1

out_file = open("FullInventory.txt", "w")

out_file.write("Character, Item, Location, Count, Full Update " + time.strftime("%d/%m/%Y") + ",NFP Bank = Poapieces; casterspells; moreagunk; priestspells,EC Tunnel = agpotgem; platbank; agxtralewt\n")
for k,v in sorted(inv_dict.items()):
    out_file.write(str(v[0]) + "," + str(v[2]) + "," + str(v[3]) + "," + str(v[4]) + "\n")
