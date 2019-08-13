#Question: Given a string, write a function to check if it is a permutation of a palindrome.
#Input: Tact Coa #Output True (permutations: "taco cat", "atco cta" etc.)
#Hints: #106 - Generate all permutations is inefficient
#121 - What characteristics does permutation of palindrome have?
#134 - Have you tried using hash table we should get it using O(N) time
#136 - Can you reduce the space size using a bit vector.

input_string = "Tact coa"
# input_string ="geeksogeeks"

#Using list which is extra space and O(N) complexity.
def permutation_palindrome(input_string):
    result_dict = []
    input_string = input_string.upper()
    input_string = input_string.replace(" ", "")
    for i in range(0, len(input_string)):
        if input_string[i] in result_dict:
             result_dict.remove(input_string[i])
        else:
            result_dict.append(input_string[i])

    if len(input_string)%2 == 0:
        if len(result_dict) ==0:
            print("True")
    elif len(result_dict) == 1:
            print("True")
    else:
        print("False")

permutation_palindrome(input_string)

#Using bit vectors instead of extra space in memory.
def permutation_palindrome_bit(input_string):
    input_string = input_string.upper()
    input_string = input_string.replace(" ", "")
    for i in range(0, len(input_string)):
        print(ord(input_string[i]))

    return True

permutation_palindrome_bit(input_string)
