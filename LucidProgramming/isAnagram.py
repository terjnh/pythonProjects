## Write a function in python to determine if 2 strings are anagrams of each other

## s1 and s2 are anagrams
s1 = "fairy tales"
s2 = "rail safety"

# normalizing the strings
s1 = s1.replace(" ", "").lower()
s2 = s2.replace(" ", "").lower()

## sort chars in s1 and s2 by ascending order
## this method below requires 'n log n time' (since any comparison-based sorting algorithm requires at least 'n log n time' to sort)
# print(sorted(s1) == sorted(s2))

# Alternative method which makes use of a dict / hash table
def is_anagram(s1, s2):
    ht = dict()
    isAnagram = True

    ## Use this conditional, if both strings are different length -> Definitely not anagrams
    if len(s1) != len(s2):
        return "Both strings are different in length. Hence they can't be anagrams."

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1
    
    print("ht after processing s1:\n {}".format(ht))

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1
    
    print("ht after processing s2:\n {}".format(ht))

    # loop through dict if any entries are not '0'  -->  we do not have an anagram!
    for i in ht:
        if ht[i] != 0:
            isAnagram = False
    
    if isAnagram == True:
        print("Both strings are anagrams")
    elif isAnagram == False:
        print("Both strings are NOT anagrams")

print(is_anagram(s1, s2))