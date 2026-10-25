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

        return "\nPOSTFIX:" + output

    def postfix_to_infix(self, expression):
        stack = ArrayStack()

        for char in expression:
            if char.isalpha():
                stack.push(char)

            elif char in self.OPERATORS:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.push(f"({op1}{char}{op2})")

            elif char in "()":
                raise ValueError("Invalid character: No parentheses in postfix.")

            else:
                raise ValueError("Invalid character: Letter operands and valid operators only")

        if not stack.is_empty():
            if stack.top().isalpha():
                raise ValueError(f"Unmatched operand(s) {stack.top()} <<<")
            if stack.top() in self.OPERATORS:
                raise ValueError(f"Unmatched operator {stack.top()} <<<")

        return stack.pop()


class main():
    converter = Converter()
    while 1:
        print("\n===== FIX CONVERTER =====")
        choice = int(input("What do you want to do?\n1. Infix to Postfix\n2. Postfix to Infix\n3. Exit\n>> "))

        match choice:
            #call infix to postfix method
            case 1:
                expression  = input("\nEnter Infix expression: ")
                print(converter.infix_to_postfix(expression))
            #call postfix to infix method
            case 2:
                expression  = input("\nEnter Postfix expression: ")
                print(converter.postfix_to_infix(expression))
                pass
            case _:
                break