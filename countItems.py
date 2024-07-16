# We are going to check the frequency of the occurence of every item in the list and transfer the results into the dictionary

my_list = [1,1,1,1,2,2,3,4,4,4,4,5,6,6,3,4,67,7,8,2]

freq = {}
for i in my_list:
    if i not in freq:
        freq[i]=1
    else:
        freq[i]+=1
print(freq)