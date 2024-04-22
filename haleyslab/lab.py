refname = []
refrt = []
# Open the file
with open("list1.csv", "r") as file:
    # Read each line
    file_text = file.read()
    filtered_file = file_text.replace("\n", "")
    file_list1 = filtered_file.split(",")
#print(file_list1)
with open("list2.csv", "r") as file:
    # Read each line
    file_text = file.read()
    filtered_file = file_text.replace("\n", "")
    file_list2 = filtered_file.split(",")
#print(file_list2)

for n in file_list1:
    if file_list1.index(n) % 2 == 0:
        refname.append(n)
    elif file_list1.index(n) % 2 == 1:
        refrt.append(n)

#print(refname)
#print(refrt)

data_rt = []
data_height = []
data_area = []

#SPLITTING SECOND LIST
for n in file_list2:
    if file_list2.index(n) % 3 == 0:
        data_rt.append(n)
    elif file_list2.index(n) % 3 == 1:
        data_height.append(n)
    elif file_list2.index(n) % 3 == 2:
        data_area.append(n)

#print(data_rt)
#print(data_height)
#print(data_area)


#finding closeest number
match_list = []
templist = []
for rt_num in refrt:
    for data_rt_num in data_rt:
        if float(rt_num) != float(data_rt_num):
            difference = abs(float(rt_num) - float(data_rt_num))
            templist.append(difference)
    match_list.append(templist.index(min(templist)))
    templist.clear()
#print(match_list)

#FINAL LIST
final_list_rt = []
final_list_hgt = []
final_list_area = []
for num in match_list:
    for drt_num in data_rt:
        if data_rt.index(drt_num) == num:
            final_list_rt.append(float(drt_num))
    for dhgt_num in data_height:
        if data_height.index(dhgt_num) == num:
            final_list_hgt.append(float(dhgt_num))
    for darea_num in data_area:
        if data_area.index(darea_num) == num:
            final_list_area.append(float(darea_num))

print(final_list_rt)
print(final_list_hgt)
print(final_list_area)

        