#Question: There are three types of edits that can be performed on strings: insert, remove and replace. Given two strings, write a function to check if they are on edit or zero edits away.
#Hints:#23 Can you check each of the conditions seperately
#97 What is the relationship between the insert and remove character? Do these need to be seperate checks?
#130 Can you do all three checks in single pass.

input_one = "pale"
input_two = "bale"

#Time complexity is O(n) using additional data structure
def check_edits(input_one, input_two):
    count = 0
    length1 = len(input_one)
    length2 = len(input_two)
    hash_dict = []
    if length1 == length2:
        for i in range(0, length2):
            hash_dict.append(input_two[i])
        for j in range(0, length1):
            if input_one[j] not in hash_dict:
                count = count + 1
        if count == 1:
            print("True")
        else:
            print("False")
    elif length1 < length2 and length2-length1 == 1:
        for i in range(0, length2):
            hash_dict.append(input_two[i])
        for j in range(0, length1):
            if input_one[j] not in hash_dict:
                print("False")
                break
        else:
            print("True")
    elif length2 < length1 and length1-length2 == 1:
        for i in range(0, length1):
            hash_dict.append(input_one[i])
        for j in range(0, length2):
            if input_two[j] not in hash_dict:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")


check_edits(input_one, input_two)