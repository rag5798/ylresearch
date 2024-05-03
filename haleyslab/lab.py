import os.path as path

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
for n in range(0, len(file_list2)):
    if n % 3 == 0:
        data_rt.append(file_list2[n])
    elif n % 3 == 1:
        data_height.append(file_list2[n])
    elif n % 3 == 2:
        data_area.append(file_list2[n])

#print(len(data_rt))
#print(len(data_height))
#print(len(data_area))

def rerun_rt():
    match_list = []
    templist = []
    for rt_num in refrt:
        for data_rt_num in data_rt:
            difference = abs(float(rt_num) - float(data_rt_num))
            templist.append(difference)
        match_list.append(templist.index(min(templist)))
        templist.clear()
    return match_list

def find_duplicate_indices(nums):
    num_indices = {}
    duplicates = []

    for i, num in enumerate(nums):
        if num in num_indices:
            duplicates.append(num_indices[num])
            duplicates.append(i)
        else:
            num_indices[num] = i

    return duplicates



#finding closest number
match_list = []
templist = []
compare_list = []
for rt_num in refrt:
    for data_rt_num in data_rt:
        difference = abs(float(rt_num) - float(data_rt_num))
        templist.append(difference)
    compare_list.append(int(data_area[templist.index(min(templist)) - 1]))
    compare_list.append(int(data_area[templist.index(min(templist))]))
    compare_list.append(int(data_area[templist.index(min(templist)) + 1]))
    match_list.append(data_area.index(f'{max(compare_list)}'))
    templist.clear()
    compare_list.clear()
#print(match_list)

#if match_list has a dup then run find_closest_rt_dup()
if len(match_list) != len(set(match_list)):
    match_list_dup_indices = find_duplicate_indices(match_list)
    rt_logic = rerun_rt()
    for x in match_list_dup_indices:
        match_list[x] = rt_logic[x]


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

#print(final_list_rt)
#print(final_list_hgt)
#print(len(final_list_area))

for x in range(0, len(final_list_rt)):
    #print(x)
    with open('final.csv', 'a') as file:
        file.write(f'{final_list_rt[x]},{int(final_list_hgt[x])},{int(final_list_area[x])}\n')

def delete_file():
    #TODO Make a delete function that gets rid of the files list1.csv and list2.csv so there is only result file
    pass