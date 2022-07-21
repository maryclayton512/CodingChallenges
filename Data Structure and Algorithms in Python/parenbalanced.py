# import class Stack
from stackinpython import Stack
# Create new method is_match
def is_match(p1, p2):
    # if two symbols match, return true
    # else, false
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
# Create new method named paren_balanced
def is_paren_balanced(paren_string):
    # declare class Stack, state is_balanced, and index
    s = Stack()
    is_balanced = True
    i = 0
    # while index is less than length of string and balanced
    while i < len(paren_string) and is_balanced:
        # paren = index of string
        paren = paren_string[i] # i = index
        # if paren in string, push paren
        if paren in "([{":
            s.push(paren)
        # else if it's empty, state is false then break
        else:
            if s.is_empty():
                is_balanced = False
                break
            # else if string is not a match, state is false then break
            else:
                top = s.pop(0)
                if not is_match(top, paren):
                    is_balanced = False
                    break
            # counter
            i += 1
        # if string is empty and balanced, return true
        # else false
        if s.is_empty() and is_balanced:
            return True
        else:
            return False

# Output compare sides of balanced and non-balanced sides
print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))
    
