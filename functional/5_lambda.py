#!/usr/bin/python
# -*- coding: utf-8 -*-

f = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 6, 7, 8, 9]))
print(f)

f = lambda x: x * x
print(f)
print(f(5))

def build(x, y):
	return lambda: x * x + y * y
print(build)
print(build(3, 5))