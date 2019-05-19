def valid_parentheses(string):
    pairs = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []
    for bracket in string: 
        if bracket in pairs.values(): 
            stack.append(bracket) 
        elif bracket in pairs.keys():  
            if (len(stack) > 0) and (pairs[bracket] == stack[-1]): 
                stack.pop() 
            else: 
                return False
    if len(stack) == 0: 
        return True
    else:
        return False
