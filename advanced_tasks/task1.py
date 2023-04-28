# todo: Magic Methods.
# Description
# You have to overload the addition operator in Counter class. Use the add() magic method to overload the addition.
#
# For example, in case of a + b, a object should have add() which accepts b as a second parameter (self goes first).
#
# In this case, Counter object accepts a list from int as a parameter. Object to summarize with will be a str object.
# The result should be a list of strings which have the following pattern: 1 test - one object from list and str separated by the whitespace.
#
# Example
# >>> Counter([1, 2, 3]) + "mississippi"
# ["1 mississippi", "2 mississippi" , "3 mississippi"]
#
# Шаблон:
# from typing import List
# class Counter:
#     def init(self, values: List[int]):
#         self.values = values
#     # TODO: add your code here

class Counter:
    def __init__(self, lst: [int]):
        self.values = lst

    def __add__(self, other:str):
        return [str(val) + " " + other for val in self.values]

print(Counter([1, 2, 3]) + "mississippi")