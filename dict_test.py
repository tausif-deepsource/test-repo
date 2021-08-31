import json
import datetime
import random


boom = {x: {x * 2} for x in range(10)}
# print(boom)


def func1(x, l1):
    """
    this was to test how function arguments can be modififed learning ->
    so only the mutable objects passed can be modifed as python takes function arguments as pointer to address value
    so List,Dict and other mutable types can be modified but int,str or other immutables cannot be changed inside
    function definition.
    """
    x = 5
    l1.append("nonsense")

    return l1


y = 10
list1 = ["meaning"]
func1(y, list1)
print(y)
print(list1)


class Dummy:
    def __init__(self):
        self.listy = []

    def append_listy(self, value):
        print(self.listy)
        self.listy.append(value)
        return self.listy

    def hello(self, a, b):
        if a + b:
            print("boo")
            raise Exception

        return a + b


a = Dummy()
print(a.hello(3, 4))
print(a.append_listy("boom"))
