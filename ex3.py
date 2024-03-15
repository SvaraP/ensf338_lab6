
#AI declaration:
#used it for the parse_expression fiunction

import sys

class TreeNode: #basic tree implementation like in the slides 
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def computation(node): #basic computional if/else statement lowkey the easiest part 
    if isinstance(node.value, str):
        left_val = computation(node.left)
        right_val = computation(node.right)

        if node.value == '+':
            return left_val + right_val
        elif node.value == '-':
            return left_val - right_val
        elif node.value == '*':
            return left_val * right_val
        elif node.value == '/':
            return left_val / right_val
    else:
        return node.value

def parse(tokens):
    if len(tokens) == 1:
        tok = int(tokens[0])
        return TreeNode((tok))
    
    if tokens[0] == '(' and tokens[-1] == ')':
        tokens = tokens[1:-1]  # Remove surrounding parentheses

    count = 0
    last_index = -1
    for i, token in enumerate(tokens):
        if token == '(':
            count += 1
        elif token == ')':
            count -= 1
        elif count == 0 and token in ['+', '-', '*', '/']:
            last_index = i
    
    if last_index != -1: #recursively callz the fuction to parse each half of the code
        left = parse(tokens[:last_index])
        right = parse(tokens[last_index+1:])
        return TreeNode(tokens[last_index], left, right)

    raise ValueError("Invalid expression")

def main():
    if len(sys.argv) != 2:
        sys.exit(1)

    math = sys.argv[1]
    tokens = math.split()
    try:
        root = parse(tokens)
        value = computation(root)
        value = int(value)
        print(value)
    except ValueError as error:
        print(f"Error {error}")

if __name__ == "__main__":
    main()