from Lab2 import ArrayStack

class PalindromeChecker:
    def __init__(self):
        self.stack = ArrayStack

    def clean(self, text):
        #error if empty
        if text == "":
            raise ValueError("Input must contain at least one letter or number.\n")
        cleaned = ""
        #keep letters and numbers only
        for char in text:
            if char.isalnum():
                cleaned = cleaned + char.lower()
        return cleaned

    def is_palindrome(self, text):
        #remove trailing spaces and check if empty
        text = self.clean(text)
        self.stack = ArrayStack()

        for char in text:
            #skip if space
            if char == " ":
                continue
            self.stack.push(char)

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