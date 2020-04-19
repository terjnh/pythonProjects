# This is a Look-and-say sequence
# 1st term: 1
# 2nd term: 11 (Looking at 1st term, there is 1 '1')
# 3rd term: 21 (Refer to 2nd term, there are 2 '1's)
# 4th term: 1211 (Refer to 3rd term, there is 1 '2', and 1 '1')
# 5th term: 111221
# ............

# Task: To write a script which will allow us to determine the nth-term of a Look-and-Say Sequence

def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1  # count variable checks if the next index of the string 's' is the same char
        # Following while loop: determine if next char is same as current char
        while (i + 1) < len(s) and s[i] == s[i + 1]:
            i += 1
            count += 1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)

s = "1"  # 1st term of the sequence

print("Please enter the nth-term you wish to calculate to: ")
n = int(input())    # we want to calculate the 4th-term of the sequence

for i in range(n - 1):
    s = next_number(s)
    print(s)
