#Question: Write a method to replace all spaces in string with %20
#Sample Input: "Mr John Smith ", 13 #Sample Output "Mr%20John%20Smith"
#Goal is to perform the operation in place.
#hint53: Often easiest to modify strings from the end of the string to the beginnnig.
#Hint 118: You might find you need to know the number of spaces. Can you just count them?



string_one = "Mr John Smith "
length = 13

#Method using predefined method replace function
# def replace(string_one, length):
#     string_one = string_one.strip()
#     replaced_string = string_one.replace(' ', '%20')
#     return replaced_string
# result = replace(string_one, length)
# print(result)

#Method using inplace algorithm and auxilary space is O(1)
def replace_inplace(string_one, length):

    #converting to character array
    string_one = list(string_one)

    #Deleting white space if present at the end of the string
    if string_one[len(string_one)-1] == " ":
        del string_one[len(string_one)-1]

    #Replacing based on ascii values, can get the ascii value based on ord function method.
    for i in range(0, length):
        if ord(string_one[i]) == 32:
            string_one[i] = '%20'
    return "".join(string_one)

result = replace_inplace(string_one, length)

print(result)

#Conclusion: Strings are immutable, You cannot replace a character in a string, so convert to character array to modify characters in inplace.
