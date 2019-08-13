#Question: Implement a method to perform basic string compression using the counts of repeated characters.
#For example aabcccccaaa would be a2b1c5a3, if the compression string is more than original return original string
#Hints: #92 Do the easy thing first compress the string and compare the lengths
#110 Be careful that you are repeatedly concatenating strings together. This can be very in efficient

input_string = "abc"

#Time complexity is O(N). Important is last edge case.
def string_compression(input_string):
    length = len(input_string)
    result_array = ""
    count = 1
    for i in range(0, length-1):
        if input_string[i] == input_string[i+1]:
            count = count + 1
        else:
            result_array += input_string[i] + str(count)
            count = 1
    result_array += input_string[i+1] + str(count)


    if len(result_array) > len(input_string):
        print(input_string)
    else:
        print(result_array)


string_compression(input_string)