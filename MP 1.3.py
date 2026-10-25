from Lab2 import ArrayStack

class PalindromeChecker:
    def __init__(self):
        self.stack = ArrayStack()

    #removes unnecessary characters/special symbols and trailing spaces
    def clean(self, text):
        cleaned = ""
        #keep letters and numbers only
        for char in text:
            if char.isalnum():
                cleaned = cleaned + char.lower()
        #error if empty
        if cleaned == "":
            raise ValueError("Input must contain at least one letter or number.\n")
        return cleaned

    def is_palindrome(self, text):
        #remove trailing spaces and check if empty
        text = self.clean(text)
        self.stack = ArrayStack()

        for char in text:
            self.stack.push(char)
        #check if it matches letter by letter
        for char in text:
            if self.stack.pop() != char:
                return False

        return True


print("=====PALINDROME CHECKER=====\n")
string = input("Enter string: ")

check = PalindromeChecker()

try:
    if check.is_palindrome(string):
        print('"' + string + '" is a palindrome.')
    else:
        print('"' + string + '" is NOT a palindrome.')
except ValueError as error:
    print("Error:", error )