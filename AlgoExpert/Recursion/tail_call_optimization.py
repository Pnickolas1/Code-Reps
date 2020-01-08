"""

Tail Call optimization:

- tail call optimization is when the recursion call is the last thing in the function before it returns
- hence the name "the recursive function call comes at the "tail" of the function
- the call stack never grows in size
- TCO prevents stack overflows
- tail call optimzation is a compiler trick,
- Cpython interpreter does not implement TCO, and it never will
    - its not pythonic
- TCO is not used in python , its irrelevent
- understand the call stack
- a function call pushes a frame onto the call stack and a return pops a stack off


"""



def tail_call_optimizatin(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_call_optimizatin(n - 1, n * accumulator)

print(tail_call_optimizatin(5))
