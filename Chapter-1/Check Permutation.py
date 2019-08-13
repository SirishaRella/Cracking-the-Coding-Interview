#Question: Given two strings check if one string is permutation of another.
#Hints: #1: Check strings permutation according to the definition
#84 Two solutions O(N log N) and O(N)
#122 Hashtable be useful?
#131 Two strings that have permutation have different orders. Can the orders be samee?

string1 = "abccb"
string2 = "bccab"

#O(nlogn) with sorting
# def check_two_strings(string1, string2):
#     sorted_string1 = "".join(sorted(string1))
#     sorted_string2 = "".join(sorted(string2))
#     if sorted_string1==sorted_string2:
#         print("True")
#     else:
#         print("False")

#With hash map => o(n)
def check_two_strings_hash(string1, string2):
    string_dict = {}

    #Storing all characters of a string2 in dictionary
    for i in range(0, len(string2)):
        if string2[i] in string_dict:
            string_dict[string2[i]] =  string_dict[string2[i]] + 1
        else:
            string_dict[string2[i]] = 1

    #Checking for characters of string1 in string_dict
    for key in range(0, len(string1)):
        if string1[key] in string_dict:
            string_dict[string1[key]] = string_dict[string1[key]] - 1


    #Check for counts in dictionary
    for key in string_dict:
        if string_dict[key] != 0:
            print("False")
        else:
            print("True")
        break


#check_two_strings(string1, string2)
check_two_strings_hash(string1, string2)
