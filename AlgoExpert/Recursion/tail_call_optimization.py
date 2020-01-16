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


leetcode def:
Tail recursion is a recursion where the recursive call is the final instruction in the recursion function.
And there should be only one recursive call in the function.



"""



def tail_call_optimizatin(n, accumulator=1):
    if n == 0:
        return accumulator
    else:
        return tail_call_optimizatin(n - 1, n * accumulator)

print(tail_call_optimizatin(5))




def sum_non_tail_recursion(ls):

    if len(ls) == 0:
        return 0

    return ls[0] + sum_non_tail_recursion(ls[1:])

def sum_tail_recursion(ls):
    def helper(ls, acc):

        if len(ls) == 0:
            return acc

        return helper(ls[1:], ls[0] + acc)
    return helper(ls, 0)