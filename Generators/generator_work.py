
"""
Generator Notes:

- yield is the indicating value to determine a generator function
- the state of the function is remembered , so when you can next() on the generator func
- generators are a great way to optimize for memeory


## understanding the yield statement
- in order to control the yield statement, you can assign the generator func to a variable and call
    next() on the variable like -> next(generator_assignment)
- when the yield value is hit, the function gets suspended, and the value gets returned to the caller
- like iterators, generators can be exhausted, meaning if you hit the end and call next, it will blow up
    (unles the generator is infinite)
- stopIteration is a natural exception that's raised to signal the end of an iterator
-

"""

def csv_reader(file_name):
    for row in open(file_name, "r"):
        yield row

row_count = 0

csv_gen = csv_reader("techcrunch.csv")
for row in csv_gen:
    row_count += 1

print(f"Row count is {row_count}")



def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1




gen = infinite_sequence()