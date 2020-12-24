from Stack import MyStack


'''
1) Loop over the input string
2) Push the values in the stack until finds an operator
3) Pop two values from the stack
4) Evaluate them and push the results back to the Stack
5) Continue from Step 1)
'''
def evaluate_post_fix(exp):
    # Write your code here
    stack = MyStack()
    arr = exp.split(',')
    for char in arr:
        if char.isdigit():
            stack.push(char)
        else:
            operand_2 = stack.pop()
            operand_1 = stack.pop()
            exp = operand_1 + char + operand_2
            result = str(int(eval(exp)))
            stack.push(result)
    return int(stack.pop())


# exp = '642/+' #"921*-8-4+"
exp = '9,4,2,+,*,6,14,7,/,+,*'
print(evaluate_post_fix(exp))
