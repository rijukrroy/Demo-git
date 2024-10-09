# Length of the longest substring with non-repeating characters
# Example string:
# - “ABCDEFGABEF” -> 7
# - “GEEKSFORGEEKS” -> 7

my_str = "GEEKSFORGEEKS"

def isNonRepeated(astr):
    alst = []
    for elem in astr:
        if elem not in alst:
            alst.append(elem)

    if astr == "".join(alst): # if there is any repeated characters:
        return True
    else:
        return False

max_length = ""
for i in range(len(my_str)):
    for j in range(i+1,len(my_str)+1):

        if(isNonRepeated(my_str[i:j])):
            # print(my_str[i:j])
            if len(my_str[i:j])> len(max_length):
                max_length = my_str[i:j]
        else:
            break
print("_______________________")
print(max_length)
