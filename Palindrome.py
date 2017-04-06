#!/usr/bin/python

def isPalindrome(inputString):
    pass

# Positive Test Cases
positiveTestCases = ["mom", "racecar", "tacocat", "Hello, e olleh", "RIGHT!!! mom THGIR"]
print ("Testing Positive Test Cases:")
for testCase in positiveTestCases:
    if isPalindrome(testCase):
        print("PASS - Testcase:  %s" %(testCase))
    else:
        print("FAIL - Testcase:  %s" %(testCase))


print ("\n====================\n")

# Negative Test Cases
print ("Testing Negative Test Cases:")
negativeTestCases = ["Devin", "Villarosa", "Hi, my name is Devin!"]
for testCase in negativeTestCases:
    if not isPalindrome(testCase):
        print("PASS - Testcase:  %s" %(testCase))
    else:
        print("FAIL - Testcase:  %s" %(testCase))

print ("\n====================\n")

#Test Poetry Line
print ("Varifying palindromes in poem")
with open("./poetry.txt", 'r') as file:
    for line in file:
        cleanLine = line.strip()
        if cleanLine and isPalindrome(cleanLine):
            print("%s - is a Palindrome" %(cleanLine))
        else:
            print(cleanLine)

