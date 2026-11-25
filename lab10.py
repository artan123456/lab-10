# Problem-solving practice 2 (competition / LeetCode style) - a step up in difficulty.
#
# Most of these are natural fits for a STACK or a QUEUE (this week's data structures).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def eval_rpn(tokens): # Restate: Put it in a stack and do reverse polish notation using that stack
    # Outline (write your plan here first):
    #  Example: 2 1 + 3 * Should be: 2, 2 1, 2 1 +, 3, 3 3, 3 3 *, 9
    # Put the operands into the stack
    # Whenever you reach an operator, run it (operate it?) on the two operands
    # Remove the two from the top of the stack & replace with the operation's result
    operators : str = "+-/*"
    stack = [] 
    for i in range(len(tokens)):
        current_token : str = tokens[i]
        
        if (current_token in operators):
            # It is an operator so do the operation
            result = 0
            if (current_token == "*"):
                stack[-2] = stack[-1] * stack[-2]
            elif (current_token == "/"):
                stack[-2] = int(stack[-2] / stack[-1])
            elif (current_token == "+"):
                stack[-2] = stack[-1] + stack[-2]
            elif (current_token == "-"):
                stack[-2] = stack[-2] - stack[-1]
            stack.pop()
        else:
            # It is an operand so put it into the stack
            stack.append(int(current_token))   

    return stack[0] # Return the result
        



def decode_string(s): # Restated: take the value in the brackets and repeat the number that many times
    # Outline:
    # Solving 3[a2[c]]: 3[acc], accaccacc
    # Stack: 3, 3 a, 3 a 2, 3 a 2 c if you reach a closing bracket, go back until you reach an open bracket, get the number and create a new string copied that many times
    stack = []
    result : str = ""
    # No square brackets
    if "[" not in s:
        return s # Return the string itself

    for i in range(len(s)):
        char : str = s[i]
        if char in "1234567890":
            stack.append(int(char)) # Make sure this is a number
        elif char == "[":
            if s[i+1] not in "1234567890":
                # It is not followed by a number, start an empty string
                stack.append("") 
        elif char == "]":
            top = stack[-1]
            stack.pop()
            second = stack[-1]
             
            if type(top) == type("hi") and type(second) == type(12345): # Make sure num is actually a number and text is actually a string
                # This is the part of the stack where we multiply
                stack.pop()
                text = second * top # I remember this from one of the lectures
                stack.append(text)
            elif type(top) == type("hi") and type(second) == type("hi"):
                # Don't multiply here, append instead
                stack.pop()
                newTop = second + top
                stack.append(newTop)
        else:
            # Character
            stack[-1] += char # Add char to the string

    # Pretending it is a stack so I wont use .join
    while (len(stack) > 1):
        top = stack.pop()
        second = stack.pop()
        if type(top) == type("hi") and type(second) == type(12345): 
            text = second * top 
            stack.append(text)
        elif type(top) == type("hi") and type(second) == type("hi"):
            newTop = second + top
            stack.append(newTop)

    result = str(stack.pop()) 

    return result







    
            



    


def daily_temperatures(temps): # Restated: Use a stack to see how many days after a given day a warmer day comes
    # Outline:
    # Start with a stack (temps but reversed)
    # Calculate the number of days until a warmer day for each day and store results in a stack
    # Original: [4, 3, 5]
    # Start from []
    # Check 4 (warmer day after 2 days), push (append) 2
    # [2]
    # Do the same for 3 (warmer after 1 day), push (append) 1
    # [2, 1]
    # The last one is zero no matter what because a warmer day cant come after the last day
    # [2, 1, 0]

    stack = []

    for i in range(len(temps)): # No need to look at the last one, that is 0 no matter what
        count = 0
        for j in range(i, len(temps)):
            if (temps[j] > temps[i]): 
                # Warmer day found
                stack.append(count)
                break
            count += 1 # Counting how many days
            if (j + 1 == len(temps)):
                # We have reached the end and were not able to find any warmer days
                stack.append(0)
                break

    #stack.append(0) # Final day does not have any following days
    return stack
            


    


def num_islands(grid):   # Part 4 - stretch (optional)
    pass


def main():
    # Optional scratch space - try your functions here, then run: python lab10.py
    pass


if __name__ == "__main__":
    main()
