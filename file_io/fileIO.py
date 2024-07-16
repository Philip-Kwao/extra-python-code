# names = []

# for _ in range(3):
#     ask = input("Mention name: ")
#     names.append(ask)

# for name in sorted(names):
#     print(name)

# name = input("Write something: ")

# file = open("name.txt", "a")

# file.write(name)
# file.close()

# with open("name.txt","a") as file:
#     file.write(f"{name} \n")


# ### Read the lines in the file

# with(open("name.txt", 'r')) as file:
#     for line in file:
#         print(line.rstrip())

# ### SORT the items in the file before view

affirmations = []

with(open("name.txt")) as file:
    for item in file:
        affirmations.append(item.rstrip())
for affirm in sorted(affirmations):
    print(affirm)