input_string= "pwwkew"


#Hints:
#Using Hashtable, bitvector and in O(NlogN)

#Brute force approach O(n^2)
#
length = len(input_string)

for i in range(0, length):
    for j in range(1, length):
        if input_string[i] == input_string[j]:
            print("False")
            break


#Using O(n log n) approach
sorted_input_string = sorted(input_string)
for i in range(0, length-1):
    if (sorted_input_string[i] == sorted_input_string[i+1]):
        print("False")
        break

# print(sorted(input_string))