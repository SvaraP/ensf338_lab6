import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_expression_tree(tokens):
    if len(tokens) == 1:
        return TreeNode(int(tokens[0]))
    
    stack = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == '(':
            stack.append(token)
        elif token.isdigit():
            node = TreeNode(int(token))
            if stack and stack[-1] in ['+', '-', '*', '/']:
                operator = stack.pop()
                node.left = stack.pop()
                node.right = node
                node = TreeNode(operator)
            stack.append(node)
        elif token in ['+', '-', '*', '/']:
            stack.append(token)
        elif token == ')':
            sub_expr = []
            while stack[-1] != '(':
                sub_expr.append(stack.pop())
            stack.pop()  # pop '('
            stack.append(build_expression_tree(sub_expr))
        i += 1
    
    while len(stack) > 1:
        right = stack.pop()
        operator = stack.pop()
        left = stack.pop()
        node = TreeNode(operator)
        node.left = left
        node.right = right
        stack.append(node)
    
    return stack[0]

def evaluate_expression_tree(root):
    if root.value.isdigit():
        return int(root.value)
    
    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)
    
    if root.value == '+':
        return left_val + right_val
    elif root.value == '-':
        return left_val - right_val
    elif root.value == '*':
        return left_val * right_val
    elif root.value == '/':
        return left_val / right_val

def evaluate_expression(expression):
    tokens = expression.split()
    expression_tree = build_expression_tree(tokens)
    return evaluate_expression_tree(expression_tree)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python arithmetic_interpreter.py 'expression'")
    else:
        expression = sys.argv[1]
        result = evaluate_expression(expression)
        print("Result:", result)


