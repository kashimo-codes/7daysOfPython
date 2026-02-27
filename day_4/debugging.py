# Debugging 
#  The process of finding and correcting errors
#  or bugs in code.
#  Python includes a debugger called pdb to help
#  you figure out where your code is going wrong and
# how to fix it.

import pdb

def add_numbers(x,y):
    result = x + y
    pdb.set_trace() # Start the debugger at this point in the code
    return result


result = add_numbers(2,3)
print(result)