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


#finding closest number
match_list = []
templist = []
compare_list = []
for rt_num in refrt:
    for data_rt_num in data_rt:
        difference = abs(float(rt_num) - float(data_rt_num))
        templist.append(difference)
    compare_list.append(data_area[templist.index(min(templist)) - 1])
    compare_list.append(data_area[templist.index(min(templist))])
    compare_list.append(data_area[templist.index(min(templist)) + 1])
    match_list.append(data_area.index(max(compare_list)))
    templist.clear()
    compare_list.clear()
print(match_list)

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

# Example usage:
nums = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 2]
print(find_duplicate_indices(nums))


test_list1 = [37,4,85,2,3,5,17,99,99,34,25]

for x in test_list1:
    for y in test_list1:
        pass 
    
    