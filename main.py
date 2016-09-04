"""
# We use the following merge sort algorithm:

import inspect
import re
import sys
import os

list_to_sort = {}

def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

mergesort = \"""
import sys
import re
import inspect
import os


def merge(a, b):
    if len(a) == 0:
        return b
    elif len(b) == 0:
        return a
    elif a[0] < b[0]:
        return [a[0]] + merge(a[1:], b)
    else:
        return [b[0]] + merge(a, b[1:])

input_list = []
sublist = input_list
sorted_sublist = []
if len(sublist) < 2:
    sorted_sublist = sublist
else:

    print("sublist length: " + str(len(sublist)))
    split_point = len(sublist) // 2
    left_portion = sublist[:split_point]
    right_portion = sublist[split_point:]
    current_module = sys.modules[__name__]

    #for side in ("left", "right"):
    #    if side in sys.modules:
    #        del sys.modules[side]
    module_source = inspect.getsource(current_module)
    print(os.getcwd())

    with open("steps/left.py", "w") as file:
        new_list_slug = 'input_list = ' + str(left_portion)
        adjusted_source = re.sub(r'^input_list = \[.*\]', new_list_slug, module_source, flags=re.MULTILINE)
        file.write(adjusted_source)
    import steps
    print(dir(steps))
    import steps.left as sleft
    from sleft import sorted_sublist as left_sorted
    #from steps.left import
    os.remove("steps/left.py")

    with open("steps/right.py", "w") as file:
        new_list_slug = 'input_list = {{slug}}'.format(slug=right_portion)
        adjusted_source = re.sub(r'^input_list = \[.*\]', new_list_slug, module_source, flags=re.MULTILINE)
        file.write(adjusted_source)

    from .right import sorted_sublist as right_sorted
    os.remove("steps/right.py")
    #print(left_sorted)
    #print(right_sorted)
    sorted_sublist = merge(left_sorted, right_sorted)
\"""

#del sys.modules[__name__]
with open("steps/algo.py", "w") as file:
    import sys
    #mergesort.format(sublist=list_to_sort)#
    adjusted_source = mergesort.replace('input_list = []', 'input_list = ' + str(list_to_sort))
    file.write(adjusted_source)
#print(sys.path)
from steps.algo import sorted_sublist as sorted_list
os.remove("algo.py")
my_list = "ank"
#print(sorted_list)
"""
__author__ = 'rogueleaderr'

# basic merge sort implementation from http://stackoverflow.com/a/4574358/998687
import random
import os

if __name__ == "__main__":
    print("let's get started")
    to_sort = [random.randint(0, 100) for i in range(0, 100)]
    with open("mergesort.py", "w") as file:
        mergesort_code = __doc__.format(to_sort)
        #print(mergesort_code)
        file.write(mergesort_code)
    from mergesort import sorted_list
    os.remove("mergesort.py")
    print(sorted_list)
