#!/usr/bin/python

import unittest
import re

#Assumption: Input will be a word, phrase, or other sequence of characters is a palindrome.
def isPalindrome(inputString):

    if not isinstance(inputString, basestring):
        print ("Error: not of string type")
        return False

    # Ignore punctuation and whitespace
    cleanString = re.sub(r'[^\w]', '', inputString)

    # Ignore upper vs lowercase by making all uppercase
    for i in range(len(cleanString)//2):
        if cleanString[i].upper() != cleanString[-1-i].upper():
            return False

    return True

def palindromeDetection(fileLocation):
    print ("Varifying palindromes in poem")
    with open(fileLocation, 'r') as file:
        for line in file:
            cleanLine = line.strip()
            if cleanLine and isPalindrome(cleanLine):
                print("%s - is a Palindrome" %(cleanLine))
            else:
                print(cleanLine)


class TestPalindrome(unittest.TestCase):

    def test_positiveCase(self):
        positiveTestCases = ["mom", "racecar", "tacocat", "Hello, e olleh", "RIGHT!!! mom THGIR"]
        for testCase in positiveTestCases:
            self.assertTrue(isPalindrome(testCase))

    def test_negativeCase(self):
        negativeTestCases = ["Devin", "Villarosa", "Hi, my name is Devin!"]
        for testCase in negativeTestCases:
            self.assertFalse(isPalindrome(testCase))


if __name__ == '__main__':

     unittest.main()
