#!/usr/bin/python
# -*- coding: utf-8 -*-

def f(x):
	return x * x
r = map(f, [1, 2, 3, 4, 5])
print(list(r))

from functools import reduce
def fn(x, y):
	return x * 10 + y
def char2num(s):
	return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn, map(char2num, '13579')))

def normalize(n):
	return n[0].upper() + n[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce
def  prod(L):
	def f(x, y):
		return x * y
	return reduce(f, L)
	# print(reduce(lambda x, y:x * y,[1, 2, 3, 4, 5, 6]))#
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))


from functools import reduce
def  str2float(s):
	n = s.index('.')
	s1 = s[:n]
	s2 = s[n+1:][::-1]# + '0'
	return reduce(lambda x, y: x + y,
					[
						reduce(lambda x, y: x * 10 + y, map(lambda x: int(x), s1)),
						reduce(lambda x, y: x / 10 + y, map(lambda x: int(x), s2))
					])
	#return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print('str2float(\'123.456\') =', str2float('1243.4586'))

#def str2float(s):
#    n = s.index('.')
#    s = s.replace('.', '')
#    def char2num(s):
#        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
#    def str2int(s):
#        return reduce(lambda x, y: x * 10 + y, map(char2num, s))
#    return str2int(s) / (10 ** n )



