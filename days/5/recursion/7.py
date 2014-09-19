#handling tree-like structures

my_expression = ['+', 5, 6]

def eval(expr):
    if isinstance(expr, int):
        return expr
    else:
        if expr[0] == '+':
            return expr[1] + expr[2]



    
print eval(my_expression)
