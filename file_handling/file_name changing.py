import os
# for i in range(1,11):
#     file_name=f"file{i}.txt"
#     with open(file_name,'w') as file:
#         file.write(f"thsi is {file_name}\n")

# print("10 files created successfully")


for idx,file in enumerate(os.listdir(),start=1):
    file_root,file_ext=os.path.splitext(file)

    if file_ext=='.txt':
        new=f"Zakir's {idx}th file.txt"
        os.rename(file,new)

    else:
        continue
print("Files renamed successfully")