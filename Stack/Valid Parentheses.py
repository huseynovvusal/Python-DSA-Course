def isValid(s: str) -> bool:
    stack = []

    op = {
        ")" : "(",
        "}" : "{",
        "]" : "["
    }

    for c in s:
        if(len(stack) and c in op and stack[-1] == op[c]):
            stack.pop()
        else:
            stack.append(c)


    return len(stack) == 0

print(isValid('[(){}[]]'))
print(isValid('[(){}[]'))