#!/usr/bin/python

import re

# TODO: Improve to O(n/2) performance by comparing the first half to the second half of the string backwards.
#   But for this exercise, I'll leave it to be more legible

#Assumption: Input will be a word, phrase, or other sequence of characters is a palindrome.
def isPalindrome(inputString):

    if not isinstance(inputString, basestring):
        print ("Error: not of string type")
        return False


    # Ignore puncutation and whitespace
    cleanString = re.sub(r'[^\w]', '', inputString)

    # Ignore upper vs lowercase
    return cleanString.upper() == cleanString[::-1].upper()


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

