'''
sorted() -> Takes any iterable and returns a new sorted list without modifying original iterable

(Note: .sort() modifies original iterable)

Syntax:
`sorted(iterable, *, key=None, reverse=False)`

iterable -> can be a list of ints, a string, tuple, or even a dict
Note: sorted returns a list (even if input is string, tuple or a dict) ***


Dictionaries:
When sorting over a dictionary, by default sorted() takes the keys
So, `sorted(dict)` is the same as `sorted(dict.keys())`


'key' argument***:
When we pass key argument, it is a function that gets called which transforms each element before comparing
sorted(iterable, key=some_function)

ex:
nums = [-10, 3, -2, 5]
sorted(nums) -> [-10, -2, 3, 5]

But, sorted(nums, key=abs)  -> [-2, 3, 5, -10]


## Imp use case:
Sorting dict by the values
out = sorted(dict, key=dict.get)



'''