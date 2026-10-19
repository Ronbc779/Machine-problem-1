from Lab2 import ArrayStack



class Converter:
    OPERATORS = "+-*/^"
    def precedence(self, op):
        if op == "^":
            return 3
        elif op == "*" or op == "/":
            return 2
        return 1
    def infix_to_postfix(self, expression):
        stack = ArrayStack()
        output = ""

        for char in expression:
            if char.isalpha():
                output = output + char

            elif char == "(":
                stack.push(char)

            elif char == ")":
                while not stack.is_empty() and stack.top() != "(":
                    output = output + stack.pop()
                if stack.is_empty():
                    raise ValueError("Unmatched ')'.")
                stack.pop()
            elif char in self.OPERATORS:
                while not stack.is_empty() and stack.top() != "(":
                    curr_precedence = self.precedence(char)
                    top_precedence = self.precedence(stack.top())
                    if top_precedence > curr_precedence or (top_precedence == curr_precedence and char != "^"):
                        output = output + stack.pop()
                    else:
                        break
                stack.push(char)
            else:
                raise ValueError("Invalid character '" + char + "'.")

        while not stack.is_empty():
            top = stack.pop()
            if top == "(":
                raise ValueError("Unmatched '('.")
            output = output + top

        return output

converter = Converter()

print(converter.infix_to_postfix("(a+b)*(a-b)"))